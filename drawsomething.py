# -*- coding: utf-8 -*-
__author__ = 'Administrator'

from sys import exit
from random import randint
from math import pi

import pygame
from pygame.locals import *


pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
points = []

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        # 按任意键可以清屏并把点回复到原始状态
        if event.type == KEYDOWN:
            points = []
            screen.fill((255, 255, 255))
        if event.type == MOUSEBUTTONDOWN:
            screen.fill((255, 255, 255))
            # 画随机矩形
            rc = (randint(0, 255), randint(0, 255), randint(0, 255))
            rp = (randint(0, 639), randint(0, 479))
            rs = (639 - randint(rp[0], 639), 479 - randint(rp[1], 479))
            pygame.draw.rect(screen, rc, Rect(rp, rs))
            # 画随机圆形
            rc = (randint(0, 255), randint(0, 255), randint(0, 255))
            rp = (randint(0, 639), randint(0, 479))
            rr = randint(1, 200)
            pygame.draw.circle(screen, rc, rp, rr)
            # 获取当前素表的点击位置
            x, y = pygame.mouse.get_pos()
            points.append((x, y))
            # 根据点击位置画弧线
            angle = (x / 639.) * pi * 2
            pygame.draw.arc(screen, (0, 0, 0), (0, 0, 639, 479), 0, angle, 3)
            # 根据点击位置画椭圆
            pygame.draw.ellipse(screen, (0, 255, 0), (0, 0, x, y))
            # 从左上到右下画两条线连接到点击位置
            pygame.draw.line(screen, (0, 0, 255), (0, 0), (x, y))
            pygame.draw.line(screen, (255, 0, 0), (x, y), (640, 480))
            # 画点击轨迹
            if len(points) > 1:
                pygame.draw.lines(screen, (155, 155, 0), False, points, 2)
            for p in points:
                pygame.draw.circle(screen, (155, 155, 0), p, 3)

    pygame.display.update()

