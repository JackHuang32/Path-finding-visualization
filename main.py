from turtle import width
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
if __name__ == '__main__':
    
    pygame.init()
    win = pygame.display.set_mode((WIDTH,WIDTH))
    pygame.display.set_caption('Path finding visualization')
    win.fill(WHITE)
    draw_begin(win)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
    pygame.quit()
