# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 16:29:46 2023

@author: mborr
"""

import os
import pygame as pg
from apples import Apple
from random import randint, random
from diamond import Diamond

class DiamondGroup(pg.sprite.Group):
    def __init__(self, path,image, box):
        super().__init__()
        self.box=box
        self.path=path
        self.image=image
        self.frames=0
        
    def update(self, group, group1, group2, group3, group4):
        #new apple generated at each frame
        self.frames=self.frames+1
        if self.frames%1900 == 0:
            self.add_new_golden()
        for a in self:
            a.update(self,group,group2)
            
    def draw(self,screen):
        for p in self:
            p.draw(screen)
            
    def add_new_golden(self):
        pos = [0,0]
        pos[0] = randint(self.image.get_width(), self.box.width-self.image.get_width())
        speed=randint(1,2)
        a=Diamond(self.path,pos,speed,self.box)
        if not pg.sprite.spritecollideany(a,self):
            self.add(a)
