"""
Created on Tue Mar  23 18:29:59 2023

@author: eduardo 
"""

import pygame as pg

class Pause:
    """Class that displays a 'PAUSED' message on the screen until the user presses the space bar.

    """

    def __init__(self, screen_size):
        """
        Initializes a pause class.

        """
        self.screen_size = screen_size
        pg.init()
        self.screen = pg.display.set_mode(screen_size)

    def pause(self):
        """
        Pauses the game and displays a 'PAUSED' message on the screen until the user presses the space bar.

        """
        paused_state = True
        font = pg.font.Font(None, 50)
        text = font.render("PAUSED", True, (255, 255, 255)) # white text 'PAUSE'
        text_rect = text.get_rect(center=(self.screen_size[0]//2, self.screen_size[1]//2))
        while paused_state:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()
                elif event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    paused_state = False
            self.screen.fill((0, 0, 0))  # black screen
            self.screen.blit(text, text_rect)
            pg.display.flip() #update the screeen and make it black