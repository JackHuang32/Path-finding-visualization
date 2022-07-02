from color import*
import pygame
class spot:
    def __init__(self,r,x,y,row,col):
        self.set_radius(r)
        self.set_coord((x,y))
        self.set_color(WHITE)
        self.set_pos((row,col))
    def set_color(self,c):
        self._color = c
    def set_pos(self,p):
        self._pos = p
    def set_radius(self,r):
        self._radius = r
    def set_coord(self,c):
        self._coord = c  
    @property  
    def get_coord(self):
        return self._coord
    @property
    def get_color(self):
        return self._color
    @property
    def get_pos(self):
        return self._pos
    @property
    def get_radius(self):
        return self._radius
    def make_begin(self):
        self.set_color(GREEN)
    def make_end(self):
        self.set_color(RED)
    def make_block(self):
        self.set_color(BLACK)
    def make_origin(self):
        self.set_color(WHITE)
    def make_done(self):
        self.set_color(TEAL)
    def make_current(self):
        self.set_color(PURPLE)
    def make_path(self):
        self.set_color(YELLOW)
    def is_block(self):
        return self.color == BLACK
    def is_begin(self):
        return self.color == WHITE
    def is_end(self):
        return self.color == RED
    def is_origin(self):
        return self.color == GREEN
    def is_done(self):
        return self.color == TEAL
    def is_current(self):
        return self.color == PURPLE
    def show(self,win):
        pygame.draw.circle(win,self._color,self._coord,self._radius,0)
        pygame.draw.circle(win,BLACK,self._coord,self._radius,3)
        pygame.display.update()
    coord = property(lambda self:self.get_coord,
                     lambda self,c:self.set_coord(c))
    color = property(lambda self:self.get_color,
                     lambda self,c:self.set_color(c))
    pos = property(lambda self:self.get_pos,
                   lambda self,p:self.set_pos(p))
    radius = property(lambda self:self.get_radius,
                      lambda self,r:self.set_radius(r))
    