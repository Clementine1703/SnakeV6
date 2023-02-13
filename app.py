import pickle
import socket
import tkinter as tk
from functools import partial
from tkinter.ttk import *
from multiplayer import server, utils
from form_tools.form_constructors import create_button, create_checkbutton, create_combobox
from form_tools.form_synchronizators import syncing_setting_with_input

from settings import *
from game import Game


class Menu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('300x300') # размеры окна настроек
        self.title('Змеюка')
        self.resizable(width=False, height=False)   # запрет на изменение размера окна
        self.lbl = tk.Label(text='Главное меню', font='Arial 14', pady=30, ).pack()
        self.buttons = {}

        create_button(
                menu= self,
                button_name= 'start',
                menu_window= self,
                text= "Играть",
                function= partial(Game.start, active_settings),
        )

        create_button(
                menu= self,
                menu_window= self,
                button_name= 'settings',
                text= "Настройки",
                function= self.open_options_window,
        )

        create_button(
                menu=self,
                menu_window=self,
                button_name='multiplayer',
                text="Игра по сети",
                function=self.open_multiplayer_window,
        )


    def open_options_window(self):
        options = tk.Tk()  # создаем новое окно tkinter
        options.geometry('400x400')  
        options.title('Настройки')
        options.resizable(width=False, height=False)
        self.forms_storage = {}

        # создаем и рисуем все поля раздела "настройки"
        for form_element in data_for_generating_settings_fields:
            if form_element['type'] == 'combobox':
                create_combobox(self, menu_window=options, label_text=form_element['label_text'], setting_name=form_element['setting_name'], coordinates=form_element['coordinates'])
            else:
                create_checkbutton(self, menu_window=options, label_text=form_element['label_text'], setting_name=form_element['setting_name'], coordinates=form_element['coordinates'])



        create_button(
                menu= self,
                menu_window= options,
                button_name= 'save_options',
                text= "Сохранить",
                function= partial(self.change_options, options),
        )

    def change_options(self, menu_window):
        global active_settings

        # синхронизируем значение active_settings со значением инпута
        for form_element in data_for_generating_settings_fields:
            syncing_setting_with_input(self, setting_name=form_element['setting_name'], type=form_element['type'])

        menu_window.destroy()


    def open_multiplayer_window(self):
        multiplayer = tk.Tk()
        multiplayer.geometry('400x400') 
        multiplayer.title('Игра по сети')
        multiplayer.resizable(width=False, height=False)

        ip_input_lbl = Label(multiplayer, text='Введите ip адрес')
        ip_input_lbl.pack(padx=8, pady= 8)
        ip_input = tk.Entry(multiplayer)
        ip_input.pack()



        create_button(
                menu= self,
                menu_window= multiplayer,
                button_name= 'connect_to_host',
                text= "Подключиться",
                function= partial(self.connect_to_host, ip_input.get()),
        )

        ip_list_area = tk.Text(multiplayer ,width=25, height=5, bg="white",
            fg='black')
        ip_list_area.pack()


        ip_list = utils.get_ip_list()
        if type(ip_list) == list:
            ip_list_area.insert("1.0", f'ip адресы: \n{ip_list}')

        
        create_button(
                menu= self,
                menu_window= multiplayer,
                button_name= 'become_a_host',
                text= "Стать хостом",
                function= self.open_wait_for_connection_window,
        )

    def connect_to_host(self, ip_address):
        sock = socket.socket()
        sock.connect((ip_address, 12341))
        print('connected')

        data = sock.recv(1024)
        if not data:
                pass
        data = pickle.loads(data)
        if (data['command'] == 'start'):
            data = sock.recv(1024)
            if not data:
                pass
            data = pickle.loads(data)

            global active_settings

            active_settings = data
            Game.start(active_settings)

    def open_wait_for_connection_window(self):
        wait_for_connection = tk.Tk()
        wait_for_connection.geometry('300x150')
        wait_for_connection.title('Ожидание 2-го игрока')
        wait_for_connection.resizable(width=False, height=False)

        ip_show_lbl = Label(wait_for_connection, text=utils.get_my_ip())
        ip_show_lbl.pack(padx=8, pady= 8)

        server.Server()

        sock = socket.socket()
        sock.connect(('127.0.0.1', 12341))
        print('connected')

        data = sock.recv(1024)
        if not data:
                pass
        data = pickle.loads(data)
        if (data['command'] == 'start'):
            sock.send(pickle.dumps(active_settings))
            Game.start(active_settings)

        


if __name__ == '__main__':
    app = Menu()
    app.mainloop()
