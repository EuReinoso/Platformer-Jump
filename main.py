import pygame,sys
from pygame.locals import *
from player import Player

pygame.init()

WINDOW_SIZE = (640,800)

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Platformer Jump")

loop = True

player = Player(100,100)

while loop:
    window.fill((135, 206, 235))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    player.draw(window)
    pygame.display.update()