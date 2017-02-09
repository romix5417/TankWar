# -*- coding: utf-8 -*-

# !/usr/bin/env python

import pygame
from pygame.locals import *
from sys import exit


class windows(object):
    def __init__(self, background_name, title="TankWar", windows_size=(640, 480)):
        pygame.init()
        self.screen = pygame.display.set_mode(windows_size, 0, 32)
        pygame.display.set_caption(title)
        self.background = pygame.image.load(background_name).convert()
        self.player = None

    def add_player(self, player):
        self.player = player

    def run(self):
        if self.player is None:
            exit()

        while True:
            for event in pygame.event.get():
                # print "key event %s", event
                if event.type == QUIT:
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        # print "key up event %s", event
                        self.player.forward()
                    if event.key == K_DOWN:
                        # print "key down event %s", event
                        self.player.backward()
                    if event.key == K_RIGHT:
                        # print "key right event %s", event
                        self.player.rightward()
                    if event.key == K_LEFT:
                        # print "key left event %s", event
                        self.player.leftward()
                    if event.key == K_SPACE:
                        self.player.fire()

            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.player.tankSurface, (self.player.x, self.player.y))
            if self.player.bullet is not None:
                self.screen.blit(self.player.bullet.bulletSurface, (self.player.bullet.x,self.player.bullet.y))

            pygame.display.update()
