import pygame

pygame.init()

class Platform:
    def __init__(self,x,y):
        self.img = pygame.image.load("assets/platform.png")
        self.rect = self.img.get_rect()
        self.rect.x = x    
        self.rect.y = y

        self.y_vel = 1


    def draw(self,display):
        display.blit(self.img,(self.rect.x,self.rect.y))

    def update(self):
        self.move()

    def move(self):
        self.rect.y += self.y_vel

