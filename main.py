import pygame,sys
from pygame.locals import *
from player import Player

pygame.init()

WINDOW_SIZE = (640,800)
DISPLAY_SIZE = (160,200)

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Platformer Jump")

display = pygame.Surface(DISPLAY_SIZE)


time = pygame.time.Clock()
loop = True

player = Player(10,10)

while loop:
    display.fill((135, 206, 235))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
        player.move_dir(event)
        
    #draw
    player.draw(display)

    #update
    player.update()
    window.blit(pygame.transform.scale(display,WINDOW_SIZE),(0,0))
    pygame.display.update()
    time.tick(60)