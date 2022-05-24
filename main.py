from ast import Try
from xml.etree.ElementTree import PI
from black import Line

from numpy import full
from utils import * 
dots = []
blocks = []
lines = []
entities = [lines , blocks , dots ]

def artef_ent():
    entities[0].append(wire(800,800,1000,1000,True))

# pravi ekrana
WIN = pygame.display.set_mode(RESOLUTIONS[RES] ,pygame.FULLSCREEN) 
pygame.display.set_caption("bruh")

def draw_entity(win):
    for l in entities[0]:
        if l.state == True:
            crl = RED
        else:
            crl = (161,40 ,48)
        pygame.draw.line(win , crl , (l.beg_w , l.beg_h,l.end_w , l.end_h) , 3)

# pravi backgrounda
def background_draw(win):
    win.fill(BG_COLOUR)
    pygame.draw.rect(win , (55,57,61) , (WORKSPACE_START_W,WORKSPACE_START_H , WORKSPACE_WIDTH,WORKSPACE_HEIGHT) , 5)
    pygame.draw.rect(win , (55,57,61) , (BLOCKMENU_START_W,BLOCKMENU_START_H , BLOCKMENU_WIDTH,BLOCKMENU_HEIGHT) , 5)
    pygame.draw.rect(win , (55,57,61) , (FILEMENU_START_W,FILEMENU_START_H , FILEMENU_WIDTH,FILEMENU_HEIGHT))



#osnova funkciq za risuvane
def draw(win):
    background_draw(win)
    draw_entity(win)
    pygame.display.update()
        
run = True
clock = pygame.time.Clock()


#main loop
while run:
    clock.tick(FPS)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = False
        if pygame.mouse.get_pressed()[0]:
            x,y = pygame.mouse.get_pos()
            try:
                pass
            except IndexError:
                pass
        else:
            debug = 0
    draw(WIN)

pygame.quit() 