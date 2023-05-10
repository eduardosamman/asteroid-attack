"""
MNUR
Virtual Reality & Serious Games
Course 2022-2023

A message object. 

To test it run:

python3 message.py

Click any key yo make it show.
Click on ok to make it disappear.
Click any key yo make it reappear and so on.

"""
import pygame as pg

class Message(pg.sprite.Sprite):
    def __init__(self, background, pos, pos_h, box_button, font, col):
        super().__init__()
        self.font  = font
        self.col = col
        self.background = background
        self.pos_h = pos_h
        self.button = pg.Rect((box_button.left + pos[0], box_button.top + pos[1]), box_button.size)
        self.image = background.copy()
        self.rect = pg.Rect(pos, self.image.get_size())
        self.text = ""
        self.state = 'hidden'

        
    def draw(self, screen):
        if self.state != 'hidden':
            screen.blit(self.image, self.rect)
        
    def update(self, newtext):
        if newtext != self.text:
            self.text = newtext
            if newtext == '':
                self.state = 'hidden'
                self.image = self.background.copy()
            else:
                self.state = 'visible'
                self.image = self.background.copy()
                phrases = newtext.split('\n')
                for i in range(len(phrases)):
                    text_image = self.font.render(phrases[i], True, self.col)
                    dx = (self.rect.width-text_image.get_width())//2
                    self.image.blit(text_image, (dx, self.pos_h*(i+1)))

                
    def pressed(self, pos_mouse):
        if self.state != 'hidden':
            if self.button.collidepoint(pos_mouse):
                self.state = 'hidden'
                self.update('')

if __name__=='__main__':
    pg.init()
    screen = pg.display.set_mode((600, 600), pg.DOUBLEBUF)
    fontname = pg.font.get_default_font()
    fontsize = 32
    font  = pg.font.SysFont(fontname, fontsize)
    screen.fill((100, 100, 100))
    mess_image = pg.image.load("resources/images/messages.png")
    pos = (screen.get_width()- mess_image.get_width())//2, (screen.get_height()- mess_image.get_height())//2
    col = 255, 100, 255
    pos_h = 50
    box_button = pg.Rect(140, 185, 220, 55 )
    message = Message(mess_image, pos, pos_h,  box_button, font, col)
    end = False
    while not end:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                end = True
            elif event.type == pg.MOUSEBUTTONDOWN:
                pos_mouse = pg.mouse.get_pos()
                message.pressed(pos_mouse)
            elif event.type == pg.KEYDOWN:
                message.update('This is a new message \n press here \n max 3 lines')
        screen.fill((100, 100, 100))
        message.draw(screen)
        pg.display.flip()
    pg.quit()
    exit()



