# -*- coding: utf-8 -*-

import pygame
from ai import *

background_image_name = '../res/background.png'
tank_forward_image_path = '../res/tank_forward.png'
tank_backward_image_path = '../res/tank_backward.png'
tank_leftward_image_path = '../res/tank_leftward.png'
tank_rightward_image_path = '../res/tank_rightward.png'
bullet_image_path = '../res/bullet.png'
bullet_boom_image_path = '../res/bullet_boom.png'

class bullet(object):
    def __init__(self, speed=16, might=1, player=None, state='Ready', direction='forward'):
        self.direction = direction
        self.speed = speed
        self.might = might
        self.owner = player
        self.x = self.owner.x
        self.y = self.owner.y
        self.state = state
        self.bulletSurface = pygame.image.load(bullet_image_path).convert()
        self.direction = direction
        self.set_location()

    def set_location(self):
        if self.direction == "forward":
            if self.y >= 0:
                self.y -= 8
                self.x = self.owner.x + (16 - 8/2)
            else:
                pass
        elif self.direction == "backward":
            if self.y < 448:
                self.y += 32
                self.x = self.owner.x + (16 - 8/2)
        elif self.direction == "rightward":
            if self.x < 608:
                self.x += 32
                self.y = self.owner.y + (16 - 8/2)
        else:
            if self.x >= 0:
                self.x -= 8
                self.y = self.owner.y + (16 - 8/2)

    def location_update(self):
        if self.direction == "forward":
            if self.y > 32:
                self.y -= 32
                self.x = self.owner.x + (16 - 8/2)
            else:
                pass
        elif self.direction == "backward":
            if self.y < 608:
                self.y += 32
                self.x = self.owner.x + (16 - 8/2)
        elif self.direction == "rightward":
            if self.x < 448:
                self.x += 32
                self.y = self.owner.y + (16 - 8/2)
        else:
            if self.x > 32:
                self.x -= 32
                self.y = self.owner.y + (16 - 8/2)


class Tank(object):
    def __init__(self, tankType='ai', x=0, y=0):
        self.tankType = tankType
        self.curDirection = 'forward'
        self.x = x
        self.y = y
        self.tankSurface = pygame.image.load(tank_forward_image_path).convert()
        self.scores = 0
        self.bullet = None

    def set_location(self, x, y):
        self.x = x
        self.y = y

    def forward(self):
        if self.curDirection != 'forward':
            self.tankSurface = pygame.image.load(tank_forward_image_path).convert()
            self.curDirection = 'forward'
        else:
            if self.y >= 16:
                self.y -= 16

    def backward(self):
        if self.curDirection != 'backward':
            self.tankSurface = pygame.image.load(tank_backward_image_path).convert()
            self.curDirection = 'backward'
        else:
            if self.y < 448:
                self.y += 16

    def rightward(self):
        if self.curDirection != 'rightward':
            self.tankSurface = pygame.image.load(tank_rightward_image_path).convert()
            self.curDirection = 'rightward'
        else:
            if self.x < 608:
                self.x += 16

    def leftward(self):
        if self.curDirection != 'leftward':
            self.tankSurface = pygame.image.load(tank_leftward_image_path).convert()
            self.curDirection = 'leftward'
        else:
            if self.x > 0:
                self.x -= 16

    def fire(self):
        self.bullet = bullet(speed=16, might=1, player=self, state='fire', direction=self.curDirection)


class aitank(Tank, ai):
    def __init__(self):
        pass