import socket
import pickle
import threading

class Server():
    def __init__(self):
        self.threading = threading.Thread(target=self.run)
        self.threading.start()
        self.threading_work = True
    def run(self):
        global socket
        socket = socket.socket()
        socket.bind(('', 12341))
        socket.listen(2)
        connect_host, addres_host = socket.accept()
        connect_client, addres_client = socket.accept()

        print(
        f'''
        ip хоста: {addres_host}
        ip клиента: {addres_client}
        ''')

        connect_host.send(pickle.dumps({'command': 'start'}))
        connect_client.send(pickle.dumps({'command': 'start'}))


        game_configurations = connect_host.recv(1024)
        connect_client.send(game_configurations)

        while self.threading_work:
            data = connect_host.recv(1024)
            if not data:
                break
            data = pickle.loads(data)

            if data.get('role') == 'host':
                data_for_client = data
            else:
                data_for_host = data
            print(data)



            data = connect_client.recv(1024)
            if not data:
                break
            data = pickle.loads(data)

            if data.get('role') == 'host':
                data_for_client = data
            else:
                data_for_host = data
            print(data)


            connect_host.send(pickle.dumps(data_for_host))
            connect_client.send(pickle.dumps(data_for_client))

        socket.close()

    def stop(self):
        self.threading_work = False

if __name__ == '__main__':
    Server()
