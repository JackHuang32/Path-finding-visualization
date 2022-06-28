WHITE = (0,0,0)
BLACK = (255,255,255)
TEAL = (104,250,240)
class spot:
    def __init__(self,r,x,y,row,col):
        self.set_radius(r)
        self.set_coord((x,y))
        self.set_color(WHITE)
        self.set_pos((row,col))
    def set_color(self,c):
        self.color = c
    def set_pos(self,p):
        self.pos = p
    def set_radius(self,r):
        self.radius = r
    def set_coord(self,c):
        self.coord = c    
    def get_coord(self):
        return self.x,self.y
    def get_color(self):
        return self.color
    def get_pos(self):
        return self.row, self.col
    def get_radius(self):
        return self.radius
    coord = property(lambda self:self.get_coord,
                     lambda self,c:self.set_coord(c))
    color = property(lambda self:self.get_color,
                     lambda self,c:self.set_color(c))
    pos = property(lambda self:self.get_pos,
                   lambda self,p:self.set_pos(p))
    radius = property(lambda self:self.get_radius,
                      lambda self,r:self.set_radius(r))
    