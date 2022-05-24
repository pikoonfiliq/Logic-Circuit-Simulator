import struct

from pygame.mouse import get_rel, get_pressed
from pygame.gfxdraw import filled_circle


all_blocks = []
all_wires = []

block_color = (0, 102, 255)
wire_color_0 = (25, 77, 0)
wire_color_1 = (255, 51, 0)

class wire:
    def __init__(self, start, end, entr, d, e):
        self.start = start
        self.end = end
        self.genre = entr
        
class OR:
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
        filled_circle(screen, self.x, self.y, 20, block_color)