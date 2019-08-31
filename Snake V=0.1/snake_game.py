# -*- coding: utf-8 -*-
#game version 0.1

import pygame #подключаем модуль pygame
import time #подключаем время
import random #подключаем рандом
import os
import webbrowser

pygame.init()
pygame.mixer.init()

ICON_DIR = os.path.dirname(__file__) # Полный путь к каталогу с файлами

#интро
game_intro1 = pygame.image.load('%sintro/DenGameStudio.png' % ICON_DIR)

#бомба
draw_bomb = pygame.image.load('%ssprites/Bomb/Bomb.png' % ICON_DIR)

#виды змей
snakeHead01 = pygame.image.load('%ssprites/SnakeHeads/snakehead.png' % ICON_DIR)
snakeHead02 = pygame.image.load('%ssprites/SnakeHeads/snakehead2.png' % ICON_DIR)
snakeHead03 = pygame.image.load('%ssprites/SnakeHeads/snakehead3.png' % ICON_DIR)

line01 = pygame.image.load('%ssprites/SnakeBodies/line1.png' % ICON_DIR)
line02 = pygame.image.load('%ssprites/SnakeBodies/line2.png' % ICON_DIR)
line03 = pygame.image.load('%ssprites/SnakeBodies/line3.png' % ICON_DIR)

appleimg = pygame.image.load("%ssprites/Apples/Apple.png" % ICON_DIR)

#виды голов для змеи
shop_snake_head0 = pygame.image.load('%ssprites/SnakeHeads/snakehead0_shop.png' % ICON_DIR)
shop_snake_head1 = pygame.image.load('%ssprites/SnakeHeads/snakehead1_shop.png' % ICON_DIR)
shop_snake_head2 = pygame.image.load('%ssprites/SnakeHeads/snakehead2_shop.png' % ICON_DIR)
shop_snake_head3 = pygame.image.load('%ssprites/SnakeHeads/snakehead3_shop.png' % ICON_DIR)

#иды тела для змеи
shop_snake_body0 = pygame.image.load('%ssprites/SnakeBodies/body0_shop.png' % ICON_DIR)
shop_snake_body1 = pygame.image.load('%ssprites/SnakeBodies/body1_shop.png' % ICON_DIR)
shop_snake_body2 = pygame.image.load('%ssprites/SnakeBodies/body2_shop.png' % ICON_DIR)
shop_snake_body3 = pygame.image.load('%ssprites/SnakeBodies/body3_shop.png' % ICON_DIR)

#звуки/музыка
button_sound = pygame.mixer.Sound('%sSounds/button.wav' % ICON_DIR)
game_music1 = pygame.mixer.music.load('%sSounds/Cramoki-Take-U-There.mp3' % ICON_DIR)
game_music2 = pygame.mixer.music.load('%sSounds/Harmony-Ikson.mp3' % ICON_DIR)

#загрузка кнопок
button_settings = pygame.image.load('%sbuttons/main_buttons/settings.png' % ICON_DIR)
button_play = pygame.image.load('%sbuttons/main_buttons/button_play.png' % ICON_DIR)
button2_info = pygame.image.load('%sbuttons/buttons2/buttons2_info.png' % ICON_DIR)
button_shop = pygame.image.load('%sbuttons/main_buttons/shop.png' % ICON_DIR)
button_music_n = pygame.image.load('%sbuttons/main_buttons/music_n.png' % ICON_DIR)
button_music_y = pygame.image.load('%sbuttons/main_buttons/music_y.png' % ICON_DIR)
button2_paused = pygame.image.load('%sbuttons/buttons2/buttons2_paused.png' % ICON_DIR)
button2_menu = pygame.image.load('%sbuttons/buttons2/buttons2_menu.png' % ICON_DIR)

#цвета для игры
white = (255,255,255) #белый
black = (0,0,0) #черный
red = (255,0,0) #красный
green = (0,155,0) #зеленый
blue = (56, 76, 224) #синий
orenge = (237, 170, 36) #оранжевый
yellow = (227, 227, 32) #желтый
SnakeColor = green #цвет змеи
SnakeColor_shop = "Зеленый"

SnakeHead_shop_m = "Обычная голова"
SnakeHead_shop = None

SnakeBody_shop_m = "Обычное тело"
SnakeLine_shop = None

display_width = 900 #дисплей в ширину
display_height  = 700 #дисплей с высоту

#дисплей
gameDisplay = pygame.display.set_mode((display_width,display_height))

#верхняя надпись
pygame.display.set_caption('Змейка')

#время
clock = pygame.time.Clock()

#ширина и высота яблока
AppleThickness = 32

#ширина и высота змеи
block_size = 20

#скорость(FPS)
FPS = 16

#живучесть
life = True

#деньги
money = 0

#музыка/звуки
game_music = True
game_sounds = True
music_volume = 0.6

#для миссий
EatApple = 0
DiedNumber = 0
NewGame = 0
bomb_mission = 0
mission_color = 0

#виды текстов
microfont = pygame.font.SysFont("comicsansms", 20)
#малый
smallfont = pygame.font.SysFont("comicsansms", 30)
#средний
medfont = pygame.font.SysFont("comicsansms", 40)
#большой
largefont = pygame.font.SysFont("comicsansms", 64)

def game_bomb():
    bomb_x = round(random.randrange(0, display_width-30))
    bomb_y = round(random.randrange(0, display_height-30))
    return bomb_x, bomb_y

def bomb_boom():
    global bomb_mission
    bomb_mission += 1

volume_mus = ""
def music_volume_p():
    global volume_mus
    global music_volume
    if music_volume == 0.0:
        volume_mus = '0'
    if music_volume == 0.1:
        volume_mus = '10'
    if music_volume == 0.2:
        volume_mus = '20'
    if music_volume == 0.3:
        volume_mus = '30'
    if music_volume == 0.4:
        volume_mus = '40'
    if music_volume == 0.5:
        volume_mus = '50'
    if music_volume == 0.6:
        volume_mus = '60'
    if music_volume == 0.7:
        volume_mus = '70'
    if music_volume == 0.8:
        volume_mus = '80'
    if music_volume == 0.9:
        volume_mus = '90'
    if music_volume == 1.0:
        volume_mus = '100'

    text = medfont.render(volume_mus, True, black)
    gameDisplay.blit(text, [490, 120])

pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(music_volume)

def button_sound_play():
    global game_sounds
    if game_sounds == True:
        pygame.mixer.Sound.play(button_sound)
        pygame.time.delay(300)
    elif game_sounds == False:
        pass

def introFunc():
    intro = True
    while intro:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro = False
                    game_intro()

        if 0 < mouse[0] < 0 + display_width:
            if 0 < mouse[1] < 0 + display_height:
                if click[0] == 1:
                    intro = False
                    game_intro()

        gameDisplay.blit(game_intro1, (-180, -2))
        message_to_screen("Нажмите SPACE для продолжения",
                        yellow,
                        300)

        message_to_screen("v=0.1",
                        (230, 215, 185),
                        -340,
                        -420,
                        size="micro")

        pygame.display.update()
        clock.tick(15)

#класс кнопка
class Button:
    #главная функция
    def __init__(self, width, height, inactive_color=None, active_color=None):
        self.width = width
        self.height = height
        self.inactive_color = inactive_color
        self.active_color = active_color

    #фунция для выбора головы 1
    def SnakeHead0(self, x, y, message, message_color, head_shop, picture_head, head_mes, head_money=None):
        global SviewHead
        global SnakeHead_shop_m
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        gameDisplay.blit(picture_head, (x+330, y-5))

        headTF = " Имеется"
        if x < mouse[0] < x + self.width:
            if y < mouse[1] < y + self.height:
                pygame.draw.rect(gameDisplay, self.active_color, (x, y-5, self.width, self.height))
                gameDisplay.blit(picture_head, (x+330, y-5))
                if click[0] == 1:
                    button_sound_play()
                    SnakeHead_shop_m = head_mes
                    SviewHead = True

        else:
            pygame.draw.rect(gameDisplay, self.inactive_color,(x, y-5, self.width, self.height))
            gameDisplay.blit(picture_head, (x+330, y-5))

        text_button = smallfont.render(message+"          "+str(headTF), True, message_color)
        gameDisplay.blit(text_button, [x+3, y-3])

    #фунция для выбора головы 2
    def SnakeHead1(self, x, y, message, message_color, head_shop, picture_head, head_mes, head_money=None):
        global money
        global Head1_shop
        global SnakeHead_shop
        global SviewHead
        global SnakeHead_shop_m
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        gameDisplay.blit(picture_head, (x+330, y-5))

        if head_shop == False:
            headTF = " "+str(head_money)+" монет"
        elif head_shop == True:
            headTF = " Имеется"
        if x < mouse[0] < x + self.width:
            if y < mouse[1] < y + self.height:
                pygame.draw.rect(gameDisplay, self.active_color, (x, y-5, self.width, self.height))
                gameDisplay.blit(picture_head, (x+330, y-5))
                if click[0] == 1:
                    button_sound_play()

                    if head_shop == False:
                        if money >= head_money:
                            money -= head_money
                            Head1_shop = True
                            SviewHead = False
                            SnakeHead_shop = snakeHead01
                            SnakeHead_shop_m = head_mes
                        elif money < head_money:
                            money = money
                            SnakeHead_shop_m = SnakeHead_shop_m
                            SnakeHead_shop = SnakeHead_shop
                    elif head_shop == True:
                        SnakeHead_shop = snakeHead01
                        SnakeHead_shop_m = head_mes
                        SviewHead = False

        else:
            pygame.draw.rect(gameDisplay, self.inactive_color,(x, y-5, self.width, self.height))
            gameDisplay.blit(picture_head, (x+330, y-5))

        text_button = smallfont.render(message+"             "+str(headTF), True, message_color)
        gameDisplay.blit(text_button, [x+3, y-3])

    #фунция для выбора головы 3
    def SnakeHead2(self, x, y, message, message_color, head_shop, picture_head, head_mes, head_money=None):
        global money
        global Head2_shop
        global SnakeHead_shop
        global SviewHead
        global SnakeHead_shop_m
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        gameDisplay.blit(picture_head, (x+330, y-5))

        if head_shop == False:
            headTF = " "+str(head_money)+" монет"
        elif head_shop == True:
            headTF = " Имеется"
        if x < mouse[0] < x + self.width:
            if y < mouse[1] < y + self.height:
                pygame.draw.rect(gameDisplay, self.active_color, (x, y-5, self.width, self.height))
                gameDisplay.blit(picture_head, (x+330, y-5))
                if click[0] == 1:
                    button_sound_play()

                    if head_shop == False:
                        if money >= head_money:
                            money -= head_money
                            Head2_shop = True
                            SviewHead = False
                            SnakeHead_shop = snakeHead02
                            SnakeHead_shop_m = head_mes
                        elif money < head_money:
                            money = money
                            SnakeHead_shop_m = SnakeHead_shop_m
                            SnakeHead_shop = SnakeHead_shop
                    elif head_shop == True:
                        SnakeHead_shop = snakeHead02
                        SnakeHead_shop_m = head_mes
                        SviewHead = False

        else:
            pygame.draw.rect(gameDisplay, self.inactive_color,(x, y-5, self.width, self.height))
            gameDisplay.blit(picture_head, (x+330, y-5))

        text_button = smallfont.render(message+"             "+str(headTF), True, message_color)
        gameDisplay.blit(text_button, [x+3, y-3])

    #фунция для выбора головы 4
    def SnakeHead3(self, x, y, message, message_color, head_shop, picture_head, head_mes, head_money=None):
        global money
        global Head3_shop
        global SnakeHead_shop
        global SviewHead
        global SnakeHead_shop_m
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        gameDisplay.blit(picture_head, (x+330, y-5))

        if head_shop == False:
            headTF = " "+str(head_money)+" монет"
        elif head_shop == True:
            headTF = " Имеется"
        if x < mouse[0] < x + self.width:
            if y < mouse[1] < y + self.height:
                pygame.draw.rect(gameDisplay, self.active_color, (x, y-5, self.width, self.height))
                gameDisplay.blit(picture_head, (x+330, y-5))
                if click[0] == 1:
                    button_sound_play()

                    if head_shop == False:
                        if money >= head_money:
                            money -= head_money
                            Head3_shop = True
                            SviewHead = False
                            SnakeHead_shop = snakeHead03
                            SnakeHead_shop_m = head_mes
                        elif money < head_money:
                            money = money
                            SnakeHead_shop_m = SnakeHead_shop_m
                            SnakeHead_shop = SnakeHead_shop
                    elif head_shop == True:
                        SnakeHead_shop = snakeHead03
                        SnakeHead_shop_m = head_mes
                        SviewHead = False

        else:
            pygame.draw.rect(gameDisplay, self.inactive_color,(x, y-5, self.width, self.height))
            gameDisplay.blit(picture_head, (x+330, y-5))

        text_button = smallfont.render(message+"             "+str(headTF), True, message_color)
        gameDisplay.blit(text_button, [x+3, y-3])

    #фунция для выбора тела 1
    def SnakeBody0(self, x, y, message, message_color, body_shop, picture_body, body_mes):
        global SnakeBody_shop_m
        global SviewBody
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        gameDisplay.blit(picture_body, (x+330, y-5))

        bodyTF = " Имеется"
        if x < mouse[0] < x + self.width:
            if y < mouse[1] < y + self.height:
                pygame.draw.rect(gameDisplay, self.active_color, (x, y-5, self.width, self.height))
                gameDisplay.blit(picture_body, (x+330, y-5))
                if click[0] == 1:
                    button_sound_play()

                    SviewBody = True
                    SnakeBody_shop_m = "Обычное тело"

        else:
            pygame.draw.rect(gameDisplay, self.inactive_color,(x, y-5, self.width, self.height))
            gameDisplay.blit(picture_body, (x+330, y-5))

        text_button = smallfont.render(message+"           "+bodyTF, True, message_color)
        gameDisplay.blit(text_button, [x+3, y-3])

    #фунция для выбора тела 2
    def SnakeBody1(self, x, y, message, message_color, body_shop, picture_body, body_mes, body_money=None):
        global money
        global Body1_shop
        global SnakeBody_shop_m
        global SnakeLine_shop
        global SviewBody
        global line01
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        gameDisplay.blit(picture_body, (x+330, y-5))

        if body_shop == False:
            bodyTF = " "+str(body_money)+" монет"
        elif body_shop == True:
            bodyTF = " Имеется"
        if x < mouse[0] < x + self.width:
            if y < mouse[1] < y + self.height:
                pygame.draw.rect(gameDisplay, self.active_color, (x, y-5, self.width, self.height))
                gameDisplay.blit(picture_body, (x+330, y-5))
                if click[0] == 1:
                    button_sound_play()

                    if body_shop == False:
                        if money >= body_money:
                            money -= body_money
                            Body1_shop = True
                            SviewBody = False
                            SnakeLine_shop = line01
                            SnakeBody_shop_m = body_mes
                        elif money < body_money:
                            money = money
                            SnakeBody_shop_m = SnakeBody_shop_m
                            SnakeLine_shop = SnakeLine_shop
                    elif body_shop == True:
                        SnakeLine_shop = line01
                        SnakeBody_shop_m = body_mes
                        SviewBody = False

        else:
            pygame.draw.rect(gameDisplay, self.inactive_color,(x, y-5, self.width, self.height))
            gameDisplay.blit(picture_body, (x+330, y-5))

        text_button = smallfont.render(message+"        "+bodyTF, True, message_color)
        gameDisplay.blit(text_button, [x+3, y-3])

    #фунция для выбора тела 3
    def SnakeBody2(self, x, y, message, message_color, body_shop, picture_body, body_mes, body_money=None):
        global money
        global Body2_shop
        global SnakeBody_shop_m
        global SnakeLine_shop
        global SviewBody
        global line02
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        gameDisplay.blit(picture_body, (x+330, y-5))

        if body_shop == False:
            bodyTF = " "+str(body_money)+" монет"
        elif body_shop == True:
            bodyTF = " Имеется"
        if x < mouse[0] < x + self.width:
            if y < mouse[1] < y + self.height:
                pygame.draw.rect(gameDisplay, self.active_color, (x, y-5, self.width, self.height))
                gameDisplay.blit(picture_body, (x+330, y-5))
                if click[0] == 1:
                    button_sound_play()

                    if body_shop == False:
                        if money >= body_money:
                            money -= body_money
                            Body2_shop = True
                            SviewBody = False
                            SnakeLine_shop = line02
                            SnakeBody_shop_m = body_mes
                        elif money < body_money:
                            money = money
                            SnakeBody_shop_m = SnakeBody_shop_m
                            SnakeLine_shop = SnakeLine_shop
                    elif body_shop == True:
                        SnakeLine_shop = line02
                        SnakeBody_shop_m = body_mes
                        SviewBody = False

        else:
            pygame.draw.rect(gameDisplay, self.inactive_color,(x, y-5, self.width, self.height))
            gameDisplay.blit(picture_body, (x+330, y-5))

        text_button = smallfont.render(message+"             "+bodyTF, True, message_color)
        gameDisplay.blit(text_button, [x+3, y-3])

    #фунция для выбора тела 4
    def SnakeBody3(self, x, y, message, message_color, body_shop, picture_body, body_mes, body_money=None):
        global money
        global Body3_shop
        global SnakeBody_shop_m
        global SnakeLine_shop
        global SviewBody
        global line02
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        gameDisplay.blit(picture_body, (x+330, y-5))

        if body_shop == False:
            bodyTF = " "+str(body_money)+" монет"
        elif body_shop == True:
            bodyTF = " Имеется"
        if x < mouse[0] < x + self.width:
            if y < mouse[1] < y + self.height:
                pygame.draw.rect(gameDisplay, self.active_color, (x, y-5, self.width, self.height))
                gameDisplay.blit(picture_body, (x+330, y-5))
                if click[0] == 1:
                    button_sound_play()

                    if body_shop == False:
                        if money >= body_money:
                            money -= body_money
                            Body3_shop = True
                            SviewBody = False
                            SnakeLine_shop = line03
                            SnakeBody_shop_m = body_mes
                        elif money < body_money:
                            money = money
                            SnakeBody_shop_m = SnakeBody_shop_m
                            SnakeLine_shop = SnakeLine_shop
                    elif body_shop == True:
                        SnakeLine_shop = line03
                        SnakeBody_shop_m = body_mes
                        SviewBody = False

        else:
            pygame.draw.rect(gameDisplay, self.inactive_color,(x, y-5, self.width, self.height))
            gameDisplay.blit(picture_body, (x+330, y-5))

        text_button = smallfont.render(message+"          "+bodyTF, True, message_color)
        gameDisplay.blit(text_button, [x+3, y-3])

    #громкость музыки
    def draw_button_volume(self, x, y, message=None, message_color=None):
        global music_volume
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        text_button = medfont.render(message, True, message_color)
        gameDisplay.blit(text_button, [x, y-10])

        if x < mouse[0] < x + self.width:
            if y < mouse[1] < y + self.height:
                text_button = medfont.render(message, True, message_color)
                gameDisplay.blit(text_button, [x, y-10])
                if click[0] == 1:
                    if message == "-":
                        if music_volume == 1.0:
                            music_volume = 0.9
                        elif music_volume == 0.9:
                            music_volume = 0.8
                        elif music_volume == 0.8:
                            music_volume = 0.7
                        elif music_volume == 0.7:
                            music_volume = 0.6
                        elif music_volume == 0.6:
                            music_volume = 0.5
                        elif music_volume == 0.5:
                            music_volume = 0.4
                        elif music_volume == 0.4:
                            music_volume = 0.3
                        elif music_volume == 0.3:
                            music_volume = 0.2
                        elif music_volume == 0.2:
                            music_volume = 0.1
                        elif music_volume == 0.1:
                            music_volume = 0.0
                        elif music_volume == 0.0:
                            pass
                        pygame.mixer.music.set_volume(music_volume)

                    elif message == "+":
                        if music_volume == 0.0:
                            music_volume = 0.1
                        elif music_volume == 0.1:
                            music_volume = 0.2
                        elif music_volume == 0.2:
                            music_volume = 0.3
                        elif music_volume == 0.3:
                            music_volume = 0.4
                        elif music_volume == 0.4:
                            music_volume = 0.5
                        elif music_volume == 0.5:
                            music_volume = 0.6
                        elif music_volume == 0.6:
                            music_volume = 0.7
                        elif music_volume == 0.7:
                            music_volume = 0.8
                        elif music_volume == 0.8:
                            music_volume = 0.9
                        elif music_volume == 0.9:
                            music_volume = 1.0
                        elif music_volume == 1.0:
                            pass
                        pygame.mixer.music.set_volume(music_volume)

        else:
            text_button = medfont.render(message, True, message_color)
            gameDisplay.blit(text_button, [x, y-10])

    def draw_button_music(self, picture, x, y, sound=None):
        global game_music
        global game_sounds
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        gameDisplay.blit(picture, (x, y))

        if x < mouse[0] < x + self.width:
            if y < mouse[1] < y + self.height:
                gameDisplay.blit(picture, (x, y))
                if click[0] == 1:
                    if sound == "game_music":
                        if game_music == True:
                            game_music = False
                            pygame.mixer.music.pause()
                        elif game_music == False:
                            game_music = True
                            pygame.mixer.music.unpause()

                    elif sound == "game_sounds":
                        if game_sounds == True:
                            game_sounds = False
                        elif game_sounds == False:
                            game_sounds = True

        else:
            gameDisplay.blit(picture, (x, y))

    #функция для обычной кнопки
    def draw(self, message, message_color, x, y, active_func=None, action=None, Msize="small"):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        pygame.draw.rect(gameDisplay, self.inactive_color,(x, y, self.width, self.height))

        if x < mouse[0] < x + self.width:
            if y < mouse[1] < y + self.height:
                pygame.draw.rect(gameDisplay, self.active_color, (x, y, self.width, self.height))

                if click[0] == 1:
                    button_sound_play()

                    if action is not None:
                        active_func = False
                        action()

        else:
            pygame.draw.rect(gameDisplay, self.inactive_color,(x, y, self.width, self.height))

        if Msize == "small":
            text_button = smallfont.render(message, True, message_color)
            gameDisplay.blit(text_button, [x + 5, y])
        elif Msize == "medium":
            text_button = medfont.render(message, True, message_color)
            gameDisplay.blit(text_button, [x + 5, y])
        elif Msize == "large":
            text_button = largefont.render(message, True, message_color)
            gameDisplay.blit(text_button, [x + 5, y])

    #функция для кнопки со значком
    def draw_picture(self, picture, x, y, active_func = None, action = None, pausel="True", WebPage=None, start=False):
        global paused
        global NewGame
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        gameDisplay.blit(picture, (x, y))

        if x < mouse[0] < x + self.width:
            if y < mouse[1] < y + self.height:
                gameDisplay.blit(picture, (x, y))
                if click[0] == 1:
                    button_sound_play()
                    if pausel == "True":
                        if start == True:
                            NewGame += 1
                            start = False
                        if active_func != None:
                            active_func = False

                        if action != None:
                            action()

                        if action == pause:
                            paused = True
                            pause()

                        if WebPage != None:
                            url_group = WebPage
                            webbrowser.open(url_group)

                    elif pausel == "False":
                        paused = False

        else:
            gameDisplay.blit(picture, (x, y))

    #функция для кнопки миссий
    def draw_mission(self, message, message_color, x, y, money_col=None, null=None):
        global money
        global EatApple
        global DiedNumber
        global NewGame
        global mission_color
        global bomb_mission
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.width:
            if y < mouse[1] < y + self.height:
                pygame.draw.rect(gameDisplay, self.active_color, (x, y, self.width, self.height))

                if click[0] == 1:
                    if money_col is not None:
                        money += money_col

                    if null != None:
                        if null == EatApple:
                            EatApple = 0

                        elif null == DiedNumber:
                            DiedNumber = 0

                        elif null == NewGame:
                            NewGame = 0

                        elif null == bomb_mission:
                            bomb_mission = 0

                        elif null == mission_color:
                            mission_color = 0

                    else:
                        pass


        else:
            pygame.draw.rect(gameDisplay, self.inactive_color,(x, y, self.width, self.height))

        text_button = smallfont.render(message, True, message_color)
        gameDisplay.blit(text_button, [x + 5, y])

    #функции выбора цвета змеи
    def draw_color_green(self, message, message_color, x, y, color_shop, color, colorMes, color_money=None):
        global SnakeColor_shop
        global SnakeColor
        global Sview
        global money
        global green_shop

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        pygame.draw.rect(gameDisplay, self.inactive_color,(x, y, self.width, self.height))

        ColorTF = ""
        if color == False:
            ColorTF = str(color_money) + " монет"
        elif color == True:
            ColorTF = "Имеется"

        if x < mouse[0] < x + self.width:
            if y < mouse[1] < y + self.height:
                pygame.draw.rect(gameDisplay, self.active_color, (x, y, self.width, self.height))

                if click[0] == 1:
                    button_sound_play()

                    if color == False:
                        if money >= color_money:
                            money -= color_money
                            green_shop = True
                            SnakeColor = color_shop
                            SnakeColor_shop = colorMes
                        elif money < color_money:
                            money = money
                            SnakeColor = SnakeColor
                            SnakeColor_shop = SnakeColor_shop
                    elif color == True:
                        SnakeColor = color_shop
                        Sview = True
                        SnakeColor_shop = colorMes

        else:
            pygame.draw.rect(gameDisplay, self.inactive_color,(x, y, self.width, self.height))

        text_button = smallfont.render(message+ColorTF, True, message_color)
        gameDisplay.blit(text_button, [x + 3, y-3])

    def draw_color_black(self, message, message_color, x, y, color_shop, color, colorMes, color_money=None):
        global SnakeColor_shop
        global SnakeColor
        global Sview
        global money
        global black_shop
        global mis_c5_a1_1
        global mission_color

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        pygame.draw.rect(gameDisplay, self.inactive_color,(x, y, self.width, self.height))

        ColorTF = ""
        if color == False:
            ColorTF = str(color_money) + " монет"
        elif color == True:
            ColorTF = "Имеется"

        if x < mouse[0] < x + self.width:
            if y < mouse[1] < y + self.height:
                pygame.draw.rect(gameDisplay, self.active_color, (x, y, self.width, self.height))

                if click[0] == 1:
                    button_sound_play()

                    if color == False:
                        if money >= color_money:
                            money -= color_money
                            black_shop = True
                            SnakeColor = color_shop
                            SnakeColor_shop = colorMes
                            mission_color = 1
                        elif money < color_money:
                            money = money
                            SnakeColor = SnakeColor
                            SnakeColor_shop = SnakeColor_shop
                    elif color == True:
                        SnakeColor = color_shop
                        Sview = True
                        SnakeColor_shop = colorMes

        else:
            pygame.draw.rect(gameDisplay, self.inactive_color,(x, y, self.width, self.height))

        text_button = smallfont.render(message+ColorTF, True, message_color)
        gameDisplay.blit(text_button, [x + 3, y-3])

    def draw_color_red(self, message, message_color, x, y, color_shop, color, colorMes, color_money=None):
        global SnakeColor_shop
        global SnakeColor
        global Sview
        global money
        global red_shop
        global mis_c5_a2_2
        global mission_color

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        pygame.draw.rect(gameDisplay, self.inactive_color,(x, y, self.width, self.height))

        ColorTF = ""
        if color == False:
            ColorTF = str(color_money) + " монет"
        elif color == True:
            ColorTF = "Имеется"

        if x < mouse[0] < x + self.width:
            if y < mouse[1] < y + self.height:
                pygame.draw.rect(gameDisplay, self.active_color, (x, y, self.width, self.height))

                if click[0] == 1:
                    button_sound_play()

                    if color == False:
                        if money >= color_money:
                            money -= color_money
                            red_shop = True
                            SnakeColor = color_shop
                            SnakeColor_shop = colorMes
                            mission_color = 2
                        elif money < color_money:
                            money = money
                            SnakeColor = SnakeColor
                            SnakeColor_shop = SnakeColor_shop
                    elif color == True:
                        SnakeColor = color_shop
                        Sview = True
                        SnakeColor_shop = colorMes

        else:
            pygame.draw.rect(gameDisplay, self.inactive_color,(x, y, self.width, self.height))

        text_button = smallfont.render(message+ColorTF, True, message_color)
        gameDisplay.blit(text_button, [x + 3, y-3])

    def draw_color_blue(self, message, message_color, x, y, color_shop, color, colorMes, color_money=None):
        global SnakeColor_shop
        global SnakeColor
        global Sview
        global money
        global blue_shop
        global mis_c5_a3_3
        global mission_color

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        pygame.draw.rect(gameDisplay, self.inactive_color,(x, y, self.width, self.height))

        ColorTF = ""
        if color == False:
            ColorTF = str(color_money) + " монет"
        elif color == True:
            ColorTF = "Имеется"

        if x < mouse[0] < x + self.width:
            if y < mouse[1] < y + self.height:
                pygame.draw.rect(gameDisplay, self.active_color, (x, y, self.width, self.height))

                if click[0] == 1:
                    button_sound_play()

                    if color == False:
                        if money >= color_money:
                            money -= color_money
                            blue_shop = True
                            SnakeColor = color_shop
                            SnakeColor_shop = colorMes
                            mission_color = 3
                        elif money < color_money:
                            money = money
                            SnakeColor = SnakeColor
                            SnakeColor_shop = SnakeColor_shop
                    elif color == True:
                        SnakeColor = color_shop
                        Sview = True
                        SnakeColor_shop = colorMes

        else:
            pygame.draw.rect(gameDisplay, self.inactive_color,(x, y, self.width, self.height))

        text_button = smallfont.render(message+ColorTF, True, message_color)
        gameDisplay.blit(text_button, [x + 3, y-3])

    def draw_color_orenge(self, message, message_color, x, y, color_shop, color, colorMes, color_money=None):
        global SnakeColor_shop
        global SnakeColor
        global Sview
        global money
        global orenge_shop
        global mis_c5_a4_4
        global mission_color

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        pygame.draw.rect(gameDisplay, self.inactive_color,(x, y, self.width, self.height))

        ColorTF = ""
        if color == False:
            ColorTF = str(color_money) + " монет"
        elif color == True:
            ColorTF = "Имеется"

        if x < mouse[0] < x + self.width:
            if y < mouse[1] < y + self.height:
                pygame.draw.rect(gameDisplay, self.active_color, (x, y, self.width, self.height))

                if click[0] == 1:
                    button_sound_play()

                    if color == False:
                        if money >= color_money:
                            money -= color_money
                            orenge_shop = True
                            SnakeColor = color_shop
                            SnakeColor_shop = colorMes
                            mission_color = 4
                        elif money < color_money:
                            money = money
                            SnakeColor = SnakeColor
                            SnakeColor_shop = SnakeColor_shop
                    elif color == True:
                        SnakeColor = color_shop
                        Sview = True
                        SnakeColor_shop = colorMes

        else:
            pygame.draw.rect(gameDisplay, self.inactive_color,(x, y, self.width, self.height))

        text_button = smallfont.render(message+ColorTF, True, message_color)
        gameDisplay.blit(text_button, [x + 3, y-3])

    def draw_color_yellow(self, message, message_color, x, y, color_shop, color, colorMes, color_money=None):
        global SnakeColor_shop
        global SnakeColor
        global Sview
        global money
        global yellow_shop
        global mis_c5_a5_5
        global mission_color

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        pygame.draw.rect(gameDisplay, self.inactive_color,(x, y, self.width, self.height))

        ColorTF = ""
        if color == False:
            ColorTF = str(color_money) + " монет"
        elif color == True:
            ColorTF = "Имеется"

        if x < mouse[0] < x + self.width:
            if y < mouse[1] < y + self.height:
                pygame.draw.rect(gameDisplay, self.active_color, (x, y, self.width, self.height))

                if click[0] == 1:
                    button_sound_play()

                    if color == False:
                        if money >= color_money:
                            money -= color_money
                            yellow_shop = True
                            SnakeColor = color_shop
                            SnakeColor_shop = colorMes
                            mission_color = 5
                        elif money < color_money:
                            money = money
                            SnakeColor = SnakeColor
                            SnakeColor_shop = SnakeColor_shop
                    elif color == True:
                        SnakeColor = color_shop
                        Sview = True
                        SnakeColor_shop = colorMes

        else:
            pygame.draw.rect(gameDisplay, self.inactive_color,(x, y, self.width, self.height))

        text_button = smallfont.render(message+ColorTF, True, message_color)
        gameDisplay.blit(text_button, [x + 3, y-3])

#консоль
def game_console():
    global EatApple
    global DiedNumber
    global NewGame
    global bomb_mission
    global money
    global FPS
    global life
    task = ""
    console = True
    while console:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # все использующиеся символы
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    task+=chr(event.key)
                if event.key == pygame.K_b:
                    task+=chr(event.key)
                if event.key == pygame.K_c:
                    task+=chr(event.key)
                if event.key == pygame.K_d:
                    task+=chr(event.key)
                if event.key == pygame.K_e:
                    task+=chr(event.key)
                if event.key == pygame.K_f:
                    task+=chr(event.key)
                if event.key == pygame.K_g:
                    task+=chr(event.key)
                if event.key == pygame.K_h:
                    task+=chr(event.key)
                if event.key == pygame.K_i:
                   task+=chr(event.key)
                if event.key == pygame.K_j:
                    task+=chr(event.key)
                if event.key == pygame.K_k:
                    task+=chr(event.key)
                if event.key == pygame.K_l:
                    task+=chr(event.key)
                if event.key == pygame.K_m:
                    task+=chr(event.key)
                if event.key == pygame.K_n:
                    task+=chr(event.key)
                if event.key == pygame.K_o:
                    task+=chr(event.key)
                if event.key == pygame.K_p:
                    task+=chr(event.key)
                if event.key == pygame.K_q:
                    task+=chr(event.key)
                if event.key == pygame.K_r:
                    task+=chr(event.key)
                if event.key == pygame.K_s:
                    task+=chr(event.key)
                if event.key == pygame.K_t:
                    task+=chr(event.key)
                if event.key == pygame.K_u:
                    task+=chr(event.key)
                if event.key == pygame.K_v:
                    task+=chr(event.key)
                if event.key == pygame.K_w:
                    task+=chr(event.key)
                if event.key == pygame.K_x:
                    task+=chr(event.key)
                if event.key == pygame.K_y:
                    task+=chr(event.key)
                if event.key == pygame.K_z:
                    task+=chr(event.key)
                if event.key == pygame.K_1:
                    task+=chr(event.key)
                if event.key == pygame.K_2:
                    task+=chr(event.key)
                if event.key == pygame.K_3:
                    task+=chr(event.key)
                if event.key == pygame.K_4:
                    task+=chr(event.key)
                if event.key == pygame.K_5:
                    task+=chr(event.key)
                if event.key == pygame.K_6:
                    task+=chr(event.key)
                if event.key == pygame.K_7:
                    task+=chr(event.key)
                if event.key == pygame.K_8:
                    task+=chr(event.key)
                if event.key == pygame.K_9:
                    task+=chr(event.key)
                if event.key == pygame.K_0:
                    task+=chr(event.key)
                if event.key == pygame.K_SPACE:
                    task+=chr(event.key)
                if event.key == pygame.K_BACKSPACE:
                    task = ""
                if event.key == pygame.K_RETURN:

                    if task[:4] == 'bomb':
                        if task[5:9] == 'plus':
                            bomb_mission += int(task[10:])
                            task = 'bomb = ' + str(bomb_mission)
                        elif task[5:8] == 'min':
                            bomb_mission -= int(task[9:])
                            task = 'bomb = ' + str(bomb_mission)

                    if task[:5] == 'apple':
                        if task[6:10] == 'plus':
                            EatApple += int(task[11:])
                            task = 'apple = ' + str(EatApple)
                        if task[6:9] == 'min':
                            EatApple -= int(task[11:])
                            task = 'apple = ' + str(EatApple)

                    if task[:4] == 'game':
                        if task[5:9] == 'plus':
                            NewGame += int(task[10:])
                            task = 'game = ' + str(NewGame)
                        if task[5:8] == 'min':
                            NewGame -= int(task[9:])
                            task = 'game = ' + str(NewGame)

                    if task[:4] == 'died':
                        if task[5:9] == 'plus':
                            DiedNumber += int(task[10:])
                            task = 'died = ' + str(DiedNumber)
                        if task[5:8] == 'min':
                            DiedNumber -= int(task[9:])
                            task = 'died = ' + str(DiedNumber)

                    if task[:5] == 'money':
                        if task[6:10] == 'plus':
                            money += int(task[11:])
                            task = 'money = ' + str(money)
                        if task[6:9] == 'min':
                            money -= int(task[10:])
                            task = 'money = ' + str(money)
                        if task[6:8] == 'ex':
                            money = int(task[9:])
                            task = 'money = ' + str(money)
                        if task[6:10] == 'null':
                            money = 0
                            task = 'money = ' + str(money)

                    if task[:5] == 'speed':
                        if task[6:10] == 'plus':
                            FPS += int(task[11:])
                            task = 'speed = ' + str(FPS)
                        if task[6:9] == 'min':
                            FPS -= int(task[10:])
                            task = 'speed = ' + str(FPS)

                    if task[:4] == 'life':
                        if task[5:10] == 'true':
                            life = True
                            task = 'life true - OK!'
                        if task[5:11] == 'false':
                            life = False
                            task = 'life false - OK!'


                    if task == 'money':
                        task = 'money = ' + str(money)

                    if task == 'speed':
                        task = 'speed = ' + str(FPS)

                    if task == 'apple':
                        task = 'apple = ' + str(EatApple)

                    if task == 'died':
                        task = 'died = ' + str(DiedNumber)

                    if task == 'life':
                        if life == True:
                            task = 'life = true'
                        elif life == False:
                            task = 'life = false'

                    if task == 'exit':
                        console = False
                        game_intro()

            gameDisplay.fill(black)
            message_to_screen("$$$Console$$$",
                              green,
                              -300,
                              -50)
            cons = smallfont.render("$ " + task + '|', True, green)
            gameDisplay.blit(cons, [30,150])

        pygame.display.update()
        clock.tick(15)

#счет в игре
def score(score):
    text = smallfont.render("Счет: "+str(score), True, black)
    gameDisplay.blit(text, [390,5])

def score_d(score):
    text = largefont.render("Счет: "+str(score), True, black)
    gameDisplay.blit(text, [350,200])

#функция паузы в игре
paused = True
def pause():
    global paused
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False

                if event.key == pygame.K_m:
                    paused = False
                    game_intro()

        #вывод на экран
        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay, (222, 144, 20), (0, 0, 900, 700), 20)

        message_to_screen("Пауза.",
                          red,
                          -300,
                          size="medium")

        #кнопка меню
        button = Button(155, 167, (10, 111, 220), (10, 100, 200))
        button.draw_picture(button2_menu,
                            11,
                            11,
                            None,
                            game_intro)

        #кнопка игры
        button = Button(150, 53)
        button.draw_picture(button_play,
                            670,
                            200,
                            paused,
                            gameLoop,
                            pausel='False')

        #missions
        pygame.draw.rect(gameDisplay, (239, 135, 1), (50, 100, 590, 500))
        pygame.draw.rect(gameDisplay, (181, 132, 30), (50, 100, 590, 500), 10)
        game_mission()

        pygame.display.update()
        clock.tick(5)

#создание яблок в игре
def randAppleGen():
	#рандом по иксу
    randAppleX = round(random.randrange(0, display_width-20-AppleThickness))
    #рандом по игрику
    randAppleY = round(random.randrange(0, display_height-20-AppleThickness))

    return randAppleX, randAppleY    

#вывод денег на экран
def money_shop():
    global money
    text = medfont.render("Деньги: "+str(money), True, orenge)
    gameDisplay.blit(text, [350,6])

#настройки в игре
joystick = "Стрелочки"
def settings_control():
    global joystick
    settings_control_f = True
    while settings_control_f:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                
                if event.key == pygame.K_1:
                    joystick = "W-S-A-D"
                if event.key == pygame.K_2:
                    joystick = "Стрелочки"
                
                if event.key == pygame.K_n:
                    settings_control_f = False
                    game_intro()
            
        gameDisplay.fill(white)
        button = Button(115, 45, white, (137, 178, 245))
        button.draw("/Menu/",
                    black,
                    5,
                    5,
                    settings_control_f,
                    game_intro)

        button = Button(155, 45, white, (137, 178, 245))
        button.draw("/Settings/",
                    black,
                    120,
                    5,
                    settings_control_f,
                    game_settings)

        message_to_screen("Настройки",
                          orenge,
                          -300,
                          size="medium")

        message_to_screen("Управление: " + joystick,
                           green,
                           -200,
                           size="medium")

        message_to_screen("Виды управлений:",
                          orenge,
                          -100)

        message_to_screen("1 - W-S-A-D(общее)",
                          blue,
                          -30)
        
        message_to_screen("2 - Стрелочки(для ПК)",
                          blue,
                          20)
        
        pygame.display.update()
        clock.tick(15)

def settings_sounds():
    settings_sounds_f = True
    while settings_sounds_f:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

                if event.key == pygame.K_n:
                    settings_sounds_f = False
                    game_intro()
            
        gameDisplay.fill(white)
        button = Button(115, 45, white, (137, 178, 245))
        button.draw("/Menu/",
                    black,
                    5,
                    5,
                    settings_sounds_f,
                    game_intro)

        button = Button(155, 45, white, (137, 178, 245))
        button.draw("/Settings/",
                    black,
                    120,
                    5,
                    settings_sounds_f,
                    game_settings)

        message_to_screen("Настройки",
                          orenge,
                          -300,
                          size="medium")

        text = medfont.render("Музыка: Music 1", True, green)
        gameDisplay.blit(text, [70,122])

        music_volume_p()

        button_plus = Button(50, 38)
        button_plus.draw_button_volume(460, 130, '-', blue)

        button_plus = Button(50, 38)
        button_plus.draw_button_volume(560, 130, '+', red)

        if game_sounds == True:
            text = medfont.render("Звуки: ВКЛ", True, green)
            gameDisplay.blit(text, [70,200])
            button_n = Button(35, 35)
            button_n.draw_button_music(button_music_y, 400, 210, "game_sounds")
        elif game_sounds == False:
            text = medfont.render("Звуки: ВЫКЛ", True, green)
            gameDisplay.blit(text, [70,200])
            button_n = Button(35, 35)
            button_n.draw_button_music(button_music_n, 400, 210, "game_sounds")

        if game_music == True:
            button_n = Button(35, 35)
            button_n.draw_button_music(button_music_y, 400, 135, "game_music")
        elif game_music == False:
            button_n = Button(35, 35)
            button_n.draw_button_music(button_music_n, 400, 135, "game_music")
        
        pygame.display.update()
        clock.tick(15)

def game_settings():
    settings = True
    while settings:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
            	
                if event.key == pygame.K_n:
                    settings = False
                    game_intro()
            
        gameDisplay.fill(white)
        button = Button(115, 45, white, (137, 178, 245))
        button.draw("/Menu/",
                    black,
                    5,
                    5,
                    settings,
                    game_intro)

        message_to_screen("Настройки",
                          orenge,
                          -300,
                          size="medium")

        button = Button(250, 60, white, (200, 190, 180))
        button.draw("Управление", green, 130, 150, settings, settings_control, Msize="medium")

        button = Button(200, 60, white, (200, 190, 180))
        button.draw("Звуки", green, 130, 250, settings, settings_sounds, Msize="medium")
        
        pygame.display.update()
        clock.tick(15)

Head0_shop = True
Head1_shop = False
Head2_shop = False
Head3_shop = False
def SnakeViewHead():
    global shop_snake_head0
    global shop_snake_head1
    global shop_snake_head2
    global shop_snake_head3
    global SnakeHead_shop_m
    ViewHead = True
    while ViewHead:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    ViewHead = False
                    SnakeViewFunc()

        gameDisplay.fill(white)
        button = Button(115, 45, white, (137, 178, 245))
        button.draw("/Menu/",
                    black,
                    5,
                    5,
                    ViewHead,
                    game_intro)
        button = Button(115, 45, white, (137, 178, 245))
        button.draw("/Shop/",
                    black,
                    115,
                    5,
                    ViewHead,
                    game_shop)
        button = Button(115, 45, white, (137, 178, 245))
        button.draw("/View/",
                    black,
                    220,
                    5,
                    ViewHead,
                    SnakeViewFunc)
        money_shop()
        
        message_to_screen("Виды голов",
                        green,
                        -230,
                        size="medium")

        message_to_screen("Сейчас используется: "+SnakeHead_shop_m,
                        (133, 58, 252),
                        - 160)

        button_head0 = Button(565, 50, white, (200, 245, 150))
        button_head0.SnakeHead0(150, 250, "1 - Обычная голова => ", green, Head0_shop, shop_snake_head0, "Обычная голова")

        button_head1 = Button(565, 50, white, (200, 245, 150))
        button_head1.SnakeHead1(150, 320, "2 - Голова змеи 1 => ", green, Head1_shop, shop_snake_head1, "Голова змеи 1", head_money=50)

        button_head2 = Button(565, 50, white, (200, 245, 150))
        button_head2.SnakeHead2(150, 390, "3 - Голова змеи 2 => ", green, Head2_shop, shop_snake_head2, "Голова змеи 2", head_money=60)

        button_head3 = Button(565, 50, white, (200, 245, 150))
        button_head3.SnakeHead3(150, 460, "4 - Голова змеи 3 => ", green, Head3_shop, shop_snake_head3, "Голова змеи 3", head_money=70)


        pygame.display.update()
        clock.tick(15)

Body0_shop = True
Body1_shop = False
Body2_shop = False
Body3_shop = False
def SnakeViewBody():
    ViewBody = True
    while ViewBody:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    ViewBody = False
                    SnakeViewFunc()

        gameDisplay.fill(white)
        button = Button(115, 45, white, (137, 178, 245))
        button.draw("/Menu/",
                    black,
                    5,
                    5,
                    ViewBody,
                    game_intro)
        button = Button(115, 45, white, (137, 178, 245))
        button.draw("/Shop/",
                    black,
                    115,
                    5,
                    ViewBody,
                    game_shop)
        button = Button(115, 45, white, (137, 178, 245))
        button.draw("/View/",
                    black,
                    220,
                    5,
                    ViewBody,
                    SnakeViewFunc)
        money_shop()

        message_to_screen("Виды тела",
                        green,
                        -230,
                        size="medium")

        message_to_screen("Сейчас используется: "+SnakeBody_shop_m,
                        (133, 58, 252),
                        - 160)

        button_body0 = Button(550, 50, white, (200, 245, 150))
        button_body0.SnakeBody0(150, 250, "1 - Обычное тело => ", green, Body0_shop, shop_snake_body0, "Обычное тело")

        button_body1 = Button(550, 50, white, (200, 245, 150))
        button_body1.SnakeBody1(150, 320, "2 - Волнистое тело => ", green, Body1_shop, shop_snake_body1, "Волнистое тело", 50)

        button_body2 = Button(550, 50, white, (200, 245, 150))
        button_body2.SnakeBody2(150, 390, "3 - Тёмное тело => ", green, Body2_shop, shop_snake_body2, "Тёмное тело", 60)

        button_body3 = Button(550, 50, white, (200, 245, 150))
        button_body3.SnakeBody3(150, 460, "4 - Радужное тело => ", green, Body3_shop, shop_snake_body3, "Радужное тело", 80)


        pygame.display.update()
        clock.tick(15)

def SnakeViewFunc():
    shop_View = True
    while shop_View:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

                if event.key == pygame.K_n:
                	shop_View = False
                	game_shop()
            
        gameDisplay.fill(white)
        button = Button(115, 45, white, (137, 178, 245))
        button.draw("/Menu/",
                    black,
                    5,
                    5,
                    shop_View,
                    game_intro)
        button = Button(115, 45, white, (137, 178, 245))
        button.draw("/Shop/",
                    black,
                    115,
                    5,
                    shop_View,
                    game_shop)
        money_shop()
        message_to_screen("Вид змеи: ",
                            black,
                            -230,
                            size="medium")

        buttonHead = Button(170, 50, yellow, orenge)
        buttonHead.draw("1 - Голова",
                        blue,
                        display_height/2,
                        200,
                        shop_View,
                        SnakeViewHead)


        buttonHead = Button(170, 50, yellow, orenge)
        buttonHead.draw("2 - Тело",
                        blue,
                        display_height/2,
                        300,
                        shop_View,
                        SnakeViewBody)

        pygame.display.update()
        clock.tick(15)

green_shop = True
black_shop = False
red_shop = False
blue_shop = False
orenge_shop = False
yellow_shop = False
#магазин/настройка цвета змеи
def SnakeColorFunc():
    shop_Color = True
    while shop_Color:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            gameDisplay.fill(white)
            button_green = Button(400, 40, white, (200, 245, 150))
            button_green.draw_color_green("1 - Зеленый => ", green, 240, 300, green, green_shop, "Зеленый", 0)

            button_black = Button(400, 40, white, (200, 190, 180))
            button_black.draw_color_black("2 - Черный => ", black, 240, 350, black, black_shop, "Черный", 20)

            button_black = Button(400, 40, white, (245, 165, 150))
            button_black.draw_color_red("3 - Красный => ", red, 240, 400, red, red_shop, "Красный", 25)

            button_black = Button(400, 40, white, (155, 175, 245))
            button_black.draw_color_blue("4 - Синий => ", blue, 240, 450, blue, blue_shop, "Синий", 25)

            button_black = Button(400, 40, white, (240, 205, 190))
            button_black.draw_color_orenge("5 - Оранжевый => ", orenge, 240, 500, orenge, orenge_shop, "Оранжевый", 30)

            button_black = Button(400, 40, white, (240, 235, 220))
            button_black.draw_color_yellow("6 - Желтый => ", yellow, 240, 550, yellow, yellow_shop, "Желтый", 30)

        button = Button(115, 45, white, (137, 178, 245))
        button.draw("/Menu/",
                    black,
                    5,
                    5,
                    shop_Color,
                    game_intro)
        button = Button(115, 45, white, (137, 178, 245))
        button.draw("/Shop/",
                    black,
                    115,
                    5,
                    shop_Color,
                    game_shop)
        money_shop()
        message_to_screen("Цвет змейки: " + str(SnakeColor_shop),
                          black,
                          -200,
                          size="medium")

        message_to_screen("Доступные цвета: ",
                          (133, 58, 252),
                          -100,
                          size="medium")

        pygame.display.update()
        clock.tick(15)

#магазин
def game_shop():
    global money
    shop = True
    while shop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

                if event.key == pygame.K_n:
                    shop = False
                    game_intro()

                if event.key == pygame.K_1:
                    shop = False
                    SnakeViewFunc()

                if event.key == pygame.K_2:
                    shop = False
                    SnakeColorFunc()


        gameDisplay.fill(white)
        button = Button(115, 45, white, (137, 178, 245))
        button.draw("/Menu/",
                    black,
                    5,
                    5,
                    shop,
                    game_intro)
        money_shop()
        message_to_screen("МАГАЗИН",
                         blue,
                          -200,
                          size="large")

        button = Button(210, 50, (10, 111, 220), (10, 100, 200))
        button.draw("1 - Вид змеи",
                    red,
                    350,
                    250,
                    shop,
                    SnakeViewFunc)

        button = Button(210, 50, (10, 111, 220), (10, 100, 200))
        button.draw("2 - Цвет змеи",
                    red,
                    350,
                    350,
                    shop,
                    SnakeColorFunc)
            
        pygame.display.update()
        clock.tick(15)

SviewBody = True
SviewHead = True
#создание змеи
def snake(block_size, snakelist):
    global SnakeHead_shop
    global SnakeLine_shop
    if SviewHead == True:
        for XnY in snakelist[:-1]:
            pygame.draw.rect(gameDisplay, SnakeColor, [XnY[0],XnY[1],block_size,block_size])

    elif SviewHead == False:
        if direction == "right":
            head = pygame.transform.rotate(SnakeHead_shop, 270)

        if direction == "left":
            head = pygame.transform.rotate(SnakeHead_shop, 90)

        if direction == "up":
            head = SnakeHead_shop

        if direction == "down":
            head = pygame.transform.rotate(SnakeHead_shop, 180)

        gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))


    if SviewBody == True:
        for XnY in snakelist[:-1]:
            pygame.draw.rect(gameDisplay, SnakeColor, [XnY[0],XnY[1],block_size,block_size])

    elif SviewBody == False:
        for XnY in snakelist[:-1]:
            if direction == "right":
                line = pygame.transform.rotate(SnakeLine_shop, 270)
                gameDisplay.blit(line, [XnY[0], XnY[1]])

            if direction == "left":
                line = pygame.transform.rotate(SnakeLine_shop, 90)
                gameDisplay.blit(line, [XnY[0], XnY[1]])

            if direction == "up":
                line = SnakeLine_shop
                gameDisplay.blit(line, [XnY[0], XnY[1]])

            if direction == "down":
                line = pygame.transform.rotate(SnakeLine_shop, 180)
                gameDisplay.blit(line, [XnY[0], XnY[1]])
######################################################################################
rand_mission_g1 = 0
def rand_mission1():
    global mis_c1
    global rand_mission_g1
    if mis_c1 == True:
        rand_mission_g1 = random.randint(1, 5)
        mis_c1 = False
    else:
        pass

game_m1 = ""
mis_c1 = True
mis_c1_a1 = False
mis_c1_a2 = False
mis_c1_a3 = False
mis_c1_a4 = False
mis_c1_a5 = False
def game_mission1():
    global game_m1
    global EatApple
    global rand_mission_g1

    global mis_c1
    global mis_c1_a1
    global mis_c1_a2
    global mis_c1_a3
    global mis_c1_a4
    global mis_c1_a5

    text_mission1 = smallfont.render("Миссии: ", True, green)
    gameDisplay.blit(text_mission1, [250,110])

    rand_mission1()


    if mis_c1 == False:
        if rand_mission_g1 == 1:
            if mis_c1_a1 == False:
                if EatApple < 20:
                    game_m1 = "Съесть 20 яблок - " + str(EatApple)+"/20"
                    button11 = Button(580, 50, (239, 135, 1), orenge)
                    button11.draw_mission("1-Миссия: "+str(game_m1),
                                        red,
                                        55,
                                        180)

                elif EatApple >= 20:
                    mis_c1_a1 = True

            elif mis_c1_a1 == True:
                game_m1 = "Съесть 20 яблок  +25 монет"
                button12 = Button(580, 50, (239, 135, 1), orenge)
                button12.draw_mission("1-Миссия: "+str(game_m1),
                                    red,
                                    55,
                                    180,
                                    25,
                                    EatApple)

                if EatApple < 20:
                    mis_c1_a1 = False
                    mis_c1 = True
                    rand_mission1()


        if rand_mission_g1 == 2:
            if mis_c1_a2 == False:
                if EatApple < 15:
                    game_m1 = "Съесть 15 яблок - " + str(EatApple)+"/15"
                    button21 = Button(580, 50, (239, 135, 1), orenge)
                    button21.draw_mission("1-Миссия: "+str(game_m1),
                                        red,
                                        55,
                                        180)

                elif EatApple >= 15:
                    mis_c1_a2 = True

            elif mis_c1_a2 == True:
                game_m1 = "Съесть 15 яблок  +20 монет"
                button22 = Button(580, 50, (239, 135, 1), orenge)
                button22.draw_mission("1-Миссия: "+str(game_m1),
                                    red,
                                    55,
                                    180,
                                    20,
                                    EatApple)

                if EatApple < 15:
                    mis_c1_a2 = False
                    mis_c1 = True
                    rand_mission1()

        if rand_mission_g1 == 3:
            if mis_c1_a3 == False:
                if EatApple < 25:
                    game_m1 = "Съесть 25 яблок - " + str(EatApple)+"/25"
                    button31 = Button(580, 50, (239, 135, 1), orenge)
                    button31.draw_mission("1-Миссия: "+str(game_m1),
                                        red,
                                        55,
                                        180)

                elif EatApple >= 25:
                    mis_c1_a3 = True

            elif mis_c1_a3 == True:
                game_m1 = "Съесть 25 яблок  +30 монет"
                button32 = Button(580, 50, (239, 135, 1), orenge)
                button32.draw_mission("1-Миссия: "+str(game_m1),
                                    red,
                                    55,
                                    180,
                                    30,
                                    EatApple)

                if EatApple < 25:
                    mis_c1_a3 = False
                    mis_c1 = True
                    rand_mission1()

        if rand_mission_g1 == 4:
            if mis_c1_a4 == False:
                if EatApple < 30:
                    game_m1 = "Съесть 30 яблок - " + str(EatApple)+"/30"
                    button41 = Button(580, 50, (239, 135, 1), orenge)
                    button41.draw_mission("1-Миссия: "+str(game_m1),
                                        red,
                                        55,
                                        180)

                elif EatApple >= 30:
                    mis_c1_a4 = True

            elif mis_c1_a4 == True:
                game_m1 = "Съесть 30 яблок  +35 монет"
                button42 = Button(580, 50, (239, 135, 1), orenge)
                button42.draw_mission("1-Миссия: "+str(game_m1),
                                    red,
                                    55,
                                    180,
                                    35,
                                    EatApple)

                if EatApple < 30:
                    mis_c1_a4 = False
                    mis_c1 = True
                    rand_mission1()

        if rand_mission_g1 == 5:
            if mis_c1_a5 == False:
                if EatApple < 35:
                    game_m1 = "Съесть 35 яблок - " + str(EatApple)+"/35"
                    button51 = Button(580, 50, (239, 135, 1), orenge)
                    button51.draw_mission("1-Миссия: "+str(game_m1),
                                        red,
                                        55,
                                        180)

                elif EatApple >= 35:
                    mis_c1_a5 = True

            elif mis_c1_a5 == True:
                game_m1 = "Съесть 35 яблок  +40 монет"
                button52 = Button(580, 50, (239, 135, 1), orenge)
                button52.draw_mission("1-Миссия: "+str(game_m1),
                            red,
                            55,
                            180,
                            40,
                            EatApple)

                if EatApple < 35:
                    mis_c1_a5 = False
                    mis_c1 = True
                    rand_mission1()
####################         ####################         ####################
rand_mission_g2 = 0
def rand_mission2():
    global mis_c2
    global rand_mission_g2
    if mis_c2 == True:
        rand_mission_g2 = random.randint(1, 5)
        mis_c2 = False
    else:
        pass

game_m2 = ""
mis_c2 = True
mis_c2_a1 = False
mis_c2_a2 = False
mis_c2_a3 = False
mis_c2_a4 = False
mis_c2_a5 = False
def game_mission2():
    global game_m2
    global DiedNumber
    global rand_mission_g2

    global mis_c2
    global mis_c2_a1
    global mis_c2_a2
    global mis_c2_a3
    global mis_c2_a4
    global mis_c2_a5

    rand_mission2()

    if mis_c2 == False:
        if rand_mission_g2 == 1:
            if mis_c2_a1 == False:
                if DiedNumber < 20:
                    game_m2 = "Задеть хвост 20 раз - " + str(DiedNumber)+"/20"
                    button211 = Button(580, 50, (239, 135, 1), orenge)
                    button211.draw_mission("2-Миссия: "+str(game_m2),
                                        red,
                                        55,
                                        240)

                elif DiedNumber >= 20:
                    mis_c2_a1 = True

            elif mis_c2_a1 == True:
                game_m2 = "Задеть хвост 20  +25 монет"
                button212 = Button(580, 50, (239, 135, 1), orenge)
                button212.draw_mission("2-Миссия: "+str(game_m2),
                                    red,
                                    55,
                                    240,
                                    25,
                                    DiedNumber)

                if DiedNumber < 20:
                    mis_c2_a1 = False
                    mis_c2 = True
                    rand_mission2()


        if rand_mission_g2 == 2:
            if mis_c2_a2 == False:
                if DiedNumber < 15:
                    game_m2 = "Задеть хвост 15 раз - " + str(DiedNumber)+"/15"
                    button221 = Button(580, 50, (239, 135, 1), orenge)
                    button221.draw_mission("2-Миссия: "+str(game_m2),
                                        red,
                                        55,
                                        240)

                elif DiedNumber >= 15:
                    mis_c2_a2 = True

            elif mis_c2_a2 == True:
                game_m2 = "Задеть хвост 15  +20 монет"
                button222 = Button(580, 50, (239, 135, 1), orenge)
                button222.draw_mission("2-Миссия: "+str(game_m2),
                                    red,
                                    55,
                                    240,
                                    20,
                                    DiedNumber)

                if DiedNumber < 15:
                    mis_c2_a2 = False
                    mis_c2 = True
                    rand_mission2()


        if rand_mission_g2 == 3:
            if mis_c2_a3 == False:
                if DiedNumber < 25:
                    game_m2 = "Задеть хвост 25 раз - " + str(DiedNumber)+"/25"
                    button231 = Button(580, 50, (239, 135, 1), orenge)
                    button231.draw_mission("2-Миссия: "+str(game_m2),
                                        red,
                                        55,
                                        240)

                elif DiedNumber >= 25:
                    mis_c2_a3 = True

            elif mis_c2_a3 == True:
                game_m2 = "Задеть хвост 25  +30 монет"
                button232 = Button(580, 50, (239, 135, 1), orenge)
                button232.draw_mission("2-Миссия: "+str(game_m2),
                                    red,
                                    55,
                                    240,
                                    30,
                                    DiedNumber)

                if DiedNumber < 25:
                    mis_c2_a3 = False
                    mis_c2 = True
                    rand_mission2()

        if rand_mission_g2 == 4:
            if mis_c2_a4 == False:
                if DiedNumber < 30:
                    game_m2 = "Задеть хвост 30 раз - " + str(DiedNumber)+"/30"
                    button241 = Button(580, 50, (239, 135, 1), orenge)
                    button241.draw_mission("2-Миссия: "+str(game_m2),
                                        red,
                                        55,
                                        240)

                elif DiedNumber >= 30:
                    mis_c2_a4 = True

            elif mis_c2_a4 == True:
                game_m2 = "Задеть хвост 30  +35 монет"
                button242 = Button(580, 50, (239, 135, 1), orenge)
                button242.draw_mission("2-Миссия: "+str(game_m2),
                                    red,
                                    55,
                                    240,
                                    35,
                                    DiedNumber)

                if DiedNumber < 30:
                    mis_c2_a4 = False
                    mis_c2 = True
                    rand_mission2()

        if rand_mission_g2 == 5:
            if mis_c2_a5 == False:
                if DiedNumber < 35:
                    game_m2 = "Задеть хвост 35 раз - " + str(DiedNumber)+"/35"
                    button251 = Button(580, 50, (239, 135, 1), orenge)
                    button251.draw_mission("2-Миссия: "+str(game_m2),
                                        red,
                                        55,
                                        240)

                elif DiedNumber >= 35:
                    mis_c2_a5 = True

            elif mis_c2_a5 == True:
                game_m2 = "Задеть хвост 35  +40 монет"
                button252 = Button(580, 50, (239, 135, 1), orenge)
                button252.draw_mission("2-Миссия: "+str(game_m2),
                            red,
                            55,
                            240,
                            40,
                            DiedNumber)

                if DiedNumber < 35:
                    mis_c2_a5 = False
                    mis_c2 = True
                    rand_mission2()
####################         ####################         ####################
rand_mission_g3 = 0
def rand_mission3():
    global mis_c3
    global rand_mission_g3
    if mis_c3 == True:
        rand_mission_g3 = random.randint(1, 5)
        mis_c3 = False
    else:
        pass

game_m3 = ""
mis_c3 = True
mis_c3_a1 = False
mis_c3_a2 = False
mis_c3_a3 = False
mis_c3_a4 = False
mis_c3_a5 = False
def game_mission3():
    global game_m3
    global NewGame
    global rand_mission_g3

    global mis_c3
    global mis_c3_a1
    global mis_c3_a2
    global mis_c3_a3
    global mis_c3_a4
    global mis_c3_a5

    rand_mission3()

    if mis_c3 == False:
        if rand_mission_g3 == 1:
            if mis_c3_a1 == False:
                if NewGame < 20:
                    game_m3 = "Начать игру 20 раз - " + str(NewGame)+"/20"
                    button311 = Button(580, 50, (239, 135, 1), orenge)
                    button311.draw_mission("3-Миссия: "+str(game_m3),
                                        red,
                                        55,
                                        300)

                elif NewGame >= 20:
                    mis_c3_a1 = True

            elif mis_c3_a1 == True:
                game_m3 = "Начать игру 20   +25 монет"
                button312 = Button(580, 50, (239, 135, 1), orenge)
                button312.draw_mission("3-Миссия: "+str(game_m3),
                                    red,
                                    55,
                                    300,
                                    25,
                                    NewGame)

                if NewGame < 20:
                    mis_c3_a1 = False
                    mis_c3 = True
                    rand_mission3()


        if rand_mission_g3 == 2:
            if mis_c3_a2 == False:
                if NewGame < 15:
                    game_m3 = "Начать игру 15 раз - " + str(NewGame)+"/15"
                    button321 = Button(580, 50, (239, 135, 1), orenge)
                    button321.draw_mission("3-Миссия: "+str(game_m3),
                                        red,
                                        55,
                                        300)

                elif NewGame >= 15:
                    mis_c3_a2 = True

            elif mis_c3_a2 == True:
                game_m3 = "Начать игру 15   +20 монет"
                button322 = Button(580, 50, (239, 135, 1), orenge)
                button322.draw_mission("3-Миссия: "+str(game_m3),
                                    red,
                                    55,
                                    300,
                                    20,
                                    NewGame)

                if NewGame < 15:
                    mis_c3_a2 = False
                    mis_c3 = True
                    rand_mission3()


        if rand_mission_g3 == 3:
            if mis_c3_a3 == False:
                if NewGame < 25:
                    game_m3 = "Начать игру 25 раз - " + str(NewGame)+"/25"
                    button331 = Button(580, 50, (239, 135, 1), orenge)
                    button331.draw_mission("3-Миссия: "+str(game_m3),
                                        red,
                                        55,
                                        300)

                elif NewGame >= 25:
                    mis_c3_a3 = True

            elif mis_c3_a3 == True:
                game_m3 = "Начать игру 25   +30 монет"
                button332 = Button(580, 50, (239, 135, 1), orenge)
                button332.draw_mission("3-Миссия: "+str(game_m3),
                                    red,
                                    55,
                                    300,
                                    30,
                                    NewGame)

                if NewGame < 25:
                    mis_c3_a3 = False
                    mis_c3 = True
                    rand_mission3()

        if rand_mission_g3 == 4:
            if mis_c3_a4 == False:
                if NewGame < 30:
                    game_m3 = "Начать игру 30 раз - " + str(NewGame)+"/30"
                    button341 = Button(580, 50, (239, 135, 1), orenge)
                    button341.draw_mission("3-Миссия: "+str(game_m3),
                                        red,
                                        55,
                                        300)

                elif NewGame >= 30:
                    mis_c3_a4 = True

            elif mis_c3_a4 == True:
                game_m3 = "Начать игру 30   +35 монет"
                button342 = Button(580, 50, (239, 135, 1), orenge)
                button342.draw_mission("3-Миссия: "+str(game_m3),
                                    red,
                                    55,
                                    300,
                                    35,
                                    NewGame)

                if NewGame < 30:
                    mis_c3_a4 = False
                    mis_c3 = True
                    rand_mission3()

        if rand_mission_g3 == 5:
            if mis_c3_a5 == False:
                if NewGame < 35:
                    game_m3 = "Начать игру 35 раз - " + str(NewGame)+"/35"
                    button351 = Button(580, 50, (239, 135, 1), orenge)
                    button351.draw_mission("3-Миссия: "+str(game_m3),
                                        red,
                                        55,
                                        300)

                elif NewGame >= 35:
                    mis_c3_a5 = True

            elif mis_c3_a5 == True:
                game_m3 = "Начать игру 35   +40 монет"
                button352 = Button(580, 50, (239, 135, 1), orenge)
                button352.draw_mission("3-Миссия: "+str(game_m3),
                            red,
                            55,
                            300,
                            40,
                            NewGame)

                if NewGame < 35:
                    mis_c3_a5 = False
                    mis_c3 = True
                    rand_mission3()
####################         ####################         ####################
rand_mission_g4 = 0
def rand_mission4():
    global mis_c4
    global rand_mission_g4
    if mis_c4 == True:
        rand_mission_g4 = random.randint(1, 5)
        mis_c4 = False
    else:
        pass

game_m4 = ""
mis_c4 = True
mis_c4_a1 = False
mis_c4_a2 = False
mis_c4_a3 = False
mis_c4_a4 = False
mis_c4_a5 = False
def game_mission4():
    global game_m4
    global bomb_mission
    global rand_mission_g4

    global mis_c4
    global mis_c4_a1
    global mis_c4_a2
    global mis_c4_a3
    global mis_c4_a4
    global mis_c4_a5

    rand_mission4()

    if mis_c4 == False:
        if rand_mission_g4 == 1:
            if mis_c4_a1 == False:
                if bomb_mission < 20:
                    game_m4 = "Взорвать бомбу 20 раз - " + str(bomb_mission)+"/20"
                    button411 = Button(580, 50, (239, 135, 1), orenge)
                    button411.draw_mission("4-Миссия: "+str(game_m4),
                                        red,
                                        55,
                                        360)

                elif bomb_mission >= 20:
                    mis_c4_a1 = True

            elif mis_c4_a1 == True:
                game_m4 = "Взорвать бомбу   +25 монет"
                button412 = Button(580, 50, (239, 135, 1), orenge)
                button412.draw_mission("4-Миссия: "+str(game_m4),
                                    red,
                                    55,
                                    360,
                                    25,
                                    bomb_mission)

                if bomb_mission < 20:
                    mis_c4_a1 = False
                    mis_c4 = True
                    rand_mission4()


        if rand_mission_g4 == 2:
            if mis_c4_a2 == False:
                if bomb_mission < 15:
                    game_m4 = "Взорвать бомбу 15 раз - " + str(bomb_mission)+"/15"
                    button421 = Button(580, 50, (239, 135, 1), orenge)
                    button421.draw_mission("4-Миссия: "+str(game_m4),
                                        red,
                                        55,
                                        360)

                elif bomb_mission >= 15:
                    mis_c4_a2 = True

            elif mis_c4_a2 == True:
                game_m4 = "Взорвать бомбу   +20 монет"
                button422 = Button(580, 50, (239, 135, 1), orenge)
                button422.draw_mission("4-Миссия: "+str(game_m4),
                                    red,
                                    55,
                                    360,
                                    20,
                                    bomb_mission)

                if bomb_mission < 15:
                    mis_c4_a2 = False
                    mis_c4 = True
                    rand_mission4()


        if rand_mission_g4 == 3:
            if mis_c4_a3 == False:
                if bomb_mission < 25:
                    game_m4 = "Взорвать бомбу 25 раз - " + str(bomb_mission)+"/25"
                    button431 = Button(580, 50, (239, 135, 1), orenge)
                    button431.draw_mission("4-Миссия: "+str(game_m4),
                                        red,
                                        55,
                                        360)

                elif bomb_mission >= 25:
                    mis_c4_a3 = True

            elif mis_c4_a3 == True:
                game_m4 = "Взорвать бомбу   +30 монет"
                button432 = Button(580, 50, (239, 135, 1), orenge)
                button432.draw_mission("4-Миссия: "+str(game_m4),
                                    red,
                                    55,
                                    360,
                                    30,
                                    bomb_mission)

                if bomb_mission < 25:
                    mis_c4_a3 = False
                    mis_c4 = True
                    rand_mission4()

        if rand_mission_g4 == 4:
            if mis_c4_a4 == False:
                if bomb_mission < 30:
                    game_m4 = "Взорвать бомбу 30 раз - " + str(bomb_mission)+"/30"
                    button441 = Button(580, 50, (239, 135, 1), orenge)
                    button441.draw_mission("4-Миссия: "+str(game_m4),
                                        red,
                                        55,
                                        360)

                elif bomb_mission >= 30:
                    mis_c4_a4 = True

            elif mis_c4_a4 == True:
                game_m4 = "Взорвать бомбу   +35 монет"
                button442 = Button(580, 50, (239, 135, 1), orenge)
                button442.draw_mission("4-Миссия: "+str(game_m4),
                                    red,
                                    55,
                                    360,
                                    35,
                                    bomb_mission)

                if bomb_mission < 30:
                    mis_c4_a4 = False
                    mis_c4 = True
                    rand_mission4()

        if rand_mission_g4 == 5:
            if mis_c4_a5 == False:
                if bomb_mission < 35:
                    game_m4 = "Взорвать бомбу 35 раз - " + str(bomb_mission)+"/35"
                    button451 = Button(580, 50, (239, 135, 1), orenge)
                    button451.draw_mission("4-Миссия: "+str(game_m4),
                                        red,
                                        55,
                                        360)

                elif bomb_mission >= 35:
                    mis_c4_a5 = True

            elif mis_c4_a5 == True:
                game_m4 = "Взорвать бомбу   +40 монет"
                button452 = Button(580, 50, (239, 135, 1), orenge)
                button452.draw_mission("4-Миссия: "+str(game_m4),
                            red,
                            55,
                            360,
                            40,
                            bomb_mission)

                if bomb_mission < 35:
                    mis_c4_a5 = False
                    mis_c4 = True
                    rand_mission4()
####################         ####################         ####################
rand_mission_g5 = 0
def rand_mission5():
    global mis_c5
    global rand_mission_g5
    if mis_c5 == True:
        rand_mission_g5 = random.randint(1, 5)
        mis_c5 = False
    else:
        pass

game_m5 = ""
mis_c5 = True
mis_c5_a1 = False
mis_c5_a2 = False
mis_c5_a3 = False
mis_c5_a4 = False
mis_c5_a5 = False

mis_c5_a1_1 = False
mis_c5_a2_2 = False
mis_c5_a3_3 = False
mis_c5_a4_4 = False
mis_c5_a5_5 = False
def game_mission5():
    global game_m5
    global mission_color
    global rand_mission_g5

    global mis_c5
    global mis_c5_a1
    global mis_c5_a2
    global mis_c5_a3
    global mis_c5_a4
    global mis_c5_a5

    global mis_c5_a1_1
    global mis_c5_a2_2
    global mis_c5_a3_3
    global mis_c5_a4_4
    global mis_c5_a5_5

    rand_mission5()

    if mis_c5 == False:
        if rand_mission_g5 == 1:
            if mis_c5_a1_1 == False:
                if mis_c5_a1 == False:
                    if mission_color == 0:
                        game_m5 = "Купить черный цвет - " + str(mission_color)+"/1"
                        button511 = Button(580, 50, (239, 135, 1), orenge)
                        button511.draw_mission("5-Миссия: "+str(game_m5),
                                            red,
                                            55,
                                            420)

                    elif mission_color == 1:
                        mis_c5_a1 = True

                elif mis_c5_a1 == True:
                    game_m5 = "Купить цвет      +25 монет"
                    button512 = Button(580, 50, (239, 135, 1), orenge)
                    button512.draw_mission("5-Миссия: "+str(game_m5),
                                        red,
                                        55,
                                        420,
                                        25,
                                        mission_color)

                    if mission_color == 0:
                        mis_c5_a1_1 = True
                        mis_c5_a1 = False
                        mis_c5 = True
                        rand_mission5()
            elif mis_c5_a1_1 == True:
                mis_c5 = True
                rand_mission5()

        elif rand_mission_g5 == 2:
            if mis_c5_a2_2 == False:
                if mis_c5_a2 == False:
                    if mission_color == 0:
                        game_m5 = "Купить красный цвет - " + str(mission_color)+"/1"
                        button521 = Button(580, 50, (239, 135, 1), orenge)
                        button521.draw_mission("5-Миссия: "+str(game_m5),
                                            red,
                                            55,
                                            420)

                    elif mission_color == 2:
                        mis_c5_a2 = True

                elif mis_c5_a2 == True:
                    game_m5 = "Купить цвет      +30 монет"
                    button522 = Button(580, 50, (239, 135, 1), orenge)
                    button522.draw_mission("5-Миссия: "+str(game_m5),
                                        red,
                                        55,
                                        420,
                                        30,
                                        mission_color)

                    if mission_color == 0:
                        mis_c5_a2_2 = True
                        mis_c5_a2 = False
                        mis_c5 = True
                        rand_mission5()
            elif mis_c5_a2_2 == True:
                mis_c5 = True
                rand_mission5()

        elif rand_mission_g5 == 3:
            if mis_c5_a3_3 == False:
                if mis_c5_a3 == False:
                    if mission_color == 0:
                        game_m5 = "Купить синий цвет - " + str(mission_color)+"/1"
                        button531 = Button(580, 50, (239, 135, 1), orenge)
                        button531.draw_mission("5-Миссия: "+str(game_m5),
                                            red,
                                            55,
                                            420)

                    elif mission_color == 3:
                        mis_c5_a3 = True

                elif mis_c5_a3 == True:
                    game_m5 = "Купить цвет      +30 монет"
                    button532 = Button(580, 50, (239, 135, 1), orenge)
                    button532.draw_mission("5-Миссия: "+str(game_m5),
                                        red,
                                        55,
                                        420,
                                        30,
                                        mission_color)

                    if mission_color == 0:
                        mis_c5_a3_3 = True
                        mis_c5_a3 = False
                        mis_c5 = True
                        rand_mission5()
            elif mis_c5_a3_3 == True:
                mis_c5 = True
                rand_mission5()

        elif rand_mission_g5 == 4:
            if mis_c5_a4_4 == False:
                if mis_c5_a4 == False:
                    if mission_color == 0:
                        game_m5 = "Купить оранжевый цвет-" + str(mission_color)+"/1"
                        button541 = Button(580, 50, (239, 135, 1), orenge)
                        button541.draw_mission("5-Миссия: "+str(game_m5),
                                            red,
                                            55,
                                            420)

                    elif mission_color == 4:
                        mis_c5_a4 = True

                elif mis_c5_a4 == True:
                    game_m5 = "Купить цвет      +35 монет"
                    button542 = Button(580, 50, (239, 135, 1), orenge)
                    button542.draw_mission("5-Миссия: "+str(game_m5),
                                        red,
                                        55,
                                        420,
                                        35,
                                        mission_color)

                    if mission_color == 0:
                        mis_c5_a4_4 = True
                        mis_c5_a4 = False
                        mis_c5 = True
                        rand_mission4()
            elif mis_c5_a4_4 == True:
                mis_c5 = True
                rand_mission4()

        elif rand_mission_g5 == 5:
            if mis_c5_a5_5 == False:
                if mis_c5_a5 == False:
                    if mission_color == 0:
                        game_m5 = "Купить желтый цвет - " + str(mission_color)+"/1"
                        button551 = Button(580, 50, (239, 135, 1), orenge)
                        button551.draw_mission("5-Миссия: "+str(game_m5),
                                            red,
                                            55,
                                            420)

                    elif mission_color == 5:
                        mis_c5_a5 = True

                elif mis_c5_a5 == True:
                    game_m5 = "Купить цвет      +35 монет"
                    button552 = Button(580, 50, (239, 135, 1), orenge)
                    button552.draw_mission("5-Миссия: "+str(game_m5),
                                red,
                                55,
                                420,
                                35,
                                mission_color)

                    if mission_color == 0:
                        mis_c5_a5_5 = True
                        mis_c5_a5 = False
                        mis_c5 = True
                        rand_mission5()
            elif mis_c5_a5_5 == True:
                mis_c5 = True
                rand_mission5()

    elif mis_c5_a5_1 == True and mis_c5_a5_2 == True and mis_c5_a5_3 == True and mis_c5_a5_4 == True and mis_c5_a5_5 == True:
        game_m5 = "Вы преобрели все цвета"
####################         ####################         ####################
def game_mission():
    game_mission1()
    game_mission2()
    game_mission3()
    game_mission4()
    game_mission5()

#меню в игре
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
             #если была нажата клавиша(с-англ)
                if event.key == pygame.K_c:
                    intro = False
                    gameLoop()
               #если была нажата клавиша(n-англ)
                if event.key == pygame.K_m:
                    intro = False
                    game_shop()
                if event.key == pygame.K_s:
                    intro = False
                    game_settings()
                if event.key == pygame.K_k:
                    intro = False
                    game_console()
               #если была нажата клавиша(q-англ)
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        #вывод на экран
        gameDisplay.fill(white)
        button = Button(130, 130)
        message_to_screen("Добро пожаловать в змейку!",
                          green,
                          -300,
                          size="medium")

        message_to_screen("DenGameStudio",
                          (240, 220, 175),
                          -340,
                          -370,
                          size="micro")

        pygame.draw.rect(gameDisplay, (239, 135, 1), (50, 100, 590, 500))
        pygame.draw.rect(gameDisplay, (181, 132, 30), (50, 100, 590, 500), 10)
        game_mission()

        button = Button(95, 95)
        button.draw_picture(button_settings,
                            690,
                            400,
                            intro,
                            game_settings)

        button = Button(77, 82)
        button.draw_picture(button2_info,
                            818,
                            5,
                            intro,
                            None,
                            WebPage='https://vk.com/dengamestudio')

        button = Button(150, 53)
        button.draw_picture(button_play,
                            670,
                            200,
                            intro,
                            gameLoop,
                            WebPage=None,
                            start=True)

        button = Button(171, 70)
        button.draw_picture(button_shop,
                            660,
                            300,
                            intro,
                            game_shop)


        #update экрана
        pygame.display.update()
        clock.tick(15)

#функция видов текстов
def text_objects(text,color,size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
    elif size == "micro":
        textSurface = microfont.render(text, True, color)
    
    return textSurface, textSurface.get_rect()

#функции вывода текста на экран
def message_to_screen(msg, color, y_displace=0, x_displase=0, size = "small"):
    textSurf, textRect = text_objects(msg,color, size)
    textRect.center = (display_width / 2)+x_displase, (display_height / 2)+y_displace
    gameDisplay.blit(textSurf, textRect)

#главная функция
def gameLoop():
    global paused

    global direction

    global money
    global life

    global EatApple
    global DiedNumber

    direction = 'right'

    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change = 10
    lead_y_change = 0

    snakeList = []
    snakeLength = 2
    
    randAppleX, randAppleY = randAppleGen()

    bomb_draw_x, bomb_draw_y = game_bomb()

    while not gameExit:
        #если игрок умер
        while gameOver == True:
            gameDisplay.fill(white)
            pygame.draw.rect(gameDisplay, (222, 144, 20), (0, 0, 900, 700), 20)
            message_to_screen("Ты умер",
                              red,
                              y_displace=-250,
                              size="large")

            score_d(snakeLength-2)
            
            button = Button(77, 83)
            button.draw_picture(button_play,
                                380,
                                350,
                                gameOver,
                                gameLoop)

            button = Button(155, 167, (10, 111, 220), (10, 100, 200))
            button.draw_picture(button2_menu,
                                15,
                                15,
                                gameExit,
                                game_intro)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
                    if event.key == pygame.K_m:
                    	gameExit = False
                    	gameOver = True
                    	game_intro()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if joystick == "W-S-A-D":
                    #если была нажата клавиша влево
                    if event.key == pygame.K_a:
                        direction = "left"
                        lead_x_change = -block_size
                        lead_y_change = 0
                    #если была нажата клавиша вправо
                    elif event.key == pygame.K_d:
                        direction = "right"
                        lead_x_change = block_size
                        lead_y_change = 0
                    #если была нажата клавиша на верх
                    elif event.key == pygame.K_w:
                        direction = "up"
                        lead_y_change = -block_size
                        lead_x_change = 0
                    #если была нажата клавиша вниз
                    elif event.key == pygame.K_s:
                        direction = "down"
                        lead_y_change = block_size
                        lead_x_change = 0

                if joystick == "Стрелочки":
                    #если была нажата клавиша влево
                    if event.key == pygame.K_LEFT:
                        direction = "left"
                        lead_x_change = -block_size
                        lead_y_change = 0
                    #если была нажата клавиша вправо
                    elif event.key == pygame.K_RIGHT:
                        direction = "right"
                        lead_x_change = block_size
                        lead_y_change = 0
                    #если была нажата клавиша на верх
                    elif event.key == pygame.K_UP:
                        direction = "up"
                        lead_y_change = -block_size
                        lead_x_change = 0
                    #если была нажата клавиша вниз
                    elif event.key == pygame.K_DOWN:
                        direction = "down"
                        lead_y_change = block_size
                        lead_x_change = 0

                if event.key == pygame.K_p:
                    paused = True
                    pause()

        #перемещение из одной стороны в другую
        #горизонтально
        if lead_x >= display_width:
        	lead_x = -9
        elif lead_x < 0:
        	lead_x = display_width-9

        #вертикально
        if lead_y >= display_height:
        	lead_y = -9
        elif lead_y < 0:
        	lead_y = display_height-9

        #змея
        lead_x += lead_x_change
        lead_y += lead_y_change

        #задний фон
        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay, (222, 144, 20), (0, 0, 900, 700), 20)
        #####################
        button = Button(77, 84)
        button.draw_picture(button2_paused,
                            800,
                            20,
                            None,
                            pause)

        #рисование яблок
        #pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, AppleThickness, AppleThickness])
        gameDisplay.blit(appleimg, (randAppleX, randAppleY))

        gameDisplay.blit(draw_bomb, (bomb_draw_x, bomb_draw_y))

        #змея
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        #отслеживание движений
        if len(snakeList) > snakeLength:
            del snakeList[0]
      
        #отслеживание задивание хвоста
        if life == True:
            for eachSegment in snakeList[:-1]:
                if eachSegment == snakeHead:
                    gameOver = True
                    DiedNumber += 1

        if life == False:
            for eachSegment in snakeList[:-1]:
                if eachSegment == snakeHead:
                    gameOver = False

        #змея
        snake(block_size, snakeList)

        #обновление рекорда
        score(snakeLength-2)

        #обновление экрана
        pygame.display.update()

        #отслеживание задивание бомбы
        if lead_x > bomb_draw_x and lead_x < bomb_draw_x + 30 or lead_x + block_size > bomb_draw_x and lead_x + block_size < bomb_draw_x + 30:
            if lead_y > bomb_draw_y and lead_y < bomb_draw_y + 30:
                bomb_boom()
                gameOver = True
            elif lead_y + block_size > bomb_draw_y and lead_y + block_size < bomb_draw_y + 30:
                bomb_boom()
                gameOver = True

        #отслеживание поедание яблок
        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:

            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:

                randAppleX,randAppleY = randAppleGen()
                snakeLength += 1
                EatApple += 1

            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:

                randAppleX,randAppleY = randAppleGen()
                snakeLength += 1
                EatApple += 1

 
        #скорость
        clock.tick(FPS)
    #выход(остановка игры)
    pygame.quit()
    quit()

#начало игры
if __name__ == "__main__":
    introFunc()