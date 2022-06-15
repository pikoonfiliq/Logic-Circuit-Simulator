

from pygame.mouse import get_rel, get_pressed, get_pos
from pygame.gfxdraw import filled_circle
from pygame.draw import rect, line
from time import sleep
from .utility import *
from .User_settings import *




class BorderDot:
    def __init__(self, x=WORKSPACE_START_W, y=WORKSPACE_START_H, state=0):
        self.type = 'BORDER_DOT'
        self.x = int(x)
        self.y = int(y)
        self.size = WIDTH / 128
        self.state = 0
        self.color = border_dot_color_0 if self.state == 0 else border_dot_color_1
        
        
        self.dots = []
        self.dots.append((self.x, self.y))
        all_border_dots.append(self)
        sleep(0.3)# used to prevent more than one dots appearing when clicking near the border
    def change_state(self):
        self.state = 1 if self.state == 0 else 0
        self.color = border_dot_color_0 if self.state == 0 else border_dot_color_1
    def checkIFclicked(self, x, y):
        """
        check if x, y are in the dot
        if so, change state
        """
        if self.x - self.size < x < self.x + self.size and self.y - self.size < y < self.y + self.size:
            self.change_state()
            return True
        return False
    def draw(self, screen):
        filled_circle(screen, self.x, self.y, int(self.size), self.color)

class Button:
    def __init__(self, screen, clr, text, class_to_exec):
        self.type = "BUTTON"
        self.class_to_exec = class_to_exec
        self.num = len(all_buttons) + 1
        self.clr = clr
        self.txt = text
        self.screen = screen
        all_buttons.append(self)
        sleep(0.3) # used to prevent more than one blocks appearing when clicking on button
    def get_pos(self,mouse_x,mouse_y):

        BLOCK_START_W = BLOCKMENU_START_W + x*self.num+((BLOCKMENU_WIDTH-11*x)/10)*(self.num-1)
        BLOCK_START_H = BLOCKMENU_START_H  + x

        BLOCK_W = ((BLOCKMENU_WIDTH-11*x)/10)
        BLOCK_H = x*2

        if BLOCK_START_W < mouse_x and (BLOCK_START_W + BLOCK_W) > mouse_x:
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
    def onclick(self):
        self.class_to_exec()

class wire:
    def __init__(self, screen, state=0, ev=None):
        self.type = "WIRE"
        self.dot_start, self.blck_start, self.wireNumber_start = self.check_if_near_dot() # obj-ta na kogoto tochkata prinadleji
        
        self.state = state
        self.screen = screen
        
        if self.dot_start != None:
            self.begin_obj = self.blck_start
            self.begin_coords = self.dot_start
            
            clicked = 1
            
            while True:
                ev = pygame.event.get()
                for event in ev:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        clicked = 1
                    elif event.type == pygame.MOUSEBUTTONUP:
                        clicked = 0
                
                
                if clicked == 1:
                    self.end_coords = get_pos()                
                    draw(screen, temp_lines=[[self.begin_coords, self.end_coords]]) 

                elif clicked == 0:
                    self.end_obj = self.check_if_near_dot(self.end_coords)[1]
                    if self.end_obj != None:
                        self.end_coords = self.check_if_near_dot(self.end_coords)[0]
                        if self.end_coords != self.begin_coords:
                            self.end_coords, self.end_obj, self.wireNumber_end= self.check_if_near_dot(self.end_coords)
                            all_wires.append(self)
                            
                            # have to match wire to which input it is connected
                            if self.begin_obj.type == "BLOCK":
                                self.begin_obj.wires[self.wireNumber_start] = self
                            
                            if self.end_obj.type == "BLOCK":
                                self.end_obj.wires[self.wireNumber_end] = self
                            
                            if self.begin_obj.type == 'BORDER_DOT_END':
                                self.begin_obj.wire.append(self) 
                                
                            if self.end_obj.type == 'BORDER_DOT_END':
                                self.end_obj.wire.append(self)        
                            #return None
                            break
                    else:
                        break
        return None
    
    def draw(self):
        #if self.begin_coords != None and self.end_coords != None:
        line(self.screen , wire_color_0 if self.state == 0 else wire_color_1, self.begin_obj.dots[self.wireNumber_start], self.end_obj.dots[self.wireNumber_end] , int(WIDTH / 640))          
    def check_if_near_dot(self, clicked_coords=None):
        clicked_coords = get_pos()
        
        check_from = (clicked_coords[0] - dot_size, clicked_coords[1] - dot_size)
        check_to = (clicked_coords[0] + dot_size, clicked_coords[1] + dot_size)
        
        for block in all_blocks:
            i = -1
            for dot in block.dots:
                i += 1
                if check_from[0] <= dot[0] and dot[0] <= check_to[0] and check_from[1] <= dot[1] and dot[1] <= check_to[1]:
                    return dot, block, i
        for dot in all_border_dots:
            if check_from[0] <= dot.x and dot.x <= check_to[0] and check_from[1] <= dot.y and dot.y <= check_to[1]:
                return (dot.x, dot.y), dot, 0
        for dot in all_border_end_dots:
            if check_from[0] <= dot.x and dot.x <= check_to[0] and check_from[1] <= dot.y and dot.y <= check_to[1]:
                return (dot.x, dot.y), dot, 0
        return None, None, None
    def updateState(self):
        if self.begin_obj != None and self.end_obj != None:
            self.state = self.begin_obj.state
            
        
class AND:
    def __init__(self, x=WIDTH /2, y=HEIGHT/2):
        self.type = "BLOCK"
        self.x = x
        self.y = y
        self.wires = [None, None, None]
        self.dots = []

        self.outline_top = (self.x - block_size * 2, self.y - block_size)
        self.outline_bot = (self.x + block_size, self.y + block_size)
        
        self.input1_coords = (self.x - block_size*2, self.y + block_size/2)
        self.input2_coords = (self.x - block_size*2, self.y - block_size/2)
        self.state_coords = (self.x + block_size*2, self.y)
        
        self.input1 = 0
        self.input2 = 0
        self.state = 1 if self.input1 == 1 and self.input2 == 1 else 0 # output
        
        self.dots.append(self.input1_coords)
        self.dots.append(self.input2_coords)
        self.dots.append(self.state_coords)
        
        
        all_blocks.append(self)
    
                
    def updateState(self):
        if self.wires[0] != None and self.wires[1] != None:
            self.input1 = self.wires[0].state
            self.input2 = self.wires[1].state
        self.state = 1 if self.input1 == 1 and self.input2 == 1 else 0 # output
    
    def move(self, screen): # needs optimization with get_rel()
        clicked = 1
        
        while clicked == 1:
            ev = pygame.event.get()
            for event in ev:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clicked = 1
                elif event.type == pygame.MOUSEBUTTONUP:
                    clicked = 0          
            if clicked == 1:
                draw(screen) 
                mouse_coords = get_pos()
                if self.outline_top[0] < mouse_coords[0] and mouse_coords[0] < self.outline_bot[0] and self.outline_top[1] < mouse_coords[1] and mouse_coords[1] < self.outline_bot[1]:
                    self.x = mouse_coords[0]
                    self.y = mouse_coords[1]
                    self.outline_top = (self.x - block_size * 2, self.y - block_size)
                    self.outline_bot = (self.x + block_size, self.y + block_size)
                    self.input1_coords = (self.x - block_size*2, self.y + block_size/2)
                    self.input2_coords = (self.x - block_size*2, self.y - block_size/2)
                    self.state_coords = (self.x + block_size*2, self.y)
                    self.dots[0] = self.input1_coords
                    self.dots[1] = self.input2_coords
                    self.dots[2] = self.state_coords
            
    def draw(self, screen):
        # risuva samiq block
        rect(screen, block_color, (self.x - block_size*2, self.y - block_size, block_size * 2 * 2, block_size * 2))
        #filled_circle(screen, self.x, self.y, block_size, block_color)
        
        # risuva krugcheta okolo input tochkite
        filled_circle(screen, int(self.input1_coords[0]), int(self.input1_coords[1]), int(dot_size), RED)
        filled_circle(screen, int(self.input2_coords[0]), int(self.input2_coords[1]), int(dot_size), RED)
        filled_circle(screen, int(self.state_coords[0]), int(self.state_coords[1]), int(dot_size), RED)
        
        #risuva tekst sus AND
        my_font = get_font(int(x*2))
        text_surface = my_font.render("AND", False, (0, 0, 0))
        screen.blit(text_surface, (self.x - block_size*2 +((block_size*2*2 -text_surface.get_size()[0])/2), self.y - block_size + ((block_size*2 -text_surface.get_size()[1])/2)))
        
        # risuva samite tochki za da e po - qsno
        rect(screen, block_color, (self.input1_coords[0], self.input1_coords[1], 2, 2))
        rect(screen, block_color, (self.input2_coords[0], self.input2_coords[1], 2, 2))
        rect(screen, block_color, (self.state_coords[0], self.state_coords[1], 2, 2))

class NAND:
    def __init__(self, x=WIDTH /2, y=HEIGHT/2):
        self.type = "BLOCK"
        self.x = x
        self.y = y
        self.wires = [None, None, None]
        self.dots = []

        self.outline_top = (self.x - block_size * 2, self.y - block_size)
        self.outline_bot = (self.x + block_size, self.y + block_size)
        
        self.input1_coords = (self.x - block_size*2, self.y + block_size/2)
        self.input2_coords = (self.x - block_size*2, self.y - block_size/2)
        self.state_coords = (self.x + block_size*2, self.y)
        
        self.input1 = 0
        self.input2 = 0
        self.state = 1 if self.input1 == 1 and self.input2 == 1 else 0 # output
        
        self.dots.append(self.input1_coords)
        self.dots.append(self.input2_coords)
        self.dots.append(self.state_coords)
        
        
        all_blocks.append(self)
    
    def updateState(self):
        if self.wires[0] != None and self.wires[1] != None:
            self.input1 = self.wires[0].state
            self.input2 = self.wires[1].state
        self.state = 1 if self.input1 == 0 and self.input2 == 0 else 0 # output
    
    def move(self, screen): # needs optimization with get_rel()
        clicked = 1
        
        while clicked == 1:
            ev = pygame.event.get()
            for event in ev:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clicked = 1
                elif event.type == pygame.MOUSEBUTTONUP:
                    clicked = 0
                    
            if clicked == 1:
                draw(screen) 
                mouse_coords = get_pos()
                if self.outline_top[0] < mouse_coords[0] and mouse_coords[0] < self.outline_bot[0] and self.outline_top[1] < mouse_coords[1] and mouse_coords[1] < self.outline_bot[1]:
                    self.x = mouse_coords[0]
                    self.y = mouse_coords[1]
                    self.outline_top = (self.x - block_size * 2, self.y - block_size)
                    self.outline_bot = (self.x + block_size, self.y + block_size)
                    self.input1_coords = (self.x - block_size*2, self.y + block_size/2)
                    self.input2_coords = (self.x - block_size*2, self.y - block_size/2)
                    self.state_coords = (self.x + block_size*2, self.y)
                    self.dots[0] = self.input1_coords
                    self.dots[1] = self.input2_coords
                    self.dots[2] = self.state_coords
            
    def draw(self, screen):
        # risuva samiq block
        rect(screen, block_color, (self.x - block_size*2, self.y - block_size, block_size * 2 * 2, block_size * 2))
        #filled_circle(screen, self.x, self.y, block_size, block_color)
        
        # risuva krugcheta okolo input tochkite
        filled_circle(screen, int(self.input1_coords[0]), int(self.input1_coords[1]), int(dot_size), RED)
        filled_circle(screen, int(self.input2_coords[0]), int(self.input2_coords[1]), int(dot_size), RED)
        filled_circle(screen, int(self.state_coords[0]), int(self.state_coords[1]), int(dot_size), RED)
        
        #risuva tekst sus AND
        my_font = get_font(int(x*2))
        text_surface = my_font.render("NAND", False, (0, 0, 0))
        screen.blit(text_surface, (self.x - block_size*2 +((block_size*2*2 -text_surface.get_size()[0])/2), self.y - block_size + ((block_size*2 -text_surface.get_size()[1])/2)))
        
        
        # risuva samite tochki za da e po - qsno
        rect(screen, block_color, (self.input1_coords[0], self.input1_coords[1], 2, 2))
        rect(screen, block_color, (self.input2_coords[0], self.input2_coords[1], 2, 2))
        rect(screen, block_color, (self.state_coords[0], self.state_coords[1], 2, 2))
              
class OR:
    def __init__(self, x=WIDTH /2, y=HEIGHT/2):
        self.type = "BLOCK"
        self.x = x
        self.y = y
        self.wires = [None, None, None]
        self.dots = []

        self.outline_top = (self.x - block_size * 2, self.y - block_size)
        self.outline_bot = (self.x + block_size, self.y + block_size)
        
        self.input1_coords = (self.x - block_size*2, self.y + block_size/2)
        self.input2_coords = (self.x - block_size*2, self.y - block_size/2)
        self.state_coords = (self.x + block_size*2, self.y)
        
        self.input1 = 0
        self.input2 = 0
        self.state = 1 if self.input1 == 1 and self.input2 == 1 else 0 # output
        
        self.dots.append(self.input1_coords)
        self.dots.append(self.input2_coords)
        self.dots.append(self.state_coords)
        
        
        all_blocks.append(self)
    
    def updateState(self):
        if self.wires[0] != None and self.wires[1] != None:
            self.input1 = self.wires[0].state
            self.input2 = self.wires[1].state
        self.state = 1 if self.input1 == 1 or self.input2 == 1 else 0 # output
    
    def move(self, screen): # needs optimization with get_rel()
        clicked = 1
        
        while clicked == 1:
            ev = pygame.event.get()
            for event in ev:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clicked = 1
                elif event.type == pygame.MOUSEBUTTONUP:
                    clicked = 0
                    
            if clicked == 1:
                draw(screen) 
                mouse_coords = get_pos()
                if self.outline_top[0] < mouse_coords[0] and mouse_coords[0] < self.outline_bot[0] and self.outline_top[1] < mouse_coords[1] and mouse_coords[1] < self.outline_bot[1]:
                    self.x = mouse_coords[0]
                    self.y = mouse_coords[1]
                    self.outline_top = (self.x - block_size * 2, self.y - block_size)
                    self.outline_bot = (self.x + block_size, self.y + block_size)
                    self.input1_coords = (self.x - block_size*2, self.y + block_size/2)
                    self.input2_coords = (self.x - block_size*2, self.y - block_size/2)
                    self.state_coords = (self.x + block_size*2, self.y)
                    self.dots[0] = self.input1_coords
                    self.dots[1] = self.input2_coords
                    self.dots[2] = self.state_coords
            
    def draw(self, screen):
        # risuva samiq block
        rect(screen, block_color, (self.x - block_size*2, self.y - block_size, block_size * 2 * 2, block_size * 2))
        #filled_circle(screen, self.x, self.y, block_size, block_color)
        
        # risuva krugcheta okolo input tochkite
        filled_circle(screen, int(self.input1_coords[0]), int(self.input1_coords[1]), int(dot_size), RED)
        filled_circle(screen, int(self.input2_coords[0]), int(self.input2_coords[1]), int(dot_size), RED)
        filled_circle(screen, int(self.state_coords[0]), int(self.state_coords[1]), int(dot_size), RED)
        
        #risuva tekst sus AND
        my_font = get_font(int(x*2))
        text_surface = my_font.render("OR", False, (0, 0, 0))
        screen.blit(text_surface, (self.x - block_size*2 +((block_size*2*2 -text_surface.get_size()[0])/2), self.y - block_size + ((block_size*2 -text_surface.get_size()[1])/2)))
        
        
        # risuva samite tochki za da e po - qsno
        rect(screen, block_color, (self.input1_coords[0], self.input1_coords[1], 2, 2))
        rect(screen, block_color, (self.input2_coords[0], self.input2_coords[1], 2, 2))
        rect(screen, block_color, (self.state_coords[0], self.state_coords[1], 2, 2))
        
class NOR:
    def __init__(self, x=WIDTH /2, y=HEIGHT/2):
        self.type = "BLOCK"
        self.x = x
        self.y = y
        self.wires = [None, None, None]
        self.dots = []

        self.outline_top = (self.x - block_size * 2, self.y - block_size)
        self.outline_bot = (self.x + block_size, self.y + block_size)
        
        self.input1_coords = (self.x - block_size*2, self.y + block_size/2)
        self.input2_coords = (self.x - block_size*2, self.y - block_size/2)
        self.state_coords = (self.x + block_size*2, self.y)
        
        self.input1 = 0
        self.input2 = 0
        self.state = 0 if self.input1 == 1 or self.input2 == 1 else 0 # output
        
        self.dots.append(self.input1_coords)
        self.dots.append(self.input2_coords)
        self.dots.append(self.state_coords)
        
        
        all_blocks.append(self)
    
    def updateState(self):
        if self.wires[0] != None and self.wires[1] != None:
            self.input1 = self.wires[0].state
            self.input2 = self.wires[1].state
        self.state = 1 if self.input1 == 0 or self.input2 == 0 else 0 # output
    
    def move(self, screen): # needs optimization with get_rel()
        clicked = 1
        
        while clicked == 1:
            ev = pygame.event.get()
            for event in ev:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clicked = 1
                elif event.type == pygame.MOUSEBUTTONUP:
                    clicked = 0
                    
            if clicked == 1:
                draw(screen) 
                mouse_coords = get_pos()
                if self.outline_top[0] < mouse_coords[0] and mouse_coords[0] < self.outline_bot[0] and self.outline_top[1] < mouse_coords[1] and mouse_coords[1] < self.outline_bot[1]:
                    self.x = mouse_coords[0]
                    self.y = mouse_coords[1]
                    self.outline_top = (self.x - block_size * 2, self.y - block_size)
                    self.outline_bot = (self.x + block_size, self.y + block_size)
                    self.input1_coords = (self.x - block_size*2, self.y + block_size/2)
                    self.input2_coords = (self.x - block_size*2, self.y - block_size/2)
                    self.state_coords = (self.x + block_size*2, self.y)
                    self.dots[0] = self.input1_coords
                    self.dots[1] = self.input2_coords
                    self.dots[2] = self.state_coords
            
    def draw(self, screen):
        # risuva samiq block
        rect(screen, block_color, (self.x - block_size*2, self.y - block_size, block_size * 2 * 2, block_size * 2))
        #filled_circle(screen, self.x, self.y, block_size, block_color)
        
        # risuva krugcheta okolo input tochkite
        filled_circle(screen, int(self.input1_coords[0]), int(self.input1_coords[1]), int(dot_size), RED)
        filled_circle(screen, int(self.input2_coords[0]), int(self.input2_coords[1]), int(dot_size), RED)
        filled_circle(screen, int(self.state_coords[0]), int(self.state_coords[1]), int(dot_size), RED)
        
        #risuva tekst sus AND
        my_font = get_font(int(x*2))
        text_surface = my_font.render("NOR", False, (0, 0, 0))
        screen.blit(text_surface, (self.x - block_size*2 +((block_size*2*2 -text_surface.get_size()[0])/2), self.y - block_size + ((block_size*2 -text_surface.get_size()[1])/2)))
        
        
        # risuva samite tochki za da e po - qsno
        rect(screen, block_color, (self.input1_coords[0], self.input1_coords[1], 2, 2))
        rect(screen, block_color, (self.input2_coords[0], self.input2_coords[1], 2, 2))
        rect(screen, block_color, (self.state_coords[0], self.state_coords[1], 2, 2))
        
        
class BorderDotEnd:
    def __init__(self, x=WORKSPACE_START_W, y=WORKSPACE_START_H, state=0):
        self.type = 'BORDER_DOT_END'
        self.wire = []
        self.x = int(x)
        self.y = int(y)
        self.size = WIDTH / 128
        self.state = 0
        self.color = border_dot_color_0 if self.state == 0 else border_dot_color_1
        
        
        self.dots = []
        self.dots.append((self.x, self.y))
        all_border_end_dots.append(self)
        sleep(0.3)# used to prevent more than one dots appearing when clicking near the border
    def updateState(self):
        for wire in self.wire:
            self.state = wire.state
        self.color = border_dot_color_0 if self.state == 0 else border_dot_color_1
    def checkIFclicked(self, x, y):
        """
        check if x, y are in the dot
        """
        if self.x - self.size < x < self.x + self.size and self.y - self.size < y < self.y + self.size:
            #self.change_state()
            return True
        return False
    def draw(self, screen):
        filled_circle(screen, self.x, self.y, int(self.size), self.color)