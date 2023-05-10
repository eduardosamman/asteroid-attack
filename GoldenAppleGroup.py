# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 12:32:19 2023

@author: 34652
"""

import os
import pygame as pg
from random import randint, random
from goldenapple import GoldenApple

class GoldenAppleGroup(pg.sprite.Group):
    def __init__(self,path, image, box):
        super().__init__()
        self.box=box
        self.path=path
        self.image=image
        self.frames=0

                
    def update(self, group, group1,group2, group3, group4):
        #new apple generated at each frame
        self.frames=self.frames+1
        if self.frames%1000 == 0:
            self.add_new_golden()
        for a in self:
            a.update(self,group,group1)
            
    def draw(self,screen):
        for p in self:
            p.draw(screen)
            
    def add_new_golden(self):
        pos = [0,0]
        pos[0] = randint(self.image.get_width(), self.box.width-self.image.get_width())
        speed=randint(1,2)
        a=GoldenApple(self.path,pos,speed,self.box)
        if not pg.sprite.spritecollideany(a,self):
            self.add(a)
