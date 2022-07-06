from queue import PriorityQueue
from tkinter import Grid
from color import*
import pygame
from spot import spot
from time import sleep
WIDTH = 800
PAD = 50
NUMBER = 30
DIAMETER = (WIDTH-2*PAD)/(NUMBER+NUMBER//2)
RADIUS = DIAMETER/2
GRID=[[spot(RADIUS,PAD+RADIUS+1.5*j*DIAMETER,PAD+RADIUS+1.5*i*DIAMETER,i,j) for j in range(NUMBER)] for i in range(NUMBER)]

def draw_begin(win):
    #draw circles
    for i in range(NUMBER):
        for j in range(NUMBER):
            GRID[i][j].show(win)
    #draw parallel lines
    for i in range(NUMBER):
        for j in range(NUMBER):
            if j != NUMBER-1:    
                pygame.draw.line(win,BLACK,(GRID[i][j].coord[0]+RADIUS,GRID[i][j].coord[1]),((GRID[i][j].coord[0]+RADIUS+RADIUS,GRID[i][j].coord[1])),2)
            if i != NUMBER-1:
                pygame.draw.line(win,BLACK,(GRID[i][j].coord[0],GRID[i][j].coord[1]+RADIUS),(GRID[i][j].coord[0],GRID[i][j].coord[1]+RADIUS+RADIUS),2)
            if i != NUMBER-1 and j != NUMBER-1:
                pygame.draw.line(win,BLACK,(GRID[i][j].coord[0]+RADIUS/1.414,GRID[i][j].coord[1]+RADIUS/1.414),(GRID[i+1][j+1].coord[0]-RADIUS/1.414,GRID[i+1][j+1].coord[1]-RADIUS/1.414),2)
            if i != NUMBER-1 and j != 0:
                pygame.draw.line(win,BLACK,(GRID[i][j].coord[0]-RADIUS/1.414,GRID[i][j].coord[1]+RADIUS/1.414),(GRID[i+1][j-1].coord[0]+RADIUS/1.414,GRID[i+1][j-1].coord[1]-RADIUS/1.414),2)
    pygame.display.update()
def get_clicked_pos(coord):
    x,y = coord
    if x <= PAD or y <= PAD:
        return False
    if x >= WIDTH-PAD or y >= WIDTH-PAD:
        return False
    col = int((x-PAD)//(1.5*DIAMETER))
    row = int((y-PAD)//(1.5*DIAMETER))
    near = GRID[row][col].coord
    if (near[0]-x)**2+(near[1]-y)**2 < RADIUS**2:
        return row,col
    else:
        return False
def dis(first,second):
    row1,col1 = first.pos
    row2,col2 = second.pos
    return abs(row1-row2)**2+abs(col2-col1)**2
def draw_path(start,end,pi,win):
    cur = pi[end]
    count=1
    while cur != start:
        count+=1
        cur.make_path(win)
        cur = pi[cur]
    print(count)
def A_PATH(start,end,win):
    global GRID
    VISIT = {start}
    pq = PriorityQueue()
    PI = {s:0 for row in GRID for s in row}
    F = {s:float('inf') for row in GRID for s in row}
    G = {s:float('inf') for row in GRID for s in row}
    G[start]=0
    F[start]=0+dis(start,end)
    pq.put((0,start))
    while not pq.empty():
        sleep(0.1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        current = pq.get()[1]
        if current == end:
            draw_path(start,end,PI,win)
            return True
        #VISIT.remove(current)
        for neighbor in current.neighbors(GRID):
            if G[neighbor] > G[current]+dis(current,neighbor):
                G[neighbor] = G[current]+dis(current,neighbor)
                F[neighbor] = G[neighbor]+dis(neighbor,end)
                PI[neighbor] = current
                if neighbor not in VISIT:
                    pq.put((F[neighbor],neighbor))
                    VISIT.add(neighbor)
                    if neighbor != end and neighbor != start:
                        neighbor.make_current(win)
        if current != start:
            current.make_done(win)
    return False
def clear(win):
    for row in GRID:
        for s in row:
            s.make_origin(win)
def reset(win):
    for row in GRID:
        for s in row:
            if s.is_done() or s.is_current() or s.is_path():
                s.make_origin(win)
if __name__ == '__main__':
    
    pygame.init()
    win = pygame.display.set_mode((WIDTH,WIDTH))
    pygame.display.set_caption('Path finding visualization')
    win.fill(WHITE)
    draw_begin(win)
    started = False
    start = None
    end = None
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if started:
                continue
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not started and start and end:
                    started = True
                    print('start')
                    A_PATH(start,end,win)
                    started = False
                if event.key == pygame.K_c and not started:
                    clear(win)
                    start = None
                    end = None
                if event.key == pygame.K_r and not started:
                    reset(win)
            pygame.display.update()
    pygame.quit()
