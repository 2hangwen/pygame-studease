# -*- encoding: utf-8 -*-
__author__ = 'Administrator'

from sys import exit

import pygame
from pygame.locals import *


SCREEN_SIZE = (640, 480)
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
pygame.display.set_caption("Event List")

font = pygame.font.SysFont("arial", 16)
font_height = font.get_linesize()
event_text = []

while True:
    event = pygame.event.wait()
    # 获取事件的名称
    event_text.append(str(event))
    # 这个切片操作保证了event_text里面只保留一个屏幕的文字
    event_text = event_text[-SCREEN_SIZE[1] / font_height:]

    if event.type == QUIT:
        exit()
    screen.fill((255, 255, 255))

    # 找一个合适的起笔位置，最下面开始但是要留一行的空
    y = SCREEN_SIZE[1] - font_height
    for text in reversed(event_text):
        screen.blit(font.render(text, True, (0, 0, 0)), (0, y))
        # 把笔提一行
        y -= font_height

    pygame.display.update()



