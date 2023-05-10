"""
MNUR Course 2022-2023

Class apple
"""

import pygame as pg
import os

class Apple(pg.sprite.Sprite):
    def __init__(self, path, pos, speed, box):
        super().__init__()
        self.path=path
        self.image = os.listdir(self.path+'/apple')
        self.time = 0
        self.cooldown=18
        self.last_update=pg.time.get_ticks()
        self.curframe=0
        self.frames=0
        self.set_apple()
        self.rect = pg.Rect(pos, self.image[0].get_size())
        self.box = box
        self.speed = speed
        self.state = 'falling'

    def set_apple(self):
         for i in range(len(self.image)):
             self.image[i]=self.path +'/apple/'+self.image[i]
             self.image[i]=pg.image.load(self.image[i])
      
    def update_animation(self):
         self.time=pg.time.get_ticks()
         if self.time - self.last_update >= self.cooldown:
             self.curframe +=1
             self.last_update=self.time
             if self.curframe>=len(self.image):
                 self.curframe=0
                 
    def draw(self, screen):
        screen.blit(self.image[self.curframe], self.rect.topleft)
        self.update_animation()

    def update(self, group, group1,group2):
        if self.state=='falling':
            self.rect.top=self.rect.top+self.speed
            if self.rect.bottom>self.box.bottom+self.speed+1:
                self.kill()

                