import pygame as pg
import os


class Bird(pg.sprite.Sprite):
    """
    A class representing
    """

    def __init__(self, path, pos, speed):
        super().__init__()
        self.speed = speed
        self.curframe = 0
        self.path=path
        self.time = 0
        self.nframes = 6
        self.image = os.listdir(self.path+'/bird')
        self.set_bird()
        self.rect = pg.Rect(pos, self.image[0].get_size())
        self.width = self.image[0].get_width()
        self.cell = pg.Rect((0, 0), (self.width, self.image[0].get_height()))
        self.jump=0
        self.cooldown=30
        self.last_update=pg.time.get_ticks()
    
    def set_bird(self):
        for i in range(len(self.image)):
            self.image[i]=self.path +'/bird/'+self.image[i]
            self.image[i]=pg.image.load(self.image[i]) 
    
    def update_animation(self):
        self.time=pg.time.get_ticks()
        if self.time - self.last_update >= self.cooldown:
            self.curframe +=1
            self.last_update=self.time
            if self.curframe>=len(self.image):
                self.curframe=0
        
    def update(self,group,group1,group2,group3,group4):
        self.rect.left = self.rect.left + self.speed
        lcollided=pg.sprite.spritecollide(self, group, dokill=True)
        lcollided2=pg.sprite.spritecollide(self, group3, dokill=True)

    def draw(self, screen):
        screen.blit(self.image[self.curframe], self.rect, self.cell)
        self.update_animation()
