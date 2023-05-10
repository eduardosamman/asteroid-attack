# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 16:06:16 2023

@author: mborr
"""

import pygame as pg
import os

class Cat(pg.sprite.Sprite):
    def __init__(self,path,pos,speed,box, spawntime):
        super().__init__()
        self.path=path
        self.speed = speed
        self.curframe = 0
        self.time = 0
        self.image=os.listdir(self.path+'/cat_rot')
        self.set_cat()
        self.rect = pg.Rect(pos, self.image[0].get_size())
        self.width = self.image[0].get_width()
        self.cell = pg.Rect((0, 0), (self.width, self.image[0].get_height()))
        self.box=box
        self.cooldown=90
        self.last_update=pg.time.get_ticks()
        self.spawntime=spawntime
          
    def set_cat(self):
        for i in range(len(self.image)):
            self.image[i]=self.path +'/cat_rot/'+self.image[i]
            self.image[i]=pg.image.load(self.image[i]) 
            
    def update_animation(self):
        self.time=pg.time.get_ticks()
        if self.time - self.last_update >= self.cooldown:
            self.curframe +=1
            self.last_update=self.time
            if self.curframe>=len(self.image):
                self.curframe=0
        
    def draw(self,screen):
        screen.blit(self.image[self.curframe],self.rect)
        self.update_animation()
        
    def update(self,group,group1,group2,group3,group4):
        self.rect.right = self.rect.right  + self.speed
        self.check_boundaries()
        lcollided=pg.sprite.spritecollide(self, group, dokill=True)
        lcollided1=pg.sprite.spritecollide(self, group3, dokill=False)
        lcollided2=pg.sprite.spritecollide(self, group4, dokill=False)
        return lcollided1, lcollided2
        #print(pg.time.get_ticks()-self.spawntime)

    
    def check_boundaries(self):
        if self.rect.right >self.box.right:
            self.rect.right=self.box.right
            for image in range(len(self.image)):
                self.image[image]= pg.transform.flip(self.image[image], True, False).convert_alpha()
            self.speed=-self.speed
        if self.rect.left<self.box.left:
            self.rect.left=self.box.left
            for image in range(len(self.image)):
                self.image[image]= pg.transform.flip(self.image[image], True, False).convert_alpha()
            self.speed=-self.speed
            