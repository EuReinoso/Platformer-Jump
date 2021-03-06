import pygame
pygame.init()

GRAVITY = 0.1

class Player:
    def __init__(self,x,y):

        self.img_idle =[pygame.image.load("assets/idle.png")]
        self.img_run = [pygame.image.load("assets/run_1.png"),
                        pygame.image.load("assets/run_2.png")]

        self.current_img = self.img_idle[0]
        
        self.rect = self.img_idle[0].get_rect()
        self.rect.x = x
        self.rect.y = y
        self.y_momentum = 0
        self.x_vel = 2

        self.jump_force = 3

        self.right = False
        self.left = False

        self.run = False

        self.ticks = 0
        self.frame = 0

    def draw(self,display):
        display.blit(self.current_img,(self.rect.x,self.rect.y))

    def update(self):
        self.gravity()
        self.move()
        self.anim(10,2)

    def gravity(self):
        self.y_momentum += GRAVITY
        self.rect.y += self.y_momentum

    def jump(self):
        self.y_momentum = -self.jump_force
    
    def move_dir(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.right = True      
            elif event.key == pygame.K_LEFT:
                self.left = True       
            # if event.key == pygame.K_SPACE:
            #     self.jump()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.right = False
            elif event.key == pygame.K_LEFT:
                self.left = False
                
    def move(self):
        if self.right:
            self.rect.x += self.x_vel
            self.run = True
        elif self.left:
            self.rect.x -= self.x_vel
            self.run = True
        else:
            self.run = False

    def anim(self,tick,frame):
        self.ticks += 1
        if self.ticks >= tick:
            self.ticks = 0
            self.frame += 1
        if self.frame == frame:
            self.frame = 0

        if self.run:
            self.current_img = self.img_run[self.frame]
        else:
            self.current_img = self.img_idle[0]
        
       
        
            

            
