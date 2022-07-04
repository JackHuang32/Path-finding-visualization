from queue import PriorityQueue
from tkinter import Grid
from color import*
import pygame
from spot import spot
WIDTH = 800
PAD = 50
NUMBER = 20
DIAMETER = (WIDTH-2*PAD)/(2*NUMBER-1)
RADIUS = DIAMETER/2
GRID=[[spot(RADIUS,PAD+RADIUS+2*j*DIAMETER,PAD+RADIUS+2*i*DIAMETER,i,j) for j in range(NUMBER)] for i in range(NUMBER)]

def draw_begin(win):
    #draw circles
    for i in range(NUMBER):
        for j in range(NUMBER):
            GRID[i][j].show(win)
    #draw parallel lines
    for i in range(NUMBER):
        for j in range(NUMBER):
            if j != NUMBER-1:    
                pygame.draw.line(win,BLACK,(GRID[i][j].coord[0]+RADIUS,GRID[i][j].coord[1]),((GRID[i][j].coord[0]+RADIUS+DIAMETER,GRID[i][j].coord[1])),2)
            if i != NUMBER-1:
                pygame.draw.line(win,BLACK,(GRID[i][j].coord[0],GRID[i][j].coord[1]+RADIUS),(GRID[i][j].coord[0],GRID[i][j].coord[1]+RADIUS+DIAMETER),2)
            if i != NUMBER-1 and j != NUMBER-1:
                pygame.draw.line(win,BLACK,(GRID[i][j].coord[0]+RADIUS/1.414,GRID[i][j].coord[1]+RADIUS/1.414),(GRID[i+1][j+1].coord[0]-RADIUS/1.414,GRID[i+1][j+1].coord[1]-RADIUS/1.414),2)
            if i != NUMBER-1 and j != 0:
                pygame.draw.line(win,BLACK,(GRID[i][j].coord[0]-RADIUS/1.414,GRID[i][j].coord[1]+RADIUS/1.414),(GRID[i+1][j-1].coord[0]+RADIUS/1.414,GRID[i+1][j-1].coord[1]-RADIUS/1.414),2)
    pygame.display.update()
def get_clicked_pos(coord):
    x,y = coord
    if x < PAD or y < PAD:
        return False
    if x > WIDTH-PAD or y > WIDTH-PAD:
        return False
    col = int((x-PAD)//(2*DIAMETER))
    row = int((y-PAD)//(2*DIAMETER))
    near = GRID[row][col].coord
    if (near[0]-x)**2+(near[1]-y)**2 < RADIUS**2:
        return row,col
    else:
        return False
def A_PATH(start,end):
    pq = PriorityQueue()
    while not pq.empty():
        
if __name__ == '__main__':
    
    pygame.init()
    win = pygame.display.set_mode((WIDTH,WIDTH))
    pygame.display.set_caption('Path finding visualization')
    win.fill(WHITE)
    draw_begin(win)
    start = None
    end = None
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                pos = get_clicked_pos(pos)
                if pos != False and not start:
                    GRID[pos[0]][pos[1]].make_begin(win)
                    start = GRID[pos[0]][pos[1]]
                    #print('make begin!')
                elif pos != False and not end and not GRID[pos[0]][pos[1]].is_begin():
                    GRID[pos[0]][pos[1]].make_end(win)
                    end = GRID[pos[0]][pos[1]]
                    #print('make end!')
                elif pos != False and not GRID[pos[0]][pos[1]].is_begin() and not GRID[pos[0]][pos[1]].is_end():
                    GRID[pos[0]][pos[1]].make_block(win)
                    #print('make block!')
            if pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                pos = get_clicked_pos(pos)
                if pos != False:
                    GRID[pos[0]][pos[1]].make_origin(win)
                    if start and start.pos == pos:
                        start = None
                    if end and end.pos == pos:
                        end = None
            pygame.display.update()
    pygame.quit()
