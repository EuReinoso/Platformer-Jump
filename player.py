import pygame
pygame.init()

class Player:
    def __init__(self,x,y):

        self.img = [pygame.image.load("assets/idle.png"),
                    pygame.image.load("assets/run_1.png"),
                    pygame.image.load("assets/run_2.png")]
        
        self.rect = self.img[0].get_rect()
        self.rect[0] = x
        self.rect[1] = y

    def draw(self,display):
        display.blit(self.img[0],(self.rect[0],self.rect[1]))

    def update():
        pass