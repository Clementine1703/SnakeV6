import socket
import pickle
from multiprocessing import Process

class Server():
    def __init__(self):
        Process(target=self.run, daemon=True)
    def run():
        global socket
        socket = socket.socket()
        socket.bind(('', 12341))
        socket.listen(2)
        connect_host, addres_host = socket.accept()
        # connect_client, addres_client = socket.accept()

        print(f'''
        Клиент 1
        ip: {addres_host}
        Клиент 2
        ip: addres_client
        ''')

        while True:
            data = connect_host.recv(1024)
            if not data:
                break
            data = pickle.loads(data)

            if data.get('host'):
                data_for_client = data
            else:
                data_for_host = data
            print(data)






            # data = connect_client.recv(1024)
            # if not data:
            #     break
            # data = pickle.loads(data)

            # if data.get('host'):
            #     data_for_client = data
            # else:
            #     data_for_host = data
            # print(data)


            # connect_host.send(pickle.dumps(data_for_host))
            # connect_client.send(pickle.dumps(data_for_client))

