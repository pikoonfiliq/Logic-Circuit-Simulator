import struct

from pygame.mouse import get_rel, get_pressed
from pygame.gfxdraw import filled_circle
from pygame.draw import rect, line


block_size = 30

all_blocks = []
all_wires = []

block_color = (0, 102, 255)
wire_color_0 = (25, 77, 0)
wire_color_1 = (255, 51, 0)

class wire:
    def __init__(self, screen, beg_w, beg_h, end_w, end_h, state):
        self.beg_w =beg_w
        self.beg_h = beg_h
        self.end_w = end_w
        self.end_h = end_h
        self.state = state
        self.screen = screen
        all_wires.append(self)
    def draw(self):
        line(self.screen , wire_color_0 if self.state == 0 else wire_color_1 , (self.beg_w , self.beg_h),(self.end_w , self.end_h) , 3)
        
class AND:
    def __init__(self, x=500, y=500):
        self.x = x
        self.y = y
        self.wire = []
        all_blocks.append(self)
    def move(self):
        while get_pressed():
            self.x += get_rel()[0]
            self.y += get_rel()[1]
    def draw(self, screen):
        rect(screen, block_color, (self.x - block_size*2, self.y - block_size, block_size * 2, block_size * 2))
        filled_circle(screen, self.x, self.y, block_size, block_color)