import random
import pygame
from functools import partial

import tkinter as tk
from tkinter.ttk import *
from settings import *
from game import Game


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('300x300')
        self.title('Змеюка')
        self.resizable(width=False, height=False)

        self.lbl = tk.Label(text='Главное меню', font='Arial 14', pady=30, )
        self.lbl.pack()

        self.btn_start = self.create_button(
            active_settings={
                'tk_object': self,
                'text': "Играть",
                'function': partial(Game.start, active_settings),
            }
        )

        self.btn_settings = self.create_button(
            active_settings={
                'tk_object': self,
                'text': "Настройки",
                'function': self.open_options,
            }
        )

        self.btn_start.pack()
        self.btn_settings.pack(pady=5)

    def open_options(self):
        options = tk.Tk()  # создаем новое окно tkinter
        options.geometry('400x400')  # размеры окна настроек
        options.title('Настройки')
        options.resizable(width=False, height=False)  # запрет изменять размер
        self.forms_storage = {}

        options.lbl = tk.Label(options, text='Настройки',
                               font='Arial', pady=15).place(x=95)

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

        button_save = self.create_button(
            active_settings={
                'tk_object': options,
                'text': "Сохранить",
                'function': self.change_options,
            }
        )

        # отрисовываем все элементы
        button_save.place(x=20, y=270)

    def change_options(self):
        global active_settings

        # устанавливаем значение настроек в соответствии с выбранным значением в инпуте
        self.syncing_setting_with_input(setting_name='arena_size', type='combobox')
        self.syncing_setting_with_input(setting_name='speed', type='combobox')
        self.syncing_setting_with_input(setting_name='crush', type='combobox')
        self.syncing_setting_with_input(setting_name='score_winning', type='combobox')

        self.syncing_setting_with_input(setting_name='apple_big', type='checkbutton')
        self.syncing_setting_with_input(setting_name='apple_random_size', type='checkbutton')


    def create_button(self, active_settings):
        # создает и возвращает объект кнопки

        button = tk.Button(active_settings['tk_object'], text=active_settings['text'],  # текст кнопки
                           width='10',
                           background="#fff",  # фоновый цвет кнопки
                           foreground="#000",  # цвет текста
                           padx="12",  # отступ от границ до содержимого по горизонтали
                           pady="6",  # отступ от границ до содержимого по вертикали
                           font="Arial 10",  # высота шрифта
                           relief='raised',
                           command=active_settings['function']
                           )
        return button

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

if __name__ == '__main__':
    app = App()
    app.mainloop()
