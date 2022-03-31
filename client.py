#! /usr/bin/python3

import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "155.41.101.57"
port =8000
s.connect((host,port))


def ts(str):
    # send the string to the server and print the response
    s.send(str.encode())
    data = s.recv(1024)
    print('Received from server:', data.decode())
    

    data = ''
    data = s.recv(1024).decode()
    print('Received from server: ' + data)

while 2:
    r = input('Testing\n')
    ts(s)

s.close ()