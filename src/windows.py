# -*- coding: utf-8 -*-

# !/usr/bin/env python

import pygame
from pygame.locals import *
from sys import exit


class windows():
    def __init__(self, background_name, title="TankWar", windows_size=(640, 480)):
        self.background = background_name
        pygame.init()
        self.screen = pygame.display.set_mode(windows_size, 0, 32)
        pygame.display.set_caption(title)
        self.background = pygame.image.load(background_name).convert()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
            self.screen.blit(self.background, (0, 0))
