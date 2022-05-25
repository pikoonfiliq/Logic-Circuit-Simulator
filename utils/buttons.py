from .settings import *
import struct

from pygame.mouse import get_rel, get_pressed
from pygame.gfxdraw import filled_circle
from pygame.draw import rect, line

x = bm_x_h / 2
all_buttons = []

class Button:
    def __init__(self,screen,number,clr,text):
        self.num = number
        self.clr = clr
        self.txt = text
        self.screen = screen
        all_buttons.append(self)
    def get_pos(self,mouse_x,mouse_y):

        BLOCK_START_W = BLOCKMENU_START_W + x*self.num+((BLOCKMENU_WIDTH-11*x)/10)*(self.num-1)
        BLOCK_START_H = BLOCKMENU_START_H  + x

        BLOCK_W = ((BLOCKMENU_WIDTH-11*x)/10)
        BLOCK_H = x*2

        if BLOCK_START_W <mouse_x and (BLOCK_START_W + BLOCK_W) > mouse_x:
            if BLOCK_START_H <mouse_y and (BLOCK_START_H + BLOCK_H) > mouse_y:
                return True
        
        return False
        
    def draw(self):
        my_font = get_font(int(x*2))
        text_surface = my_font.render(self.txt, False, (0, 0, 0))

        BLOCK_START_W = BLOCKMENU_START_W + x*self.num+((BLOCKMENU_WIDTH-11*x)/10)*(self.num-1)
        BLOCK_START_H = BLOCKMENU_START_H  + x
        mid_w = ((((BLOCKMENU_WIDTH-11*x)/10)- text_surface.get_size()[0])/2)
        mid_h = ((x*2- text_surface.get_size()[1])/2)

        rect(self.screen , self.clr,(BLOCK_START_W,BLOCK_START_H, ((BLOCKMENU_WIDTH-11*x)/10),x*2))
        self.screen.blit(text_surface, (BLOCK_START_W + mid_w,BLOCK_START_H  +mid_h))
