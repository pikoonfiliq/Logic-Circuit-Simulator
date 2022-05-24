import pygame
pygame.init()
pygame.font.init()

#cvetove
WHITE = (255, 255, 255)
BLACK = (26, 37, 41)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BG_COLOUR = (31, 32, 34)

#rezolucii i matematikata zad resunkite na backgrounda
FPS = 60
RESOLUTIONS = [(600, 480), (1280, 720), (1920, 1080), (1920, 1200)]
RES = 2

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




#font
def get_font(size):
    return pygame.font.SysFont("comicsans", size)
