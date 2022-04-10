import socket
import threading

class Server():
    def __init__(self):
        self.connections = []
        self.peers = []
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(('0.0.0.0', 5000))
        self.sock.listen(1)

    def broadcast_peers(self):
        pass

    def worker(self, conn, add):
        while True:
            data = conn.recv(1024)

            # check for disconnections
            if not data:
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
            self.connections.append(conn)
            self.peers.append(add[0])
            self.broadcast_peers()

            # Managing each connection thread
            recvTh = threading.Thread(target=self.worker, args=(conn, add), daemon=True)
            recvTh.start()

# import socket
# from threading import *
# import sys

# serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# host = str(sys.argv[1])
# port = int(sys.argv[2])

# print(host)
# print(port)
# serversocket.bind((host, port))


# class client(Thread):
#     def __init__(self, socket, address):
#         Thread.__init__(self)
#         self.sock = socket
#         self.addr = address
#         self.start()

#     def run(self):
#         while 1:
#             print('Client sent:', self.sock.recv(1024).decode())
#             self.sock.send(b'Oi you sent something to me')


# serversocket.listen(5)
# print('server started and listening')
# while 1:
#     clientsocket, address = serversocket.accept()
#     client(clientsocket, address)
