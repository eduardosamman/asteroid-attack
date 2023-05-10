#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 15:21:05 2023

@author: marc.borras.sanchez
"""

import os
import pygame as pg
from apples import Apple
from random import randint, random

class AppleGroup(pg.sprite.Group):
    def __init__(self, path, image, box):
        super().__init__()
        self.box=box
        self.path=path
        self.image=image
        self.frames=0
        
    def update(self, group, group1,group2, group3, group4):
        #new apple generated at each frame
        self.frames=self.frames+1
        if self.frames%30 == 0:
            self.add_new()
        for a in self:
            a.update(self, group1,group2)

    def draw(self,screen):
        for p in self:
            p.draw(screen)

            
    def add_new(self):
        pos = [0,0]
        pos[0] = randint(self.image.get_width(), self.box.width-self.image.get_width())
        speed=randint(1,6)
        a=Apple(self.path,pos,speed,self.box)
        if not pg.sprite.spritecollideany(a,self):
            self.add(a)

