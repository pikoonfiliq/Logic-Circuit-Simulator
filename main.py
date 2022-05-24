from ast import Try
from xml.etree.ElementTree import PI

from numpy import full
from utils import * 




WIN = pygame.display.set_mode(RESOLUTIONS[RES] ,pygame.FULLSCREEN)
pygame.display.set_caption("bruh")

def background_draw(win):
    win.fill(BG_COLOUR)
    pygame.draw.rect(win , (55,57,61) , (WORKSPACE_START_W,WORKSPACE_START_H , WORKSPACE_WIDTH,WORKSPACE_HEIGHT) , 5)
    pygame.draw.rect(win , (55,57,61) , (BLOCKMENU_START_W,BLOCKMENU_START_H , BLOCKMENU_WIDTH,BLOCKMENU_HEIGHT) , 5)
    pygame.draw.rect(win , (55,57,61) , (FILEMENU_START_W,FILEMENU_START_H , FILEMENU_WIDTH,FILEMENU_HEIGHT))




def draw(win,debug):
    background_draw(win)
    if debug == 1:
        pygame.draw.rect(win , RED , (0,WORKSPACE_HEIGHT , 10,10))
    for block in all_blocks:
        block.draw(win)
    for wire in all_wires:
        wire.draw()
    pygame.display.update()
        
run = True
clock = pygame.time.Clock()

OR = AND()
wire1 = wire(WIN, 800,800,1000,1000,1)
wire2 = wire(WIN, 1000,1000,600,800,0)
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
    draw(WIN,debug)

pygame.quit() 
