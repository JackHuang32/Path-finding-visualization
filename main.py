from color import*
import pygame
from spot import spot
WIDTH = 800
PAD = 50
NUMBER = 20
DIAMETER = (WIDTH-2*PAD)/(2*NUMBER-1)
RADIUS = DIAMETER/2
GRID=[[spot(RADIUS,PAD+RADIUS+2*i*DIAMETER,PAD+RADIUS+2*j*DIAMETER,i,j) for j in range(NUMBER)] for i in range(NUMBER)]
def draw_begin(win):
    for i in range(NUMBER):
        for j in range(NUMBER):
            GRID[i][j].show(win)
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
