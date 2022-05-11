import random
import pygame
import tkinter as tk
from tkinter.ttk import *

COLORS = {'SNAKE': (102, 153, 0), 'WHITE': (255, 255, 255), 'WINDOW': (255, 255, 153), 'GREEN': (0, 255, 0),
          'APPLE': (102, 0, 0), 'BLUE': (153, 255, 255), 'FIOLET': (153, 51, 255), 'PINK': (255, 153, 255)}
WINDOW_WIDTH = 900
WINDOW_HEIGTH = 600
SIZE = 25
FPS = 60
SPEED_OPT = 6
SPEED = 6
APPLE_SIZE = 'big'  # small / big
APPLE_RAND = True
CRUSH = 'on'  # on / off
SCORE_BORDER = 'off'  # int or 'off'


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.first_open = True
        self.geometry('300x300')
        self.title('Змеюка')
        self.resizable(width=False, height=False)

        self.lbl = tk.Label(text='Главное меню', font='Arial 14', pady=30, )
        self.lbl.pack()

        self.btn_start = tk.Button(self, text='Играть',  # текст кнопки
                                   width='18',
                                   background="#77ff00",  # фоновый цвет кнопки
                                   foreground="#fff",  # цвет текста
                                   padx="12",  # отступ от границ до содержимого по горизонтали
                                   pady="6",  # отступ от границ до содержимого по вертикали
                                   font="Arial 10",  # высота шрифта
                                   relief='raised',
                                   command=self.start_game
                                   )

        self.btn = tk.Button(self, text='Настройки',  # текст кнопки
                             width='18',
                             background="#77ff00",  # фоновый цвет кнопки
                             foreground="#fff",  # цвет текста
                             padx="12",  # отступ от границ до содержимого по горизонтали
                             pady="6",  # отступ от границ до содержимого по вертикали
                             font="Arial 10",  # высота шрифта
                             relief='raised',
                             command=self.open_options
                             )

        self.btn_start.pack()
        self.btn.pack(pady=5)

    def open_options(self):
        options = tk.Tk()  # создаем новое окно tkinter
        options.geometry('300x400')  # размеры окна настроек
        options.title('Настройки')
        options.resizable(width=False, height=False)  # запрет изменять размер

        options.lbl = tk.Label(options, text='Настройки', font='Arial', pady=15)  # заголовок "настройки"
        options.lbl.place(x=95)

        sizes = [(600, 400), (900, 600), (1000, 700), (1200, 800)]  # возможные значения переменных
        speeds = [30, 20, 12, 6, 4, 3]
        scores = ['off', 10, 20, 30, 40, 50, 100]
        apple_sizes = ['small', 'big']
        apple_rand = [False, True]
        crush_options = ['on', 'off']

        self.size_lbl = Label(options, text="Размер карты:")
        self.size_radio = Combobox(options, state='readonly')
        self.size_radio['values'] = (1, 2, 3, 4)

        self.speed_lbl = Label(options, text="Скорость:")
        self.speed_radio = Combobox(options, state='readonly')
        self.speed_radio['values'] = (1, 2, 3, 4, 5, 6)

        self.crush_lbl = Label(options, text="Столкновения:")
        self.crush_radio = Combobox(options, state='readonly')
        self.crush_radio['values'] = ("on", "off")

        self.score_lbl = Label(options, text="Счет для победы")
        self.score_radio = Combobox(options, state='readonly')
        self.score_radio['values'] = ('off', 10, 20, 30, 40, 50, 100)

        self.cb = tk.IntVar(options)
        self.cb1 = tk.IntVar(options)

        self.apple_size = Checkbutton(options, text="Большое яблоко",
                                      variable=self.cb,
                                      onvalue=1, offvalue=0,
                                      )
        self.apple_random = Checkbutton(options, text="Случ. размер яблока после съедания",
                                        variable=self.cb1,
                                        onvalue=1, offvalue=0,
                                        )

        self.apple_size.place(x=20, y=200)
        self.apple_random.place(x=20, y=230)

        global WINDOW_WIDTH
        global WINDOW_HEIGTH
        global SPEED_OPT
        global SPEED
        global APPLE_SIZE
        global APPLE_RAND
        global CRUSH
        global SCORE_BORDER

        self.size_radio.current(sizes.index((WINDOW_WIDTH, WINDOW_HEIGTH)))
        self.speed_radio.current(speeds.index(SPEED_OPT))
        self.crush_radio.current(crush_options.index(CRUSH))
        self.score_radio.current(scores.index(SCORE_BORDER))
        self.cb.set(apple_sizes.index(APPLE_SIZE))
        self.cb1.set(apple_rand.index(APPLE_RAND))

        save_button = tk.Button(options, text='Сохранить',  # текст кнопки
                                width='10',
                                background="#fff",  # фоновый цвет кнопки
                                foreground="#000",  # цвет текста
                                padx="12",  # отступ от границ до содержимого по горизонтали
                                pady="6",  # отступ от границ до содержимого по вертикали
                                font="Arial 10",  # высота шрифта
                                relief='raised',
                                command=self.change_options
                                )
        save_button.place(x=20, y=270)

        self.size_lbl.place(x=20, y=60)  # отрисовываем все элементы
        self.size_radio.place(x=110, y=60)
        self.speed_lbl.place(x=20, y=95)
        self.speed_radio.place(x=110, y=95)
        self.crush_lbl.place(x=20, y=130)
        self.crush_radio.place(x=110, y=130)
        self.score_lbl.place(x=20, y=165)
        self.score_radio.place(x=125, y=165)

    def change_options(self):
        sizes = [(600, 400), (900, 600), (1000, 700), (1200, 800)]
        speeds = [30, 20, 12, 6, 4, 3]
        scores = ['off', 10, 20, 30, 40, 50, 100]
        apple_sizes = ['small', 'big']
        apple_rand = [False, True]
        crush_options = ['on', 'off']

        global WINDOW_WIDTH
        global WINDOW_HEIGTH
        global SPEED_OPT
        global SPEED
        global APPLE_SIZE
        global APPLE_RAND
        global CRUSH
        global SCORE_BORDER

        WINDOW_WIDTH = sizes[int(self.size_radio.get()) - 1][0]
        WINDOW_HEIGTH = sizes[int(self.size_radio.get()) - 1][1]
        SPEED_OPT = speeds[int(self.speed_radio.get()) - 1]
        SPEED = SPEED_OPT
        APPLE_SIZE = apple_sizes[int(self.cb.get())]
        APPLE_RAND = apple_rand[int(self.cb1.get())]
        CRUSH = self.crush_radio.get()
        if self.score_radio.get() != 'off':
            SCORE_BORDER = int(self.score_radio.get())

        self.first_open = False

    def start_game(self):
        pygame.init()
        pygame.font.init()
        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGTH))
        pygame.display.set_caption('Змеюка')
        clock = pygame.time.Clock()
        font_score = pygame.font.Font(None, 36)
        font_gameover = pygame.font.Font(None, 100)

        running = True

        class Snake:
            def __init__(self, body, side, upr, color, name):
                self.start_body = body
                self.body = body
                self.color = color
                self.pside = side
                self.side = side
                self.kadr = 0
                self.upr = upr
                self.score = 0
                self.name = name



            def take_side_tehn(self):
                self.side_tehn = 0  # параметр для проверки противоположных направлений змеек
                if self.side == 'top':
                    self.side_tehn = 1
                elif self.side == 'bottom':
                    self.side_tehn = -1
                elif self.side == 'right':
                    self.side_tehn = 2
                else:
                    self.side_tehn = -2
                return self.side_tehn


            def one_step(
                    self):  # Функция которая проверяет не касается ли змейка рамок окна, и не съела ли змейка яблоко
                if self.side == 'top':
                    if self.body[0][1] <= 0:  # коснулась окна
                        self.body.insert(0, [self.body[0][0], WINDOW_HEIGTH / SIZE])
                        self.body.pop(-1)
                    else:
                        self.body.insert(0, [self.body[0][0], self.body[0][1] - 1])
                        self.body.pop(-1)
                if self.side == 'bottom':
                    if self.body[0][1] >= WINDOW_HEIGTH / SIZE - 1:
                        self.body.insert(0, [self.body[0][0], 0])
                        self.body.pop(-1)
                    else:
                        self.body.insert(0, [self.body[0][0], self.body[0][1] + 1])
                        self.body.pop(-1)
                if self.side == 'left':
                    if self.body[0][0] <= 0:
                        self.body.insert(0, [WINDOW_WIDTH / SIZE, self.body[0][1]])
                        self.body.pop(-1)
                    else:
                        self.body.insert(0, [self.body[0][0] - 1, self.body[0][1]])
                        self.body.pop(-1)
                if self.side == 'right':
                    if self.body[0][0] >= WINDOW_WIDTH / SIZE - 1:
                        self.body.insert(0, [0, self.body[0][1]])
                        self.body.pop(-1)
                    else:
                        self.body.insert(0, [self.body[0][0] + 1, self.body[0][1]])
                        self.body.pop(-1)

            def draw_snake(self):  # Функция проходится по списку координат и рисует квадраты змейки
                for i in self.body:
                    r = pygame.Rect(i[0] * SIZE, i[1] * SIZE, SIZE, SIZE)
                    pygame.draw.rect(screen, self.color, r, 0)
                    if i == self.body[0]:  # рисуем глазки
                        if self.side == 'top':
                            left_eye_coord = (i[0] * SIZE + (SIZE / 2 - 4), i[1] * SIZE + SIZE / 2 - 3)
                            right_eye_coord = (i[0] * SIZE + (SIZE / 2 + 4), i[1] * SIZE + SIZE / 2 - 3)
                        elif self.side == 'bottom':
                            left_eye_coord = (i[0] * SIZE + (SIZE / 2 - 4), i[1] * SIZE + SIZE / 2 + 3)
                            right_eye_coord = (i[0] * SIZE + (SIZE / 2 + 4), i[1] * SIZE + SIZE / 2 + 3)
                        elif self.side == 'right':
                            left_eye_coord = (i[0] * SIZE + (SIZE / 2 + 3), i[1] * SIZE + SIZE / 2 - 4)
                            right_eye_coord = (i[0] * SIZE + (SIZE / 2 + 3), i[1] * SIZE + SIZE / 2 + 4)
                        else:
                            left_eye_coord = (i[0] * SIZE + (SIZE / 2 - 3), i[1] * SIZE + SIZE / 2 - 4)
                            right_eye_coord = (i[0] * SIZE + (SIZE / 2 - 3), i[1] * SIZE + SIZE / 2 + 4)

                        pygame.draw.circle(screen, (0, 0, 0), left_eye_coord, 2)
                        pygame.draw.circle(screen, (0, 0, 0), right_eye_coord, 2)

            def snake_crush_check(self, test = False):
                if test == False:
                    if CRUSH == 'on':  # если столкновения в настройках включены
                        if self.body[0] in self.body[1:-1:1]:
                            return self.gameover(type = 'crush')
                        for i in snakes_list:
                            if self != i:
                                if self.body[0] in i.body[0:-1:1]:
                                    if self.body[0] == i.body[0] and self.take_side_tehn() == -i.take_side_tehn(): #ппроверка на взаимное столкновение (ничью)
                                        return self.gameover(type = 'crush',no_winner = True)
                                    else:
                                        return self.gameover(type = 'crush')
                    else:  # если столкновения выключены
                        pass
                else:       #если нам нужна только информация есть ли столкновение без вывода сообщения о конце игры
                    if CRUSH == 'on':  # если столкновения в настройках включены
                        if self.body[0] in self.body[1:-1:1]:
                            return True
                        for i in snakes_list:
                            if self != i:
                                if self.body[0] in i.body[0:-1:1]:
                                    return True
                    else:  # если столкновения выключены
                        pass

            def score_winner_check(self):
                if SCORE_BORDER != 'off':
                    if self.score >= SCORE_BORDER:
                        for i in snakes_list:
                            if self != i:
                                if self.score == i.score:
                                    return self.gameover(type = 'score', no_winner=True)
                        return self.gameover(type = 'score')

            def gameover(self,type, no_winner = False ):
                global SPEED
                SPEED = 999999999  # окно будет обновляться каждую 999999999 секунду, то есть зависнет (типа конец игры)

                apple.coordinates = [-99999, -99999, -99999,
                                     -99999]  # в конце раунда яблочко выносится далеко з а экран и удаляется
                apple.delete_apple()

                screen.blit(font_gameover.render(f'Игра окончена', True, COLORS['APPLE']), #ывод надписи о конце игры
                            # расположили текст окончания раунда
                            (WINDOW_WIDTH / 2 - 230, WINDOW_HEIGTH / 2 - 80))
                screen.blit(font_score.render(f'для рестарта нажмите "R"', True, COLORS['APPLE']),
                            (WINDOW_WIDTH / 2 - 200, WINDOW_HEIGTH / 2 - 5))

                if no_winner == False: #вывод победителя на экран
                    if type == 'crush': #если конец игры вызван столкновением
                        color = [i.color for i in snakes_list if i.color != self.color]
                        name = [i.name for i in snakes_list if i != self]
                    if type == 'score': #если конец игры назван набором очков
                        color = [self.color]
                        name = [self.name]

                    screen.blit(font_score.render(f'Победитель: {name[0]}', True, color[0]),
                                # расположили текст окончания раунда
                                (WINDOW_WIDTH / 2 - 230, WINDOW_HEIGTH / 2 - 160))
                if no_winner == True:
                    screen.blit(font_score.render(f'НИЧЬЯ', True, (0,0,0)),
                                # расположили текст окончания раунда
                                (WINDOW_WIDTH / 2 - 40, WINDOW_HEIGTH / 2 - 160))

                return True

            def game_quit(self):  # конец игры
                nonlocal running
                running = False
                # raise Exception('чтобы tkinter не завис!')
                # self.restart()

            # def restart(self):
            #     self.body=self.start_body

            def snake_event_check(self):  # отслеживавем нажатие кллавиши
                if self.upr == 1:

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_w:
                            if self.side != 'bottom':
                                self.pside = 'top'
                        if event.key == pygame.K_s:
                            if self.side != 'top':
                                self.pside = 'bottom'
                        if event.key == pygame.K_a:
                            if self.side != 'right':
                                self.pside = 'left'
                        if event.key == pygame.K_d:
                            if self.side != 'left':
                                self.pside = 'right'
                if self.upr == 2:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            if self.side != 'bottom':
                                self.pside = 'top'
                        if event.key == pygame.K_DOWN:
                            if self.side != 'top':
                                self.pside = 'bottom'
                        if event.key == pygame.K_LEFT:
                            if self.side != 'right':
                                self.pside = 'left'
                        if event.key == pygame.K_RIGHT:
                            if self.side != 'left':
                                self.pside = 'right'

            def apple_eat_check(self,
                                its_a_test=False):  # проверяем координаты головы змеи на совпадение с координатами яблока
                global APPLE_SIZE
                if APPLE_SIZE == 'small':
                    if self.body[0] == apple.coordinates:
                        if its_a_test == False:
                            self.body.insert(-1, (self.body[-1][0] - self.body[-2][0] - self.body[-1][0],
                                                  self.body[-1][1] - self.body[-2][1] - self.body[-1][
                                                      1]))
                        return 1
                    return 0
                if APPLE_SIZE == 'big':
                    if self.body[0] in apple.coordinates:
                        # увеличивается на 2 деления при съедании большого яблока
                        if its_a_test == False:
                            for i in range(2):
                                self.body.insert(-1, [self.body[-1][0] - self.body[-2][0] - self.body[-1][0],
                                                      self.body[-1][1] - self.body[-2][1] - self.body[-1][
                                                          1]])  # вставляем новый квадрат в конец змейки
                        return 2
                    return 0

            def apply_side_edit(
                    self):  # так как направление головы может меняться много раз за кадр (сделали это искуственно)
                self.side = self.pside  # то не даем провести манипуляции разворачивающие змейку

            def show_score(self, x, y):
                screen.blit(font_score.render(f'{self.score}', True, self.color), (x, y))

        class Apple:
            def __init__(self):
                global APPLE_SIZE
                global APPLE_RAND

                if APPLE_RAND == True:
                    APPLE_SIZE = random.choice(['big', 'small'])

                if APPLE_SIZE == 'small':
                    opt_side = False
                    wrong_coords = [k for i in snakes_list for k in
                                    i.body]  # координаты в которых не может появиться яблоко (тело змей)
                    while opt_side == False:
                        x = random.randint(0, WINDOW_WIDTH / SIZE - 1)
                        y = random.randint(0, WINDOW_HEIGTH / SIZE - 1)
                        if (x, y) not in wrong_coords:
                            self.coordinates = [x, y]
                            opt_side = True
                            break

                if APPLE_SIZE == 'big':
                    opt_side = 0
                    wrong_coords = [k for i in snakes_list for k in
                                    i.body]  # координаты в которых не может появиться яблоко (тело змей)
                    while opt_side != 4:
                        x = random.randint(0, WINDOW_WIDTH / SIZE - 2)
                        y = random.randint(0, WINDOW_HEIGTH / SIZE - 2)
                        apple_parts = [[x, y], [x + 1, y], [x + 1, y + 1], [x, y + 1]]
                        self.coordinates = []
                        opt_side = 0
                        for i in apple_parts:
                            if i not in wrong_coords:
                                self.coordinates = apple_parts
                                opt_side += 1

            def draw_apple(self):
                c = self.coordinates
                if APPLE_SIZE == 'small':
                    try:
                        pygame.draw.circle(screen, COLORS['APPLE'], (c[0] * SIZE + SIZE / 2, c[1] * SIZE + SIZE / 2),
                                           SIZE / 2)
                    except:
                        pass
                if APPLE_SIZE == 'big':
                    try:
                        pygame.draw.circle(screen, COLORS['APPLE'], (c[0][0] * SIZE + SIZE, c[0][1] * SIZE + SIZE),
                                           SIZE)
                    except:
                        pass

            def delete_apple(self):
                del self

        snake = Snake([[0, 2], [0, 1], [0, 0]], 'bottom', 1, color=COLORS['SNAKE'], name='ЗЕЛЁНАЯ змеюка')
        snake1 = Snake(
            [[WINDOW_WIDTH / SIZE - 1, WINDOW_HEIGTH / SIZE - 3],
             [WINDOW_WIDTH / SIZE - 1, WINDOW_HEIGTH / SIZE - 2],
             [WINDOW_WIDTH / SIZE - 1, WINDOW_HEIGTH / SIZE - 1]], 'top', 2, color=COLORS['FIOLET'],
            name='ФИОЛЕТОВАЯ змеюка')
        snakes_list = [snake, snake1]

        game_paused = False

        def pause_switch():  # ставим паузу
            nonlocal screen
            global SPEED
            nonlocal game_paused
            if not game_paused:
                SPEED = 99999999
                game_paused = True
            else:
                SPEED = SPEED_OPT
                game_paused = False

        apple = Apple()
        global SPEED

        while running:
            clock.tick(FPS)
            screen.fill(COLORS['WINDOW'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    SPEED = SPEED_OPT

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        del snake
                        del snake1
                        snake = Snake([[0, 2], [0, 1], [0, 0]], 'bottom', 1, color=COLORS['SNAKE'], name='ЗЕЛЁНАЯ змеюка')
                        snake1 = Snake(
                            [[WINDOW_WIDTH / SIZE - 1, WINDOW_HEIGTH / SIZE - 3],
                             [WINDOW_WIDTH / SIZE - 1, WINDOW_HEIGTH / SIZE - 2],
                             [WINDOW_WIDTH / SIZE - 1, WINDOW_HEIGTH / SIZE - 1]], 'top', 2, color=COLORS['FIOLET'], name='ФИОЛЕТОВАЯ змеюка')

                        snakes_list = [snake, snake1]
                        del apple
                        apple = Apple()

                        SPEED = SPEED_OPT
                    if event.key == pygame.K_p:  # ставим паузу
                        pause_switch()

                snake.snake_event_check()
                snake1.snake_event_check()

            if snake.kadr % SPEED == 0:  # кадров в секунду 30, но змейка будет двигаться каждый 5й кадр
                snake.apply_side_edit()
                snake1.apply_side_edit()
                snake.one_step()
                snake1.one_step()
                snake.draw_snake()
                snake1.draw_snake()
                if not snake.snake_crush_check(): #что
                    snake1.snake_crush_check()
                elif snake.snake_crush_check(test=True) and snake1.snake_crush_check(test=True):
                    pass
                snake.show_score(20, 10)
                snake1.show_score(WINDOW_WIDTH - 40, 10)
                if not snake.score_winner_check():
                    snake1.score_winner_check()

                if (snake.apple_eat_check(its_a_test=True) != 0) and (
                        snake1.apple_eat_check(
                            its_a_test=True) != 0):  # я в шоке чтобы если два съели оба наелись если не два то 1 наелся
                    for i in snakes_list:
                        i.score += i.apple_eat_check()
                    del apple
                    apple = Apple()
                else:
                    for i in snakes_list:
                        if i.apple_eat_check(its_a_test=True) != 0:
                            i.score += i.apple_eat_check()
                            del apple
                            apple = Apple()

                apple.draw_apple()
                pygame.display.flip()

            snake.kadr += 1

        pygame.display.quit()
        pygame.quit()


if __name__ == '__main__':
    game = App()
    game.mainloop()
