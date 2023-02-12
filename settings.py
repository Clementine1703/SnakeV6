
active_settings = {
    'colors': {'SNAKE': (102, 153, 0), 'WHITE': (255, 255, 255), 'WINDOW': (255, 255, 153), 'GREEN': (0, 255, 0),
               'APPLE': (102, 0, 0), 'BLUE': (153, 255, 255), 'FIOLET': (153, 51, 255), 'PINK': (255, 153, 255)},
    'arena_size': (900, 600), # размеры поля
    'cell_size': 25, # размер минимального деления поля (1 клеточки)
    'fps': 60,  # кадры в секунду
    'speed': 6,
    'apple_big': True, # размер яблока
    'apple_random_size': True,
    'crush': 'on', # столкновения
    'score_winning': False, # выйгрыш по счету
}

snake_start_settings = {
    '1': {'coordinates': [[0, 2], [0, 1], [0, 0]], 'side': 'bottom', 'control': 1,'color': active_settings['colors']['SNAKE'], 'name': 'ЗЕЛЁНАЯ змеюка'},
    '2': {'coordinates':[[active_settings['arena_size'][0] / active_settings['cell_size'] - 1, active_settings['arena_size'][1] / active_settings['cell_size'] - 3],[active_settings['arena_size'][0] / active_settings['cell_size'] - 1,active_settings['arena_size'][1] / active_settings['cell_size'] - 2],[active_settings['arena_size'][0] / active_settings['cell_size'] - 1, active_settings['arena_size'][1] / active_settings['cell_size'] - 1]],'side': 'top','control': 2, 'color':active_settings['colors']['FIOLET'],
            'name':'ФИОЛЕТОВАЯ змеюка'}
}

all_settings = {
    'arena_size': [
        {
            'value': (600, 400),
            'title': ' 600x400 '
        },
        {
            'value': (900, 600),
            'title': ' 900x600 '
        },
        {
            'value': (1000, 700),
            'title': ' 1000x700 '
        },
        {
            'value': (1200, 800),
            'title': ' 1200x800 '
        },


    ],
    'speed': [
        {
            'value': 30,
            'title': ' Медленно ',
        },
        {
            'value': 20,
            'title': ' Средне ',
        },
        {
            'value': 12,
            'title': ' Выше среднего ',
        },
        {
            'value': 6,
            'title': ' Быстро ',
        },
        {
            'value': 4,
            'title': ' Очень быстро ',
        },
        {
            'value': 3,
            'title': ' Со скоростью света ',
        },
    ],
    'score_winning': [
        {
            'value': False,
            'title': ' Отключить '
        },
        {
            'value': 10,
            'title': ' 10 очков '
        },
        {
            'value': 20,
            'title': ' 20 очков '
        },
        {
            'value': 30,
            'title': ' 30 очков '
        },
        {
            'value': 40,
            'title': ' 40 очков '
        },
        {
            'value': 50,
            'title': ' 50 очков '
        },
        {
            'value': 100,
            'title': ' 100 очков '
        },
    ],
    'apple_big': [
        {
            'value': False,
            'title': ' Маленькое яблоко '
        },
        {
            'value': True,
            'title': ' Большое яблоко '
        },
    ],
    'apple_random_size': [
        {
            'value': False,
            'title': ' Фиксированный размер '
        },
        {
            'value': True,
            'title': ' Случайный размер '
        },
    ],
    'crush': [
        {
            'value': 'on',
            'title': ' Включить '
        },
        {
            'value': 'off',
            'title': ' Отключить '
        },
    ]
}

def get_setting_titles(setting_objects):
    values = [value['title'] for value in setting_objects]
    print(values)
    return values

def get_setting_value_by_title(title, setting_objects):
    value = [obj['value'] for obj in setting_objects if obj['title'] == title][0]
    return value

def get_setting_index_by_value(value, setting_objects):
    setting_object = [obj for obj in setting_objects if obj['value'] == value][0]
    index = setting_objects.index(setting_object)
    return index
