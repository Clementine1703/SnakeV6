import random
import pygame
from functools import partial

import tkinter as tk
from tkinter.ttk import *
from settings import *
from game import Game
from multiplayer import utils


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('300x300')
        self.title('Змеюка')
        self.resizable(width=False, height=False)
        self.lbl = tk.Label(text='Главное меню', font='Arial 14', pady=30, ).pack()
        self.buttons = {}

        self.create_button(
            active_settings={
                'button_name': 'start',
                'tk_object': self,
                'text': "Играть",
                'function': partial(Game.start, active_settings),
            }
        )

        self.create_button(
            active_settings={
                'button_name': 'settings',
                'tk_object': self,
                'text': "Настройки",
                'function': self.open_options,
            }
        )

        self.create_button(
            active_settings={
                'button_name': 'multiplayer',
                'tk_object': self,
                'text': "Игра по сети",
                'function': self.open_multiplayer,
            }
        )


    def open_options(self):
        options = tk.Tk()  # создаем новое окно tkinter
        options.geometry('400x400')  # размеры окна настроек
        options.title('Настройки')
        options.resizable(width=False, height=False)  # запрет изменять размер
        self.forms_storage = {}

        # создаем поле для каждой настройки
        self.create_combobox(options, label_text='Размер карты', setting_name='arena_size', coordinates={
            'lbl': (20, 60),
            'combobox': (110, 60),
        })

        self.create_combobox(options, label_text='Скорость:', setting_name='speed', coordinates={
            'lbl': (20, 95),
            'combobox': (110, 95),
        })

        self.create_combobox(options, label_text='Столкновения:', setting_name='crush', coordinates={
            'lbl': (20, 130),
            'combobox': (110, 130),
        })

        self.create_combobox(options, label_text='Счет для победы: ', setting_name='score_winning', coordinates={
            'lbl': (20, 165),
            'combobox': (120, 165),
        })

        self.create_checkbutton(options, label_text='Большое яблоко', setting_name='apple_big', coordinates={
            'checkbutton': (20, 200)
        })

        self.create_checkbutton(options, label_text='Случ. размер яблока после съедания', setting_name='apple_random_size', coordinates={
            'checkbutton': (20, 230)
        })

        # выставляем значения input в соответствии с нынешними настройками

        self.create_button(
            active_settings={
                'button_name': 'save_options',
                'tk_object': options,
                'text': "Сохранить",
                'function': partial(self.change_options, options),
            }
        )

        # отрисовываем все элементы


    def change_options(self, tk_object):
        global active_settings

        # устанавливаем значение настроек в соответствии с выбранным значением в инпуте
        self.syncing_setting_with_input(setting_name='arena_size', type='combobox')
        self.syncing_setting_with_input(setting_name='speed', type='combobox')
        self.syncing_setting_with_input(setting_name='crush', type='combobox')
        self.syncing_setting_with_input(setting_name='score_winning', type='combobox')

        self.syncing_setting_with_input(setting_name='apple_big', type='checkbutton')
        self.syncing_setting_with_input(setting_name='apple_random_size', type='checkbutton')

        tk_object.destroy()
        
    def create_button(self, active_settings):
        # создает и возвращает объект кнопки

        self.buttons[active_settings['button_name']] = tk.Button(active_settings['tk_object'], text=active_settings['text'],  # текст кнопки
                           width='10',
                           background="#fff",  # фоновый цвет кнопки
                           foreground="#000",  # цвет текста
                           padx="12",  # отступ от границ до содержимого по горизонтали
                           pady="6",  # отступ от границ до содержимого по вертикали
                           font="Arial 10",  # высота шрифта
                           relief='raised',
                           command=active_settings['function']
                           )

        self.buttons[active_settings['button_name']].pack(pady=5)

    def create_combobox(self, tk_object, label_text, setting_name, coordinates):
        self.forms_storage[setting_name] = {
            'lbl': Label(tk_object, text=label_text),
            'combobox': Combobox(tk_object, state='readonly')
        } 
        self.forms_storage[setting_name]['combobox']['values'] = get_setting_titles(
            all_settings[setting_name])

        self.forms_storage[setting_name]['lbl'].place(x=coordinates['lbl'][0], y=coordinates['lbl'][1])
        self.forms_storage[setting_name]['combobox'].place(x=coordinates['combobox'][0], y=coordinates['combobox'][1])

        self.syncing_input_with_setting(setting_name, type='combobox')

    def create_checkbutton(self, tk_object, label_text, setting_name, coordinates):
        self.forms_storage[setting_name] = {}
        self.forms_storage[setting_name]['checkbutton_variable'] = tk.IntVar(tk_object)
        self.forms_storage[setting_name]['checkbutton'] = Checkbutton(tk_object, text=label_text,
                                      variable=self.forms_storage[setting_name]['checkbutton_variable'],
                                      onvalue=1, offvalue=0,
                                      )

        self.forms_storage[setting_name]['checkbutton'].place(x=coordinates['checkbutton'][0], y=coordinates['checkbutton'][1])

        self.syncing_input_with_setting(setting_name, type='checkbutton')

    def syncing_input_with_setting(self, setting_name, type):
        # устанавливает значение инпутов в соответствии с значением настроек

        global active_settings
        global all_settings

        if type == 'combobox':
            self.forms_storage[setting_name]['combobox'].current(
            get_setting_index_by_value(
                (active_settings[setting_name]),
                all_settings[setting_name]
            )
        )
        elif type == 'checkbutton':
            self.forms_storage[setting_name]['checkbutton_variable'].set(
            int(get_setting_index_by_value(
                active_settings[setting_name],
                all_settings[setting_name]
                )
            )
        )

    def syncing_setting_with_input(self, setting_name, type):
        if type == 'combobox':
            active_settings[setting_name] = get_setting_value_by_title(
            self.forms_storage[setting_name]['combobox'].get(),
            all_settings[setting_name]
            )
        elif type == 'checkbutton':
            active_settings[setting_name] = bool(int(self.forms_storage[setting_name]['checkbutton_variable'].get()))

    def open_multiplayer(self):
        multiplayer = tk.Tk()  # создаем новое окно tkinter
        multiplayer.geometry('400x400')  # размеры окна настроек
        multiplayer.title('Игра по сети')
        multiplayer.resizable(width=False, height=False)  # запрет изменять размер

        ip_input_lbl = Label(multiplayer, text='Введите ip адрес')
        ip_input = tk.Entry(multiplayer)
        ip_input_lbl.pack(padx=8, pady= 8)
        ip_input.pack()

        ip_list_area = tk.Text(multiplayer ,width=25, height=5, bg="white",
            fg='black')
        ip_list_area.pack()

        ip_list = utils.get_ip_list()
        if type(ip_list) == list:
            ip_list_area.insert("1.0", f'ip адресы: \n{ip_list}')


if __name__ == '__main__':
    app = App()
    app.mainloop()
