"""
MNUR
Virtual Reality & Serious Games
Course 2022-2023

Example 1 of pygame
Birds life

"""

import os
import pygame as pg
from pygame.locals import *
from scenes import Scene
from windows import LoadingWindow, VideoWindow, StartScreen, GameOverWindow
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from pause import Pause

pg.init()
   
def main_loop(scene):
    clock = pg.time.Clock()
    end = False

    mouse_positions = []

    screen_size = (1280, 640)
    pause1 = Pause(screen_size)

    background_music = pg.mixer.Sound("resources/sound/smashbrawl.mp3")
    background_music.play()

    gameover = GameOverWindow(screen_size)

    while not end:
        frame_time = clock.tick(100)
        # print(pg.time.get_ticks())
        scene.update()
        
        x, y = pg.mouse.get_pos()
        mouse_positions.append((x, y))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                df = pd.DataFrame(mouse_positions, columns=["x", "y"])
                df.to_csv("mouse_positions.csv", index=False)
                end = True
            if event.type == pg.KEYDOWN:
                scene.activate(event.key)
                scene.spawn_cat(event.key)
                scene.spawn_bird(event.key)
            if event.type == pg.KEYUP:
                scene.stop()
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                pause1.pause()

        scene.draw()

        # Bar reaches 0, the game is over
        if scene.healthbar.current_health <= 0:
            background_music.stop()
            gameover.run2()
            end = True
            df = pd.DataFrame(mouse_positions, columns=["x", "y"])
            df.to_csv("mouse_positions.csv", index=False)
            df = pd.read_csv("mouse_positions.csv")
            x = df["x"]
            y = df["y"]
            frames = np.arange(len(x))

            fig = plt.figure(figsize = (10, 6))
            ax = fig.add_subplot(projection = '3d')
            ax.plot(x, y, frames, 'k-', linewidth = 4)
            ax.invert_yaxis()
            ax.set_xlabel('X Position (px.)')
            ax.set_ylabel('Y Position (px.)')
            ax.set_zlabel('Frames')
            ax.set_title('Asteroid Attack GAME Mouse Trajectory')
            plt.show()
            
        pg.display.flip()
        
    background_music.stop()

    # Read excel file... and plot stuff
    df = pd.read_csv("mouse_positions.csv")
    x = df["x"]
    y = df["y"]
    frames = np.arange(len(x))

    fig = plt.figure(figsize = (10, 6))
    ax = fig.add_subplot(projection = '3d')
    ax.plot(x, y, frames, 'k-', linewidth = 4)
    ax.invert_yaxis()
    ax.set_xlabel('X Position (px.)')
    ax.set_ylabel('Y Position (px.)')
    ax.set_zlabel('Frames')
    ax.set_title('Asteroid Attack GAME Mouse Trajectory')
    plt.show()

if __name__ == "__main__":
    screen_size = (1280, 640)
    scene= Scene('resources/images')

    screen = pg.display.set_mode(screen_size)

    loading_window = LoadingWindow(screen)
    loading_window.show()

    video_window = VideoWindow(screen)
    video_window.play_video()


    start_screen = StartScreen(screen_size)
    start_screen.run()

    scene = Scene(os.getcwd() + '/resources/images')

    main_loop(scene)

    pg.quit()
    
