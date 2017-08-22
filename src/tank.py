# -*- coding: utf-8 -*-

import pygame
from ai import *

background_image_name = '../res/background.png'
tank_forward_image_path = '../res/tank_forward.png'
tank_backward_image_path = '../res/tank_backward.png'
tank_leftward_image_path = '../res/tank_leftward.png'
tank_rightward_image_path = '../res/tank_rightward.png'

ai_tank_forward_image_path = '../res/ai_tank_forward.png'
ai_tank_backward_image_path = '../res/ai_tank_backward.png'
ai_tank_leftward_image_path = '../res/ai_tank_leftward.png'
ai_tank_rightward_image_path = '../res/ai_tank_rightward.png'

bullet_image_path = '../res/bullet.png'
bullet_boom_image_path = '../res/bullet_boom.png'

class bullet(object):
    def __init__(self, speed=16, might=1, player=None, magazine=None, state='Ready', direction='forward'):
        self.direction = direction
        self.speed = speed
        self.might = might
        self.owner = player
        self.magazine = magazine
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
            if self.y <= 448:
                self.y += 32
                self.x = self.owner.x + (16 - 8/2)
        elif self.direction == "rightward":
            if self.x <= 608:
                self.x += 32
                self.y = self.owner.y + (16 - 8/2)
        else:
            if self.x >= 0:
                self.x -= 8
                self.y = self.owner.y + (16 - 8/2)

    def location_update(self):
        if self.direction == "forward":
            if self.y >= 8:
                self.y -= 32
            else:
                if self.magazine == 1:
                    self.owner.bullet1 = None
                if self.magazine == 2:
                    self.owner.bullet2 = None
                if self.magazine == 3:
                    self.owner.bullet3 = None
        elif self.direction == "backward":
            if self.y < 480:
                self.y += 32
            else:
                if self.magazine == 1:
                    self.owner.bullet1 = None
                if self.magazine == 2:
                    self.owner.bullet2 = None
                if self.magazine == 3:
                    self.owner.bullet3 = None
        elif self.direction == "rightward":
            if self.x < 640:
                self.x += 32
            else:
                if self.magazine == 1:
                    self.owner.bullet1 = None
                if self.magazine == 2:
                    self.owner.bullet2 = None
                if self.magazine == 3:
                    self.owner.bullet3 = None
        else:
            if self.x >= 8:
                self.x -= 32
            else:
                if self.magazine == 1:
                    self.owner.bullet1 = None
                if self.magazine == 2:
                    self.owner.bullet2 = None
                if self.magazine == 3:
                    self.owner.bullet3 = None


class Tank(object):
    def __init__(self, tanktype='ai', x=0, y=0, number=0):
        self.tankType = tanktype
        self.curDirection = 'forward'
        self.x = x
        self.y = y

        self.tankSurface = pygame.image.load(tank_forward_image_path).convert()

        self.scores = 0
        self.bullet1 = None
        self.bullet2 = None
        self.bullet3 = None
        self.number = number

    def set_location(self, x, y):
        self.x = x
        self.y = y

    def change_surface(self, surface):
        self.tankSurface = pygame.image.load(ai_tank_forward_image_path).convert()

    def forward(self):
        if self.curDirection != 'forward':
            if self.tankType == "ai":
                self.tankSurface = pygame.image.load(ai_tank_backward_image_path).convert()
            else:
                self.tankSurface = pygame.image.load(tank_forward_image_path).convert()
            self.curDirection = 'forward'
        else:
            if self.y >= 16:
                self.y -= 16

    def backward(self):
        if self.curDirection != 'backward':
            if self.tankType == "ai":
                self.tankSurface = pygame.image.load(ai_tank_backward_image_path).convert()
            else:
                self.tankSurface = pygame.image.load(tank_backward_image_path).convert()
            self.curDirection = 'backward'
        else:
            if self.y < 448:
                self.y += 16

    def rightward(self):
        if self.curDirection != 'rightward':
            if self.tankType == "ai":
                self.tankSurface = pygame.image.load(ai_tank_rightward_image_path).convert()
            else:
                self.tankSurface = pygame.image.load(tank_rightward_image_path).convert()
            self.curDirection = 'rightward'
        else:
            if self.x < 608:
                self.x += 16

    def leftward(self):
        if self.curDirection != 'leftward':
            if self.tankType == "ai":
                self.tankSurface = pygame.image.load(ai_tank_leftward_image_path).convert()
            else:
                self.tankSurface = pygame.image.load(tank_leftward_image_path).convert()
            self.curDirection = 'leftward'
        else:
            if self.x > 0:
                self.x -= 16

    def fire(self):
        if self.bullet1 is None:
            self.bullet1 = bullet(speed=16, might=1, player=self, magazine=1, state='fire', direction=self.curDirection)
            return
        if self.bullet2 is None:
            self.bullet2 = bullet(speed=16, might=1, player=self, magazine=2, state='fire', direction=self.curDirection)
            return
        if self.bullet3 is None:
            self.bullet3 = bullet(speed=16, might=1, player=self, magazine=3, state='fire', direction=self.curDirection)
            return



class aitank(Tank, ai):
    def __init__(self, tanktype="ai", x=0, y=0, number=0):
        Tank.__init__(self, tanktype, x, y, number)
        self.change_surface(ai_tank_forward_image_path)
    def change_surface(self, surface):
        Tank.change_surface(self, surface)
