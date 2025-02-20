import os
import re
import socket
import pickle


def get_my_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


def make_server_request(socket_object, multiplayer_data):
    message = pickle.dumps(multiplayer_data)
    socket_object.send(message)
    multiplayer_data = socket_object.recv(1024)
    if not multiplayer_data:
        pass
    multiplayer_data = pickle.loads(multiplayer_data)
    return multiplayer_data

    
    
