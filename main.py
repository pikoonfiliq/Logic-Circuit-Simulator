from ast import With
from pickle import TRUE
from xml.etree.ElementTree import PI
from screeninfo import get_monitors

from numpy import full
from utils import *




WIN = pygame.display.set_mode(RESOLUTIONS[RES] ,pygame.FULLSCREEN)
pygame.display.set_caption("bruh")

def init_grid(rows,cols,color):
    grid = []
    for i in range(rows):
        grid.append([])
        for _ in range(cols):
            grid[i].append(color)
    return grid

def grid_draw(win,grid):
    for i , row in enumerate(grid):
        for j , pixel in enumerate(row):
            pygame.draw.rect(win , pixel , (j * PIXEL_SIZE + 10, i * PIXEL_SIZE + 10,PIXEL_SIZE,PIXEL_SIZE))
    if DRAW_GRID_LINES:
        for i in range(ROWS):
            pygame.draw.line(win, WHITE ,(10,i * PIXEL_SIZE ),(WIDTH - 10 , i * PIXEL_SIZE))
        for i in range(COLUMS):
            pygame.draw.line(win, WHITE ,(i * PIXEL_SIZE , 10),(i * PIXEL_SIZE, HEIGHT - TOOLBAR_HIGHT))

def background_draw(win):
    win.fill(ORANGE)
    pygame.draw.rect(win,BG_COLOUR,[10,10,WIDTH - 20, HEIGHT - 20])

def draw(win , grid):
    background_draw(win)
    grid_draw(win,grid)
    pygame.display.update()

run = True
clock = pygame.time.Clock()
grid = init_grid(ROWS, COLUMS, BG_COLOUR)


while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    draw(WIN,grid)

pygame.quit() 