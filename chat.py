from http import client
import time
from random import randint
from server import Server
from client import Client
from p2p import p2p

p2p_peers = []

while True:
    print('Adding you to P2P network...')
    time.sleep(randint(1, 5))
    for p in p2p.peers:
        # First try connecting to a client
        # if there is already a server
        try:
            client = Client(p)
            client.run()
        except:
            pass

        # If there is no server then connect
        # as a server
        try:
            server = Server(p)
            server.run()
        except:
            pass
