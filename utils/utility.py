from pygame.draw import line
import pygame
from .User_settings import *

#HERE ARE CONSTANT VARIABLES THAT ARE USED FOR VARIOUS STUFF

NAME = "Logic Circuit Simulator"
#variables used for drawing based on the resolution chosen by the user
FPS = 60
WIDTH, HEIGHT = RESOLUTIONS[RES]
# ------------------------------------------------------
WORKSPACE_WIDTH, WORKSPACE_HEIGHT = WIDTH * 0.9, HEIGHT * 0.8
x_w, x_h = (WIDTH - WORKSPACE_WIDTH) / 4, (HEIGHT * 0.1) / 4
WORKSPACE_START_W, WORKSPACE_START_H = x_w * 2, x_h * 2

FILEMENU_START_W, FILEMENU_START_H = 0, 0
FILEMENU_WIDTH, FILEMENU_HEIGHT = WIDTH, x_h
bm_x_h = (HEIGHT - (WORKSPACE_HEIGHT + WORKSPACE_START_H)) / 4
BLOCKMENU_START_W, BLOCKMENU_START_H = x_w, WORKSPACE_HEIGHT + WORKSPACE_START_H + bm_x_h
BLOCKMENU_WIDTH, BLOCKMENU_HEIGHT = WIDTH - 2*x_w, bm_x_h * 2
# ------------------------------------------------------

x = bm_x_h / 2

block_size = WIDTH / 64
dot_size = block_size/5


all_blocks = []
all_wires = []
all_buttons = []
all_border_dots = []
all_border_end_dots = []


#HERE ARE FUNCTIONS FOR DRAWING AND MISC. FUNCTIONS
def get_font(size):
    return pygame.font.SysFont(FONTS[FONT], size)

#deletes the lines connected to the block we deleted
def snap(block):
    for x in block.wires:
        if x == None:
            pass
        else:
            ind = all_wires.index(x)
            del all_wires[ind]
#draws background
def background_draw(win):
    win.fill(BG_COLOUR)
    pygame.draw.rect(win , (55,57,61) , (WORKSPACE_START_W,WORKSPACE_START_H , WORKSPACE_WIDTH,WORKSPACE_HEIGHT) , 5)
    pygame.draw.rect(win , (55,57,61) , (BLOCKMENU_START_W,BLOCKMENU_START_H , BLOCKMENU_WIDTH,BLOCKMENU_HEIGHT) , 5)
    pygame.draw.rect(win , (55,57,61) , (FILEMENU_START_W,FILEMENU_START_H , FILEMENU_WIDTH,FILEMENU_HEIGHT))
    my_font = get_font(int(x))
    text_surface = my_font.render(NAME, False, (0, 0, 0))
    f_mid_w = ((FILEMENU_WIDTH - text_surface.get_size()[0] )/2)
    win.blit(text_surface, (f_mid_w,0))
    
#main function to draw background and entities
def draw(win, temp_lines=None):
    background_draw(win)
    for block in all_blocks:
        block.draw(win)
    for wire in all_wires:
        wire.draw()
    if temp_lines:
        for el in temp_lines:
            line(win, WHITE, el[0], el[1], int(WIDTH / 640))
    for button in all_buttons:
        button.draw()
    for dot in all_border_dots:
        dot.draw(win)
    for dot in all_border_end_dots:
        dot.draw(win)
    pygame.display.update()


