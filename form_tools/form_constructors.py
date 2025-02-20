import tkinter as tk
from tkinter.ttk import *
from settings import *
from .form_synchronizators import syncing_input_with_setting


def create_button(menu, menu_window, button_name, text, function):
    # создает и рисует объект кнопки

    menu.buttons[button_name] = tk.Button(menu_window, text=text,  # текст кнопки
                                          width='10',
                                          background="#fff",  # фоновый цвет кнопки
                                          foreground="#000",  # цвет текста
                                          padx="12",  # отступ от границ до содержимого по горизонтали
                                          pady="6",  # отступ от границ до содержимого по вертикали
                                          font="Arial 10",  # высота шрифта
                                          relief='raised',
                                          command=function
                                          )

    menu.buttons[button_name].pack(
        pady=5)


def create_combobox(menu, menu_window, label_text, setting_name, coordinates):
    menu.forms_storage[setting_name] = {
        'lbl': Label(menu_window, text=label_text),
        'combobox': Combobox(menu_window, state='readonly')
    }
    menu.forms_storage[setting_name]['combobox']['values'] = get_setting_titles(
        all_settings[setting_name])

    menu.forms_storage[setting_name]['lbl'].place(
        x=coordinates['lbl'][0], y=coordinates['lbl'][1])
    menu.forms_storage[setting_name]['combobox'].place(
        x=coordinates['combobox'][0], y=coordinates['combobox'][1])

    syncing_input_with_setting(menu, setting_name, type='combobox')


def create_checkbutton(menu, menu_window, label_text, setting_name, coordinates):
    menu.forms_storage[setting_name] = {}
    menu.forms_storage[setting_name]['checkbutton_variable'] = tk.IntVar(
        menu_window)
    menu.forms_storage[setting_name]['checkbutton'] = Checkbutton(menu_window, text=label_text,
                                                                  variable=menu.forms_storage[
                                                                      setting_name]['checkbutton_variable'],
                                                                  onvalue=1, offvalue=0,
                                                                  )

    menu.forms_storage[setting_name]['checkbutton'].place(
        x=coordinates['checkbutton'][0], y=coordinates['checkbutton'][1])

    syncing_input_with_setting(menu, setting_name, type='checkbutton')
