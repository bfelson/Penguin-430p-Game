'''
Class 1: Ends 30:36
1. Import and init
2. Create display surface
3. main event loop
4. quit and update
5. clock
6. Non-display surfaces 
'''

import pygame
from sys import exit #using to quit the program effectively

pygame.init() #necessary to run before any other code, initiates the library so to speak

#create display surface
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))   #creates an actual window of size width, height
#after above code, window should open briefly, but just for a second. we need to make it run forever

#Create a title
pygame.display.set_caption("Ben's 4:30PM Python Game")

#Clock Creation
clock = pygame.time.Clock() #clock object

#Non-display surfaces
test_width = 100
test_height = 200
test_surface = pygame.Surface((WIDTH/2 - test_width/2, HEIGHT/2 - test_height/2))    #creates surface with given height and width
test_surface.fill('cyan')   #need to change color so it displays on black background



#main event loop
while True:
    #check player inputs
    for event in pygame.event.get():
        #quit
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() #need to get out of the loop, otherwise will throw an error


    #draw all elements
    screen.blit(test_surface, (0,0))    #displays surfaces on screen at given position

    #update everything

    pygame.display.update() #updates display surface (screen)
    clock.tick(60)  #runs at 60fps MAXIMUM (explain framerates)