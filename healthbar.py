# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 22:05:47 2023

@author: isaac
"""

import pygame

class HealthBar(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.current_health = 0
		self.target_health = 100
		self.max_health = 100
		self.health_bar_length = 400
		self.health_ratio = self.max_health / self.health_bar_length
		self.health_change_speed = 3

	def get_damage(self,hit):
		if self.target_health > 0:
			self.target_health -= hit
		if self.target_health < 0:
			self.target_health = 0

	def get_health(self,heal):
		if self.target_health < self.max_health:
			self.target_health += heal
		if self.target_health > self.max_health:
			self.target_health = self.max_health

	def update(self,screen):
		self.draw_health(screen)
		
	def draw_health(self,screen):
		transition_width = 0
		transition_color = (255,255,0)

		if self.current_health < self.target_health:
			self.current_health += self.health_change_speed
			transition_width = int((self.target_health - self.current_health) / self.health_ratio)
			transition_color = (0,0,0)

		if self.current_health > self.target_health:
			self.current_health -= self.health_change_speed 
			transition_width = int((self.target_health - self.current_health) / self.health_ratio)
			transition_color = (255,0,0)

		health_bar_width = int(self.current_health / self.health_ratio)
		health_bar = pygame.Rect(10,10,health_bar_width,25)
		transition_bar = pygame.Rect(health_bar.right,10,transition_width,25)
		
		pygame.draw.rect(screen,(0,255,0),health_bar)
		pygame.draw.rect(screen,transition_color,transition_bar)	
		pygame.draw.rect(screen,(255,255,255),(10,10,self.health_bar_length,25),4)	



