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
from gameobjects.vector2 import Vector2

# 初始化pygame，为使用硬件做准备
pygame.init()

# 创建了一个窗口
screen = pygame.display.set_mode((640, 480), 0, 32)
# 设置窗口标题
pygame.display.set_caption("Hello World")

# 加载并转换图像
background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(mouse_image_filename).convert_alpha()

# Clock对象
clock = pygame.time.Clock()

position = Vector2(100.0, 100.0)
heading = Vector2()

# 游戏主循环
while True:
    for event in pygame.event.get():
        # 接收到退出事件后退出程序
        if event.type == QUIT:
            exit()
    # 将背景图画上去
    screen.blit(background, (0, 0))
    screen.blit(sprite, position)

    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0

    # 参数前面加*意味着把列表或元组展开
    destination = Vector2(*pygame.mouse.get_pos()) - Vector2(*sprite.get_size()) / 2
    # 计算鱼儿当前位置到鼠标位置的向量
    vector_to_mouse = Vector2.from_points(position, destination)
    # 向量格式化
    vector_to_mouse.normalize()

    # 这个heading可以看做是鱼的速度，但由于这样的运算，鱼的速度就不断的改变了
    # 在没有到达鼠标时，加速运动，超过以后则减速。因而鱼会在鼠标附近晃动
    heading = heading + (vector_to_mouse * .6)

    position += heading * time_passed_seconds

    # 刷新一下画面
    pygame.display.update()




