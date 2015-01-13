# -*- coding: utf-8 -*-
__author__ = 'Administrator'
background_image_filename = 'sushiplate.jpg'

from sys import exit

import pygame
from pygame.locals import *


SCREEN_SIZE = (640, 480)
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
background = pygame.image.load(background_image_filename).convert()

fullscreen = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_f:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode(SCREEN_SIZE, FULLSCREEN, 32)
                else:
                    screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        pygame.display.update()