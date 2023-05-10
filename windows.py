"""
Created on Tue Mar  23 18:29:59 2023

@author: eduardo 
"""

import cv2
import numpy as np
import os
import pygame as pg


class LoadingWindow:
    def __init__(self, screen):
        """
        initialize the LoadingWindow class to observe the acardia entreprise initiation screen
        """
        pg.init()
        fontpath = pg.font.get_default_font()
        size = 48
        self.font = pg.font.Font(fontpath,size)
        self.screen = screen
        self.sound = pg.mixer.Sound('resources/sound/Power-Up-KP-1879176533.wav') #change to path (not hardcoded))

    def show(self):
        loading_text = self.font.render('ARCADIA ENTERPRISE', True, (255, 255, 255))
        loading_text_rect = loading_text.get_rect(center=self.screen.get_rect().center)

        self.screen.fill((0, 0, 0))

        self.screen.blit(loading_text, loading_text_rect)
        pg.display.flip()

        # play sound, mixer has to be initialized
        pg.mixer.init()
        self.sound.play()

        clock = pg.time.Clock()
        elapsed_time = 0
        while elapsed_time < 4000:
            self.screen.fill((0, 0, 0))
            self.screen.blit(loading_text, loading_text_rect)
            pg.display.flip()
            clock.tick(50)
            elapsed_time += clock.get_time()
            if elapsed_time>= 4000:
                break
        pg.time.wait(2000)

class StartScreen:

    def __init__(self, screen_size):

        self.path = 'resources/images'
        self.backimage_filenames = os.listdir(self.path + '/backg3')
        self.backimages = []
        for filename in self.backimage_filenames:
            image = pg.image.load(self.path + '/backg3/' + filename)
            image = pg.transform.scale(image, screen_size)
            self.backimages.append(image)

        self.screen = pg.display.set_mode(screen_size)
        self.image_index = 0

        self.start_screen_ima = pg.image.load('resources/images/text_1.png')
        self.start_screen_ima = pg.transform.scale(self.start_screen_ima, (int(screen_size[0]*0.5), int(screen_size[1]*0.3)))
        self.start_screen_ima_rect = self.start_screen_ima.get_rect(center=(self.screen.get_width()//2, self.screen.get_height()-570))

        self.font = pg.font.SysFont("Arial", 50)
        self.text = self.font.render("Press SPACE BAR to begin", True, (255, 255, 255))
        self.text_rect = self.text.get_rect(center=(self.screen.get_width()//2, self.screen.get_height()-40))
        
        self.show_text = True
        self.time2 = pg.time.get_ticks()
        self.update_time = pg.time.get_ticks() 
        self.transition_time = 100   
    
    def run(self):
        running = True
        pg.mixer.init()
        sound = pg.mixer.Sound('resources/sound/alien-spaceship_daniel_simion.wav')
        sound.play()
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    running = False

            current_time = pg.time.get_ticks()
            if current_time - self.time2 > 500:
                self.show_text = not self.show_text
                self.time2 = current_time

            if current_time - self.update_time > self.transition_time:
                self.image_index = (self.image_index + 1) % len(self.backimages)
                self.update_time = current_time


            self.screen.blit(self.backimages[self.image_index], (0, 0))
            
            self.screen.blit(self.start_screen_ima, self.start_screen_ima_rect)

            box_size = [830, 410]
            box_color = (128, 128, 128)
            box_transparency = 200 #the value goes from low to high transparency
            box_rect = pg.Rect((self.screen.get_width() - box_size[0]) // 2, (self.screen.get_height() - box_size[1]) // 1.5, box_size[0], box_size[1])
            box_surface = pg.Surface((box_size[0], box_size[1]), pg.SRCALPHA)
            box_surface.fill((box_color[0], box_color[1], box_color[2], box_transparency))
            self.screen.blit(box_surface, box_rect)

            # Draw the text inside the box
            text_font = pg.font.SysFont("Helvetica", 20, bold=True)
            text_color = (0, 0, 0)
            text_start = [
                "Welcome to the game of ASTEROID ATTACK, where you must defend your spaceship from incoming",
                "danger! Your mission is to move the SHIELD with your mouse and protect the ship's rear from three",
                "types of enemies: BLUE ASTEROIDS (-1 HP), GREEN ORBs (Kills Monsters), DARK ORBs (- MAX HP)", 
                "       ", "The GOAL is to destroy as many asteroids as possible","       ",
                "Along the way, you'll encounter POWER-UPS to help you in your quest. The SPACE MONSTER which",
                "you can summon by pressing the B key, and the ENERGY BALL, which you can activate with the C key.",
                "And if you're lucky, you might even find a BLUE ORB that gives you more SPACE MONSTER summons",
                "or an ENERGY ROCK that boosts your health.",
                "   ",
                "So what are you waiting for? Let's protect that spaceship and save the day! Move that",
                "mouse and get ready for some asteroid-blasting action!"
            ]
            text_rects =[]
            for i, text in enumerate(text_start):
                text_render = text_font.render(text, True, text_color)
                text_rect = text_render.get_rect(topleft=(box_rect.x+20, box_rect.y+14 + i * 30))
                text_rects.append(text_rect)
                self.screen.blit(text_render, text_rect)
            if self.show_text:
                self.screen.blit(self.text, self.text_rect)
            pg.display.flip()


        pg.quit()

class GameOverWindow:
    def __init__(self, screen_size):
        self.path = 'resources/images'
        self.backimage_filenames = os.listdir(self.path + '/backg4')
        self.backimages = []
        for filename in self.backimage_filenames:
            image = pg.image.load(self.path + '/backg4/' + filename)
            image = pg.transform.scale(image, screen_size)
            self.backimages.append(image)
        self.screen = pg.display.set_mode(screen_size)
        self.image_index = 0

        self.show_text = True
        self.time2 = pg.time.get_ticks()
        self.update_time = pg.time.get_ticks()
        self.transition_time = 100  # Change this to adjust the time between image updates. El 100 va bien. 
        
        self.font = pg.font.SysFont('Arial', 50)
        self.game_over_text = self.font.render('GAME OVER', True, (255, 255, 255))
        self.game_over_rect = self.game_over_text.get_rect(center=(screen_size[0] // 2, screen_size[1] // 2))

    def run2(self):
        running = True
        pg.mixer.init()
        sound = pg.mixer.Sound('resources/sound/alien-spaceship_daniel_simion.wav')
        sound.play()
        while running:
            current_time = pg.time.get_ticks()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
            # Update the background gifs
            if current_time - self.update_time > self.transition_time:
                self.image_index = (self.image_index + 1) % len(self.backimages)
                self.update_time = current_time
            self.screen.blit(self.backimages[self.image_index], (0, 0))
            if self.show_text:
                self.screen.blit(self.game_over_text, self.game_over_rect)
            pg.display.flip()
        pg.quit()


class VideoWindow:
    def __init__(self, screen):

        self.screen = screen
        self.font = pg.font.Font(None, 36)
        self.skip_text = self.font.render("Press 's' to skip storyline", True, (255, 255, 255))
        self.skip_rect = self.skip_text.get_rect(left=10, top=10)
        self.clock = pg.time.Clock()

        self.skip_timer = 0
        self.skip_interval = 2000

        self.video_path = os.path.join("resources", "videos", "video_intro.mov")
        self.cap = None
        self.sound_played = False
        self.sound = None
        self.start_time = 5000 # 5 seconds, as the video was shortened. 

    def play_video(self):
        
        pg.init()
        self.cap = cv2.VideoCapture(self.video_path)
        while self.cap.isOpened():
            ret, frame = self.cap.read()

            if ret:
                
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = np.rot90(np.flipud(frame), k=1, axes=(1,0))

                frame =pg.surfarray.make_surface(frame)
                self.screen.blit(frame, (self.screen.get_width()//2- frame.get_width()//2, self.screen.get_height()//2 - frame.get_height()//2))

                # the video goes very fast of not, problem with framerate, that not matching
                pg.time.wait(3)

                self.skip_timer += self.clock.tick()
                if self.skip_timer>=self.skip_interval:
                    self.screen.blit(self.skip_text, self.skip_rect)

                pg.display.flip() # to update

                if not self.sound_played:
                    pg.mixer.init()
                    self.sound = pg.mixer.Sound('resources/sound/video_intro_sound.wav')
                    self.sound.play(self.start_time)
                    self.sound_played = True
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        self.cap.release()
                        self.sound.stop()
                        pg.quit()
                        exit()
                    elif event.type == pg.KEYDOWN and event.key == pg.K_s:
                        self.sound.stop()
                        self.cap.release()
                        return

            else:

                self.sound.stop()
                self.cap.release()
                return
            
    
# https://stackoverflow.com/questions/21356439/how-to-load-and-play-a-video-in-pygame
