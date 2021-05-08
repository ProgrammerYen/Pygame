import pygame
import random

# Initialising pygame.
pygame.init()

# Creating screen
win = pygame.display.set_mode((400, 400))

# Window caption
pygame.display.set_caption("Square block")

# Assigning values to variables

x = y = 182
width = height = 40
vel = 1

active = True
while active:
    
    # Delays the program by 100 milliseconds before certain movements happen.
    pygame.time.delay(5)
    
    # Allows window to close when the red "x" is pressed.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
    
    # Creating movement in game.
    keys = pygame.key.get_pressed()
    
    # Checking conditions to make character move in specific direction
    
    colours = [(0,191,255), (246, 255, 0), (0, 255, 0)]
    # Making the character move and not increase in size when arrows are pressed.
    def random_colour():
        colour_choice = random.choice(colours)
        win.fill(colour_choice)
        
        # Creating character surface - a square
        pygame.draw.rect(win, (255, 0, 255), (x, y, width, height))
        pygame.display.update()

    if keys[pygame.K_LEFT]:
        x -= vel
        random_colour()
        
    if keys[pygame.K_RIGHT]:
        x += vel
        random_colour()
        
    if keys[pygame.K_UP]:
        y -= vel
        random_colour()
        
    if keys[pygame.K_DOWN]:
        y += vel
        random_colour()
        
    pygame.draw.rect(win, (255, 0, 255), (x, y, width, height))
    pygame.display.update()

pygame.quit() 