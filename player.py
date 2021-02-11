import pygame
pygame.init()

GRAVITY = 0.1

class Player:
    def __init__(self,x,y):

        self.img = [pygame.image.load("assets/idle.png"),
                    pygame.image.load("assets/run_1.png"),
                    pygame.image.load("assets/run_2.png")]
        
        self.rect = self.img[0].get_rect()
        self.rect.x = x
        self.rect.y = y
        self.y_momentum = 0
        self.x_vel = 2

        self.jump_force = 3

        self.right = False
        self.left = False

    def draw(self,display):
        display.blit(self.img[0],(self.rect.x,self.rect.y))

    def update(self):
        self.gravity()
        self.move()

    def gravity(self):
        self.y_momentum += GRAVITY
        self.rect.y += self.y_momentum

    def jump(self):
        self.y_momentum = -self.jump_force
    
    def move_dir(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.right = True
            if event.key == pygame.K_LEFT:
                self.left = True
            if event.key == pygame.K_SPACE:
                self.jump()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.right = False
            if event.key == pygame.K_LEFT:
                self.left = False
    def move(self):
        if self.right:
            self.rect.x += self.x_vel
        if self.left:
            self.rect.x -= self.x_vel