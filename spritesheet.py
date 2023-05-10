# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 10:44:29 2023

@author: isaac
"""

import pygame as pg

class SpriteSheet():
	def __init__(self, image):
		self.sheet = image

	def get_image(self, frame,jump, width, height, colour):
		image = pg.Surface((width, height)).convert_alpha()
		image.blit(self.sheet, (0, 0), (frame * width,jump*height, width, height))
		image.set_colorkey(colour)
		return image
    

    
