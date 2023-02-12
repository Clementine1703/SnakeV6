from settings import *
import pygame

class Snake:
    def __init__(self, values):
        self.start_body = values['coordinates']
        self.body = values['coordinates']
        self.color = values['color']
        self.pside = values['side']
        self.side = values['side']
        self.kadr = 0
        self.upr = values['control']
        self.score = 0
        self.name = values['name']

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
                self.body.insert(
                    0, [self.body[0][0], active_settings['arena_size'][1] / active_settings['cell_size'] - 1])
                self.body.pop(-1)
            else:
                self.body.insert(
                    0, [self.body[0][0], self.body[0][1] - 1])
                self.body.pop(-1)
        if self.side == 'bottom':
            if self.body[0][1] >= active_settings['arena_size'][1] / active_settings['cell_size'] - 1:
                self.body.insert(0, [self.body[0][0], 0])
                self.body.pop(-1)
            else:
                self.body.insert(
                    0, [self.body[0][0], self.body[0][1] + 1])
                self.body.pop(-1)
        if self.side == 'left':
            if self.body[0][0] <= 0:
                self.body.insert(
                    0, [active_settings['arena_size'][0] / active_settings['cell_size'] - 1, self.body[0][1]])
                self.body.pop(-1)
            else:
                self.body.insert(
                    0, [self.body[0][0] - 1, self.body[0][1]])
                self.body.pop(-1)
        if self.side == 'right':
            if self.body[0][0] >= active_settings['arena_size'][0] / active_settings['cell_size'] - 1:
                self.body.insert(0, [0, self.body[0][1]])
                self.body.pop(-1)
            else:
                self.body.insert(
                    0, [self.body[0][0] + 1, self.body[0][1]])
                self.body.pop(-1)

    def draw_snake(self):  # Функция проходится по списку координат и рисует квадраты змейки
        for i in self.body:
            r = pygame.Rect(i[0] * active_settings['cell_size'], i[1] * active_settings['cell_size'],
                            active_settings['cell_size'], active_settings['cell_size'])
            pygame.draw.rect(screen, self.color, r, 0)
            if i == self.body[0]:  # рисуем глазки
                if self.side == 'top':
                    left_eye_coord = (
                        i[0] * active_settings['cell_size'] + (active_settings['cell_size'] / 2 - 4), i[1] * active_settings['cell_size'] + active_settings['cell_size'] / 2 - 3)
                    right_eye_coord = (
                        i[0] * active_settings['cell_size'] + (active_settings['cell_size'] / 2 + 4), i[1] * active_settings['cell_size'] + active_settings['cell_size'] / 2 - 3)
                elif self.side == 'bottom':
                    left_eye_coord = (
                        i[0] * active_settings['cell_size'] + (active_settings['cell_size'] / 2 - 4), i[1] * active_settings['cell_size'] + active_settings['cell_size'] / 2 + 3)
                    right_eye_coord = (
                        i[0] * active_settings['cell_size'] + (active_settings['cell_size'] / 2 + 4), i[1] * active_settings['cell_size'] + active_settings['cell_size'] / 2 + 3)
                elif self.side == 'right':
                    left_eye_coord = (
                        i[0] * active_settings['cell_size'] + (active_settings['cell_size'] / 2 + 3), i[1] * active_settings['cell_size'] + active_settings['cell_size'] / 2 - 4)
                    right_eye_coord = (
                        i[0] * active_settings['cell_size'] + (active_settings['cell_size'] / 2 + 3), i[1] * active_settings['cell_size'] + active_settings['cell_size'] / 2 + 4)
                else:
                    left_eye_coord = (
                        i[0] * active_settings['cell_size'] + (active_settings['cell_size'] / 2 - 3), i[1] * active_settings['cell_size'] + active_settings['cell_size'] / 2 - 4)
                    right_eye_coord = (
                        i[0] * active_settings['cell_size'] + (active_settings['cell_size'] / 2 - 3), i[1] * active_settings['cell_size'] + active_settings['cell_size'] / 2 + 4)

                pygame.draw.circle(
                    screen, (0, 0, 0), left_eye_coord, 2)
                pygame.draw.circle(
                    screen, (0, 0, 0), right_eye_coord, 2)

    def snake_crush_check(self, test=False):
        if test == False:
            # если столкновения в настройках включены
            if active_settings['crush'] == 'on':
                if self.body[0] in self.body[1:-1:1]:
                    return self.gameover(type='crush')
                for i in snakes_list:
                    if self != i:
                        if self.body[0] in i.body[0:-1:1]:
                            # ппроверка на взаимное столкновение (ничью)
                            if self.body[0] == i.body[0] and self.take_side_tehn() == -i.take_side_tehn():
                                return self.gameover(type='crush', no_winner=True)
                            else:
                                return self.gameover(type='crush')
            else:  # если столкновения выключены
                pass
        else:  # если нам нужна только информация есть ли столкновение без вывода сообщения о конце игры
            # если столкновения в настройках включены
            if active_settings['crush'] == 'on':
                if self.body[0] in self.body[1:-1:1]:
                    return True
                for i in snakes_list:
                    if self != i:
                        if self.body[0] in i.body[0:-1:1]:
                            return True
            else:  # если столкновения выключены
                pass

    def score_winner_check(self):
        if active_settings['score_winning']:
            if self.score >= active_settings['score_winning']:
                for i in snakes_list:
                    if self != i:
                        if self.score == i.score:
                            return self.gameover(type='score', no_winner=True)
                return self.gameover(type='score')

    def gameover(self, type, no_winner=False):
        nonlocal current_speed

        # окно будет обновляться каждую 999999999 секунду, то есть зависнет (типа конец игры)
        current_speed = 999999999

        apple.coordinates = [[-99999, -99999, -99999,
                             -99999]]  # в конце раунда яблочко выносится далеко з а экран и удаляется
        apple.delete_apple()

        screen.blit(font_gameover.render(f'Игра окончена', True, active_settings['colors']['APPLE']),  # ывод надписи о конце игры
                    # расположили текст окончания раунда
                    (active_settings['arena_size'][0] / 2 - 230, active_settings['arena_size'][1] / 2 - 80))
        screen.blit(font_score.render(f'для рестарта нажмите "R"', True, active_settings['colors']['APPLE']),
                    (active_settings['arena_size'][0] / 2 - 200, active_settings['arena_size'][1] / 2 - 5))

        if no_winner == False:  # вывод победителя на экран
            if type == 'crush':  # если конец игры вызван столкновением
                color = [
                    i.color for i in snakes_list if i.color != self.color]
                name = [i.name for i in snakes_list if i != self]
            if type == 'score':  # если конец игры назван набором очков
                color = [self.color]
                name = [self.name]

            screen.blit(font_score.render(f'Победитель: {name[0]}', True, color[0]),
                        # расположили текст окончания раунда
                        (active_settings['arena_size'][0] / 2 - 230, active_settings['arena_size'][1] / 2 - 160))
        if no_winner == True:
            screen.blit(font_score.render(f'НИЧЬЯ', True, (0, 0, 0)),
                        # расположили текст окончания раунда
                        (active_settings['arena_size'][0] / 2 - 40, active_settings['arena_size'][1] / 2 - 160))

        return True

    def snake_event_check(self):  # отслеживавем нажатие клавиш
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
        apple_points = 1 + active_settings['apple_big']
        if self.body[0] in apple.coordinates:
            # увеличивается на 2 деления при съедании большого яблока
            if its_a_test == False:
                for i in range(apple_points):
                    self.body.insert(-1, [self.body[-1][0] - self.body[-2][0] - self.body[-1][0],
                                          self.body[-1][1] - self.body[-2][1] - self.body[-1][
                        1]])  # вставляем новый квадрат в конец змейки
            return apple_points
        return 0

    def apply_side_edit(
            self):  # так как направление головы может меняться много раз за кадр (сделали это искуственно)
        self.side = self.pside  # то не даем провести манипуляции разворачивающие змейку

    def show_score(self, x, y):
        screen.blit(font_score.render(
            f'{self.score}', True, self.color), (x, y))
