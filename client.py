import socket
import threading
from p2p import p2p

class Client:
    def __init__(self, add):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.connect((add, 5000))
        print('Connected as client...')

    def update_peers(self, data):
        p2p.peers = str(data, 'utf-8').split(',')

    def worker(self):
        while True:
            self.sock.send(bytes(input(""), 'utf-8'))

    def run(self):
        # Data sending thread
        sendTh = threading.Thread(target=self.worker, daemon=True)
        sendTh.start()

        # Data receivng thread
        while True:
            data = self.sock.recv(1024)
            # Check for disconnections
            if not data:
                break
            # Check for peers list
            if data[0:1] == b'\x11':
                print('Peers updated')
                self.update_peers(data[1:])
            else:
                print(str(data, 'utf-8'))
