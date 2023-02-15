import os
import re
import socket
import pickle


def get_ip_list():
    try:
        global os
        devices = []
        for device in os.popen('arp -a'):
            devices.append(device)
        result = [
            device for device in devices if not '(incomplete)' in device and not 'ff:ff:ff:ff:ff:ff' in device and '192.168.' in device]
        result = [re.findall(r'\(.*?\)', el)[0][1:-1] for el in result]
        return (result)
    except:
        return ('Не получилось определить ip адреса в вашей сети, введите вручную')


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

    
    
