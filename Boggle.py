import pygame
import time
import math
import random

pygame.init()
window = pygame.display.set_mode((600, 700))
clock = pygame.time.Clock()
points = []
lines = []
begin = False
anim = False
font = pygame.font.SysFont('didot.ttc', 70)

newBoard = True
while True:
    letters = {
        1:('a', 'a', 'a', 'f', 'r', 's'),
        2:('a', 'a', 'e', 'e', 'e', 'e'),
        3:('a', 'a', 'f', 'i', 'r', 's'),
        4:('a', 'd', 'e', 'n', 'n', 'n'),
        5:('a', 'e', 'e', 'e', 'e', 'm'),
        6:('a', 'e', 'e', 'g', 'm', 'u'),
        7:('a', 'e', 'g', 'm', 'n', 'n'),
        8:('a', 'f', 'i', 'r', 's', 'y'),
        9:('b', 'j', 'k', 'q', 'x', 'z'),
        10:('c', 'c', 'e', 'n', 's', 't'),
        11:('c', 'e', 'i', 'i', 'l', 't'),
        12:('c', 'e', 'i', 'l', 'p', 't'),
        13:('c', 'e', 'i', 'p', 's', 't'),
        14:('d', 'd', 'h', 'n', 'o', 't'),
        15:('d', 'h', 'h', 'l', 'o', 'r'),
        16:('d', 'h', 'l', 'n', 'o', 'r'),
        17:('d', 'h', 'l', 'n', 'o', 'r'),
        18:('e', 'i', 'i', 'i', 't', 't'),
        19:('e', 'm', 'o', 't', 't', 't'),
        20:('e', 'n', 's', 's', 's', 'u'),
        21:('f', 'i', 'p', 'r', 's', 'y'),
        22:('g', 'o', 'r', 'r', 'v', 'w'),
        23:('i', 'p', 'r', 'r', 'r', 'y'),
        24:('n', 'o', 'o', 't', 'u', 'w'),
        25:('o', 'o', 'o', 't', 't', 'u')
    }
    window.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                newBoard = True

    if newBoard:
        start_ticks = pygame.time.get_ticks()
        dice = list(letters.keys())
        random.shuffle(dice)
        indices = []
        for i in range(25):
            indices.append(random.randint(0,5))
        newBoard = False

    for i in range(6):
        pygame.draw.line(window, (255,255,255), ((i+1)*100 - 50, 50), ((i+1)*100 - 50,550))
        pygame.draw.line(window, (255,255,255), (50, (i+1)*100 - 50), (550, (i+1)*100 - 50))
    for x in range(5):
        for y in range(5):
            current = letters[dice[5*x + y]][indices[5*x+y]].upper()
            l =font.render(current, True, (255,0,0))
            window.blit(l, ((y+1)*100 - 20, (x+1)*100 - 20))

    seconds = pygame.time.get_ticks() - start_ticks
    t = font.render(str(round(seconds/1000)), True, (255,0,0))
    window.blit(t, (250,650))
    pygame.display.update()
    clock.tick(30)
