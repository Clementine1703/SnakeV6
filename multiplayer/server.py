import socket
import pickle
import threading

class Server():
    def __init__(self):
        threading.Thread(target=self.run).start()
    def run(self):
        global socket
        socket = socket.socket()
        socket.bind(('', 12341))
        print(socket)
        socket.listen(1)
        connect_host, addres_host = socket.accept()
        connect_client, addres_client = socket.accept()

        some_data = {
            'command': 'start'
        }
        connect_host.send(pickle.dumps(some_data))
        connect_client.send(pickle.dumps(some_data))

        data_for_client = connect_host.recv(1024)
        connect_client.send(data_for_client)

        print(
        f'''
        ip хоста: {addres_host}
        ip клиента: {addres_client}
        ''')

        while True:
            pass
            # data = connect_host.recv(1024)
            # if not data:
            #     break
            # data = pickle.loads(data)

            # if data.get('host'):
            #     data_for_client = data
            # else:
            #     data_for_host = data
            # print(data)






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

if __name__ == '__main__':
    Server()
