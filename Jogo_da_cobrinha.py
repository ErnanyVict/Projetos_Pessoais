import pygame as pg
from random import randint
import time

pg.init()

def position_apple(l, a):
    l = randint(100, 700)
    a = randint(50, 550)
    return l, a

largura, altura = 800, 600
screen = pg.display.set_mode((largura, altura))

dark_green = [25, 111, 61]
dark_blue = [41, 128, 185]
red = [231, 76, 60]

l, a = 300, 400

wall1 = pg.Rect(0, 0, 40, 600)
wall2 = pg.Rect(760, 0, 40, 600)
wall3 = pg.Rect(0, 0, 800, 40)
wall4 = pg.Rect(0, 560, 800, 40)

player = pg.Rect(400, 300, 20, 20)
vx, vy = 0, 0

snake_body = [player]

exe = True
while exe:
    for event in  pg.event.get():
        if event.type == pg.QUIT:
            exe = False

    screen.fill((88, 214, 141))

    apple = pg.Rect(l, a, 20, 20)

    pg.draw.rect(screen, dark_green, wall1)
    pg.draw.rect(screen, dark_green, wall2)
    pg.draw.rect(screen, dark_green, wall3)
    pg.draw.rect(screen, dark_green, wall4)
    pg.draw.rect(screen, dark_blue, player)
    pg.draw.rect(screen, red, apple)

    for x in range(1, len(snake_body)):
        pg.draw.rect(screen, dark_blue, snake_body[x])

    keys = pg.key.get_pressed()
    if keys[pg.K_a] and vx != 20:
        vx = -20
        vy = 0

    if keys[pg.K_d] and vx != -20:
        vx = 20
        vy = 0

    if keys[pg.K_w] and vy != 20:
        vy = -20
        vx = 0

    if keys[pg.K_s] and vy != -20:
        vy = 20
        vx = 0

    player.left += vx
    player.top += vy
    if (wall1.colliderect(player)) or (wall4.colliderect(player)) or wall2.colliderect(player) or wall3.colliderect(player):
        vx, vy = 0, 0

    elif apple.colliderect(player):
        l, a = position_apple(l, a)
        new_body = pg.Rect(snake_body[-1].x, snake_body[-1].y, player.width, player.height)
        snake_body.append(new_body)
        menox, menosy = 0, 0

    for x in range(len(snake_body) -1, 0, -1):
        snake_body[x].x = snake_body[x-1].x
        snake_body[x].y = snake_body[x-1].y

    
    for segment in snake_body[2:]:
        if player.colliderect(segment):
            exe = False

    time.sleep(0.07)

    pg.display.flip()

pg.quit()