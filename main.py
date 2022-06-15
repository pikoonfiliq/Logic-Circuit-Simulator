from numpy import full
from utils import * 




WIN = pygame.display.set_mode(RESOLUTIONS[RES] ,pygame.FULLSCREEN)
pygame.display.set_caption(NAME)     
run = True
clock = pygame.time.Clock()

#initializing main 4 buttons
Button(WIN,(206, 206, 206),'AND', AND)
Button(WIN,(206, 206, 206),'OR', OR)
Button(WIN,(206, 206, 206),'NAND', NAND)
Button(WIN,(206, 206, 206),'NOR', NOR)

#main loop
while run:
    clock.tick(FPS)
    draw(WIN)#drawing
    current_bl = 0#counter used later
    for event in pygame.event.get(): 
        event_global = event
        if event.type == pygame.QUIT:
            run = False
        #logic updates
        for block_ in all_blocks:
            block_.updateState()
        for wire_ in all_wires:
            wire_.updateState()
        for dot_ in all_border_end_dots:
            dot_.updateState()
        #moveing a block
        for block in all_blocks:
                if block.outline_top[0] < x < block.outline_bot[0] and block.outline_top[1] < y < block.outline_bot[1]:
                    block.move(WIN)
        #mouse clicked
        if pygame.mouse.get_pressed()[0]:
            x, y = pygame.mouse.get_pos()
            
            #if we are makinh a wire
            wire(WIN, ev=event)
            #if a button has been klicked
            for butt in all_buttons:
                if butt.get_pos(x,y):
                    butt.onclick()
              
            flag = 0#flag
            #if we clicked near the border of the board we crate an entry dot
            if WORKSPACE_START_W - 10 < x and WORKSPACE_START_W + 10 > x:
                if WORKSPACE_START_H < y and WORKSPACE_START_H + WORKSPACE_HEIGHT > y :
                    if not len(all_border_dots) == 0:
                        for dot in all_border_dots:
                            if dot.checkIFclicked(x, y):
                                flag = 1
                                break
                            else:
                                flag = 0
                    if not flag == 1:
                        BorderDot(y=y)
            #if we clicked on the other side of the board we me an exit dot            
            if WORKSPACE_START_W + WORKSPACE_WIDTH - 10 < x and WORKSPACE_START_W + WORKSPACE_WIDTH + 10> x:
                if WORKSPACE_START_H < y and WORKSPACE_START_H + WORKSPACE_HEIGHT > y :
                    BorderDotEnd(y=y, x=WORKSPACE_START_W + WORKSPACE_WIDTH)
    #if a moved block is outside the workspace it will get deleted with the wires its connected
    for block in all_blocks:
        if block.y < WORKSPACE_START_H or block.y > WORKSPACE_START_H + WORKSPACE_HEIGHT or block.x < WORKSPACE_START_W or block.x > WORKSPACE_START_W + WORKSPACE_WIDTH:
            snap(block)
            del all_blocks[current_bl]
    current_bl=current_bl+1
            
pygame.quit() 
