"""
Created on Tue Mar  7 16:19:19 2023

@author: eduardo 
"""
import pygame as pg
import os

class Bucket(pg.sprite.Sprite):
    def __init__(self, image, pos, box, sound):
        """
        - image: bucket's image and its path
        - pos: [x , y] position representing the initial position of the bucket 
        - box: box representing the bounding box in which the bucket moves
        - sound: a sound with path to play
        """
        super().__init__()
        self.image = image
        self.rect  = pg.Rect(pos, image.get_size())
        self.box   = box
        self.sound = sound
    
    def draw(self, screen):

        screen.blit(self.image, self.rect.topleft)
        
    def update(self, group, goldengroup, diamond, medium, terminator):
        """
            It will update the position of the bucket and check for the collisions within the groups of other sprites present. 
        """
        mouse_pos   = pg.mouse.get_pos()
        self.rect.x = mouse_pos[ 0 ]
        if self.rect.left    < self.box.left:
            self.rect.left   = self.box.left
        elif self.rect.right > self.box.right:
            self.rect.right  = self.box.right
        lcollided  = pg.sprite.spritecollide(self, group, dokill=True)
        lcollided1 = pg.sprite.spritecollide(self, goldengroup,dokill=True)
        lcollided2 = pg.sprite.spritecollide(self, diamond, dokill=True)
        lcollided3 = pg.sprite.spritecollide(self, medium, dokill=True)
        lcollided4 = pg.sprite.spritecollide(self, terminator, dokill=True)
        return lcollided1, lcollided2
