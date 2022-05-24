from ast import Try
from xml.etree.ElementTree import PI

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

def background_draw(win):
    win.fill(BG_COLOUR)
    pygame.draw.rect(win , (55,57,61) , (WORKSPACE_START_W,WORKSPACE_START_H , WORKSPACE_WIDTH,WORKSPACE_HEIGHT) , 5)
    pygame.draw.rect(win , (55,57,61) , (BLOCKMENU_START_W,BLOCKMENU_START_H , BLOCKMENU_WIDTH,BLOCKMENU_HEIGHT) , 5)
    pygame.draw.rect(win , (55,57,61) , (FILEMENU_START_W,FILEMENU_START_H , FILEMENU_WIDTH,FILEMENU_HEIGHT))




def draw(win,debug,x,y):
    background_draw(win)
    if debug == 1:
        pygame.draw.rect(win , RED , (x,y , 10,10))
    pygame.display.update()
        
run = True
clock = pygame.time.Clock()



while run:
    clock.tick(FPS)
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = False
        
        if pygame.mouse.get_pressed()[0]:
            x,y = pygame.mouse.get_pos()
            debug = 1
            try:
                pass
            except IndexError:
                pass
        else:
            debug = 0
    draw(WIN,debug, x,y)

pygame.quit() 