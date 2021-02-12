import pygame,sys,random
from pygame.locals import *
from player import Player
from platform import Platform

pygame.init()

WINDOW_SIZE = (640,800)
DISPLAY_SIZE = (160,200)

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Platformer Jump")

display = pygame.Surface(DISPLAY_SIZE)

def collission_test(rect,plats):
    hit_list = []
    for plat in plats:
        if rect.colliderect(plat):
            hit_list.append(plat)
    return hit_list

def collision(rect,plats):
    collision_types = {'top': False,'bottom':False}

    hit_list = collission_test(rect,plats)
    for plat in hit_list:
            if player.y_momentum < 0:
                collision_types['top'] = True
            if player.y_momentum > 0:
                if player.rect.bottom >= plat.rect.top:
                    player.rect.bottom = plat.rect.top
                    collision_types['bottom'] = True
    return collision_types

time = pygame.time.Clock()
loop = True

player = Player(10,10)
plat_group = []

ticks = 0

start = True
start_time = 0
    

while loop:
    display.fill((135, 206, 235))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
        player.move_dir(event)
    start_time += 1
    if start:
        if player.rect.y + player.img_idle[0].get_height() >= DISPLAY_SIZE[1]:
            player.rect.y = DISPLAY_SIZE[1] - player.img_idle[0].get_height()
    if start_time >= 720:
        start = False
        
    #gen_plats
    ticks += 1
    if ticks >= 45:
        ticks = 0
        plat_group.append(Platform(random.randint(0,DISPLAY_SIZE[0] - 16),-10))

    #plataform collision
    collisions = collision(player.rect,plat_group)

    if collisions['bottom']:
        player.jump()
    #draw
    player.draw(display)
    for plat in plat_group:
        plat.draw(display)

    #update
    for plat in plat_group:
        plat.update()
        if plat.rect.y >= DISPLAY_SIZE[1]:
            plat_group.pop(0)

    player.update()
    window.blit(pygame.transform.scale(display,WINDOW_SIZE),(0,0))
    pygame.display.update()
    time.tick(60)


