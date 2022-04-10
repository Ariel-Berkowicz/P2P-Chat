import socket
import threading

class Client:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.connect(('0.0.0.0', 5000))

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
            # check for disconnections
            if not data:
                break
            print(str(data, 'utf-8'))

c = Client()
print(c.sock)

# import socket, pickle
# import sys

# HOST = 'localhost'
# PORT = int(sys.argv[2])

# # Create a socket connection.
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((HOST, PORT))


# while True:
#     # received data from user input
#     data = input('Enter the data to be sent to the server: ')

#     # Pickle the object and send it to the server
#     data_string = pickle.dumps(data)
#     s.send(data_string)
#     print ('Data Sent to Server')

#     if data == 'exit':
#         s.close()
#         break