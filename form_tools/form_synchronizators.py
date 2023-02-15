from tkinter.ttk import *
from settings import *

# синхронизируем значение active_settings со значением инпута
def syncing_setting_with_input(menu, setting_name, type):
    if type == 'combobox':
        active_settings[setting_name] = get_setting_value_by_title(
            menu.forms_storage[setting_name]['combobox'].get(),
            all_settings[setting_name]
        )
    elif type == 'checkbutton':
        active_settings[setting_name] = bool(
            int(menu.forms_storage[setting_name]['checkbutton_variable'].get()))


 # устанавливаем значение инпутов в соответствии с значениями active_settings
def syncing_input_with_setting(menu, setting_name, type):


    if type == 'combobox':
        menu.forms_storage[setting_name]['combobox'].current(
            get_setting_index_by_value(
                (active_settings[setting_name]),
                all_settings[setting_name]
            )
        )
    elif type == 'checkbutton':
        menu.forms_storage[setting_name]['checkbutton_variable'].set(
            int(get_setting_index_by_value(
                active_settings[setting_name],
                all_settings[setting_name]
            )
            )
        )
