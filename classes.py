import pygame
from random import randint
from math import *

class Baseclass(pygame.sprite.Sprite):
    allsprites = pygame.sprite.Group()
    
    def __init__(self,x,y,width,height,image_string):
        pygame.sprite.Sprite.__init__(self)
        Baseclass.allsprites.add(self)

        self.image = pygame.image.load(image_string)
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.width = width
        self.height = height

    def destroy(self, ClassName):
        ClassName.List.remove(self)
        Baseclass.allsprites.remove(self)
        del self

class Bug(Baseclass):
    
    List = pygame.sprite.Group()
    def __init__(self,x,y,width,height,image_string):
        
        Baseclass.__init__(self,x,y,width,height,image_string)
        Bug.List.add(self)
        self.velx = 0
        vertical_bug_speed = 15
        self.vely = vertical_bug_speed
        self.jumping, self.go_down = False,False

    def motion(self, SCREEN_WIDTH, SCREEN_HEIGHT):

        predicted_location = self.rect.x + self.velx

        if predicted_location < 0:
            self.velx = 0
        elif predicted_location + self.width > SCREEN_WIDTH:
            self.velx = 0

        self.rect.x +=self.velx

        self.__jump(SCREEN_HEIGHT)

    def __jump(self, SCREEN_HEIGHT):

        max_jump = 150

        if self.jumping:
            if self.rect.y <= max_jump:
                self.go_down = True
            if self.go_down:
                predicted_location = self.rect.y + (self.vely*2)

                if predicted_location + self.height >= SCREEN_HEIGHT:
                    self.go_down = False
                    self.jumping = False
                    
                self.rect.y += self.vely
            else:
                self.rect.y -= self.vely
                
            

class Fly(Baseclass):

    List = pygame.sprite.Group()

    def __init__(self,x,y,width,height,image_string):
        Baseclass.__init__(self,x,y,width,height,image_string)
        Fly.List.add(self)
        self.velx = randint(4,7)
        self.vely = 5
        self.amplitude, self.period = randint(50, 170), randint(4,5)/70.0
        self.health = 100
        self.primary_hit = self.health/2.0
        self.frozen = None
        self.frost_hit = 0

    def go_down(self):
        self.rect.y +=self.vely
        
    @staticmethod
    def update_all(SCREEN_WIDTH, SCREEN_HEIGHT):
        for fly in Fly.List:
            if fly.health <=0:
                fly.image = pygame.image.load("burnt_fly.png")
                fly.go_down()
                if fly.rect.y + fly.height >= SCREEN_HEIGHT:
                    fly.destroy(Fly)

            elif fly.frozen == True and fly.frost_hit >=2:
                fly.go_down()
                if fly.rect.y + fly.height >= SCREEN_HEIGHT:
                    fly.destroy(Fly)
            else:
                fly.fly(SCREEN_WIDTH)


    def fly(self, SCREEN_WIDTH):

        if self.rect.x + self.width > SCREEN_WIDTH or self.rect.x < 0:
            self.image = pygame.transform.flip(self.image, True, False)
            self.velx = -self.velx
        self.rect.x += self.velx

        #a*sin(bx +c)+y
        self.rect.y = self.amplitude * sin(self.period * self.rect.x) + 200

##    @staticmethod
##    def movement(SCREEN_WIDTH):
##        for fly in Fly.List:
##            fly.fly(SCREEN_WIDTH)


class BugProjectile(Baseclass):
    
    List = pygame.sprite.Group()
    
    def __init__(self,x,y,width,height,proj_type,image_string):
        Baseclass.__init__(self,x,y,width,height,image_string)
        BugProjectile.List.add(self)
        self.velx = 0
        self.proj_type = proj_type

    def destroy(self):
        BugProjectile.List.remove(self)
        Baseclass.allsprites.remove(self)
        del self 

    @staticmethod
    def movement():
        for projectile in BugProjectile.List:
            projectile.rect.x += projectile.velx







        
