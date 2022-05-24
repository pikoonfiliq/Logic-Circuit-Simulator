import pygame
pygame.init()
pygame.font.init()

WHITE = (255 , 255 , 255)
BLACK = (26, 37, 41)
RED = (255 , 0 , 0)
GREEN = (0 , 255 , 0)
BLUE = (0 , 0 , 255)
ORANGE = (198, 75, 25)
FPS = 60


RESOLUTIONS = [(600 , 480),(1280 , 720),(1920 , 1080),(1920 , 1200)]

RES = 2

WIDTH , HEIGHT = RESOLUTIONS[RES]

USABEL_WIDTH , USABLE_HEIGHT = WIDTH - 20 , WIDTH - 20

ROWS = COLUMS = 100

TOOLBAR_HIGHT = USABLE_HEIGHT - USABEL_WIDTH

PIXEL_SIZE = USABEL_WIDTH // COLUMS

BG_COLOUR = BLACK

DRAW_GRID_LINES = True

def get_font(size):
    return pygame.font.SysFont("comicsans", size)