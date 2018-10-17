#Bugstar

import pygame, sys
from classes import *
import random

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),0,32)
clock = pygame.time.Clock()
FPS = 24
total_frames = 0
projectile_direction = "right" 


background = pygame.image.load("forest.png")

##colour1 =(22,122,211)
##colour2 =(0,44,166)
##colour3 =(34,55,245)

bug_width, bug_height, bug_startx = 60,60,10
bug = Bug(bug_startx, SCREEN_HEIGHT-bug_height,bug_width,bug_height,"bug.png")

fly_width, fly_height = 40,40

def spawn(FPS, total_frames):
    fly_starty = 140
    half_second = FPS /2 
    if total_frames % half_second == 0:
        r = random.randint(1,2)

        x = 1
        if r == 2:
            x = SCREEN_WIDTH - fly_width
        fly = Fly(x,fly_starty, fly_width,fly_height,"fly.png")

def collision():
##    for fly in Fly.List:
##        if pygame.sprite.spritecollide(fly, BugProjectile.List, False):
##            if BugProjectile.fire:
##                fly.health -= fly.primary_hit
##            else:
##                fly.velx = 0
##
##    for projectile in BugProjectile.List:
##        if pygame.sprite.spritecollide(projectile, Fly.List, False):
##            projectile.destroy()
##        
    for fly in Fly.List:
        projectiles = pygame.sprite.spritecollide(fly, BugProjectile.List, True)
        for projectile in projectiles:
            if projectile.proj_type == "fire":
                fly.health -= fly.primary_hit
                if fly.health <= 0:
                    fly.image = pygame.image.load("burnt_fly.png")
            elif projectile.proj_type == "frost":
                fly.frozen = True
                fly.frost_hit +=1
                if fly.velx > 0:
                    fly.image = pygame.image.load("frozen_fly.png")
                    fly.velx = 0
                    fly.go_down
                elif fly.velx < 0:
                    fly.image = pygame.image.load("frozen_fly.png")
                    fly.image = pygame.transform.flip(fly.image, True, False)
                    fly.velx = 0
                    fly.go_down()
      

while True:
    
    #EVENTS
    spawn(FPS, total_frames)
    collision()
                
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        projectile_direction = "right"
        bug.image = pygame.image.load("bug.png")
        bug.velx = 5
    elif keys[pygame.K_LEFT]:
        projectile_direction = "left" 
        bug.image = pygame.image.load("bug back.png")
        bug.velx = -5
    else:
        bug.velx = 0

    if keys[pygame.K_UP]:
        bug.jumping = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            def direction():
                if projectile_direction == "right":
                    p.velx = 20
                elif projectile_direction == "left":
                    p.image = pygame.transform.flip(p.image, True, False)
                    p.velx = -20
            if event.key == pygame.K_SPACE:
                BugProjectile.fire = True
                p = BugProjectile(bug.rect.x, bug.rect.y,40,30,"fire","fire.png")
                direction()
                

            if event.key == pygame.K_b:
                p = BugProjectile(bug.rect.x, bug.rect.y, 40,30,"frost","frost.png")
                direction()
                

    

    #EVENTS

        
    #LOGIC
    bug.motion(SCREEN_WIDTH, SCREEN_HEIGHT)
##    Fly.movement(SCREEN_WIDTH)
    Fly.update_all(SCREEN_WIDTH, SCREEN_HEIGHT)
    BugProjectile.movement()
    total_frames +=1
    
    #LOGIC
    
    #DRAW
    screen.blit(background, (0,0))
    Baseclass.allsprites.draw(screen)

    pygame.display.flip()

    #DRAW

    clock.tick(FPS)
