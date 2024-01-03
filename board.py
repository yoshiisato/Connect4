import constants
import pygame

#Draws grid on the Pygame GUI using squares
def drawGrid(screen):
    blocksize = 100
    for x in range(0, constants.SCREEN_WIDTH, blocksize):
        for y in range(0, constants.SCREEN_HEIGHT, blocksize):
            rect = pygame.Rect(x,y,constants.SCREEN_WIDTH,constants.SCREEN_HEIGHT)
            pygame.draw.rect(screen, constants.BLACK, rect, 1)

#Draws circles given the column (x) and row (y) numbers
def drawCircle(screen, x, y, color):
    center_x = 100*x+50
    center_y = 100*y+50
    pygame.draw.circle(screen, constants.BLACK, (center_x, center_y), 50)
    pygame.draw.circle(screen, color, (center_x, center_y), 48)
