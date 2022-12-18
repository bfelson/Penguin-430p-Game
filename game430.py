'''
Class 1: Ends 30:36
1. Import and init
2. Create display surface
3. main event loop
4. quit and update
5. clock
6. Non-display surfaces 
'''

'''
Class 2: Ends 45:23
1. Fix screen.blit line
2. Import Image, replace test_surface
3. Text Surface
4. Resize Surfaces
5. Animating Surfaces
6. Collisions with wall
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

#Surfaces with text
font_type = 'assets/fonts/MinecraftRegular-Bmg3.otf'
font_size = 50
test_font = pygame.font.Font(font_type, font_size)

text_surface = test_font.render('Message', True, 'White') #format is (text, anti-aliasing (bool), color)

#Non-display surfaces
amongus_surface = pygame.image.load('assets/graphics/among_us_guy.png')
amongus_surface = pygame.transform.rotozoom(amongus_surface ,0, 0.1)
amongus_x = 10; amongus_y = 10
amongus_xSpeed = 2; amongus_ySpeed = 2

background_surface = pygame.image.load('assets/graphics/space_background.png')
background_surface = pygame.transform.rotozoom(background_surface, 0, 2)



#main event loop
while True:
    #check player inputs
    for event in pygame.event.get():
        #quit
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() #need to get out of the loop, otherwise will throw an error


    #draw all elements
    screen.blit(background_surface, ((0,0)))
    screen.blit(amongus_surface, ((amongus_x, amongus_y)))    #displays surfaces on screen at given position
    screen.blit(text_surface, ((WIDTH/2 - text_surface.get_width()/2, HEIGHT/2 - text_surface.get_height()/2)))

    #Animating (Updating coordinates)
    if amongus_x > WIDTH-amongus_surface.get_width() or amongus_x < 0:
        amongus_xSpeed *= -1.1
 
    if amongus_y > HEIGHT-amongus_surface.get_height() or amongus_y < 0:
        amongus_ySpeed *= -1.1

    amongus_x += amongus_xSpeed
    amongus_y += amongus_ySpeed
 #   print("x: ", amongus_x, "\t y: ", amongus_y)

    #update everything

    pygame.display.update() #updates display surface (screen)
    clock.tick(60)  #runs at 60fps MAXIMUM (explain framerates)