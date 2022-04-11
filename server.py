import socket
import threading

class Server:
    def __init__(self, add):
        self.connections = []
        self.peers = []
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((add, 5000))
        self.sock.listen(1)
        print('Server started...')

    def broadcast_peers(self):
        peers_list = ",".join(self.peers)
        for c in self.connections:
            c.send(b'\x11' + bytes(peers_list, 'utf-8'))

    def worker(self, conn, add):
        while True:
            data = conn.recv(1024)

            # check for disconnections
            if not data:
                print(add, 'disconnected...')
                self.connections.remove(conn)
                self.peers.remove(add[0])
                self.broadcast_peers()
                conn.close()
                break

            # Sending to the rest of the connections
            for c in self.connections:
                c.send(data)

    def run(self):
        # Connections accepting thread
        while True:
            conn, add = self.sock.accept()
            print(add, 'connected...')
            self.connections.append(conn)
            self.peers.append(add[0])
            self.broadcast_peers()

            # Managing each connection thread
            recvTh = threading.Thread(target=self.worker, args=(conn, add), daemon=True)
            recvTh.start()
