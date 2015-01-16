# -*- coding: utf-8 -*-
__author__ = 'Administrator'

# 指定图像文件名称
background_image_filename = 'sushiplate.jpg'
mouse_image_filename = 'fugu.png'

# 导入pygame库
import pygame
# 导入一些常用的函数和常量
from pygame.locals import *
# 向sys模块借一个exit函数用来退出程序
from sys import exit

# 初始化pygame，为使用硬件做准备
pygame.init()

# 创建了一个窗口
screen = pygame.display.set_mode((640, 480), 0, 32)
# 设置窗口标题
pygame.display.set_caption("Hello World")

# 加载并转换图像
background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(mouse_image_filename).convert_alpha()
x = 0

# 游戏主循环
while True:
    for event in pygame.event.get():
        # 接收到退出事件后退出程序
        if event.type == QUIT:
            exit()
    # 将背景图画上去
    screen.blit(background, (0, 0))
    screen.blit(sprite, (x, 100))

    x += 1
    if x > 640:
        x = 0

    # 刷新一下画面
    pygame.display.update()




