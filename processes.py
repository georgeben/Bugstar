import pygame, sys

def processes():
    
    while True:
        #EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
