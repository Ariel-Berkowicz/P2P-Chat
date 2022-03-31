import socket, pickle
import sys

HOST = 'localhost'
PORT = int(sys.argv[2])

# Create a socket connection.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


while True:
    # received data from user input
    data = input('Enter the data to be sent to the server: ')

    # Pickle the object and send it to the server
    data_string = pickle.dumps(data)
    s.send(data_string)
    print ('Data Sent to Server')

    if data == 'exit':
        s.close()
        break