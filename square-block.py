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
width = height = 45
vel = 1

win.fill((255,165,0))

jump = True
active = True
jump_count = 1

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

    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
        random_colour()
        
    if keys[pygame.K_RIGHT] and x < 355:
        x += vel
        random_colour()
    
    if not(jump):
        if keys[pygame.K_UP] and y > 0:
            y -= vel
            random_colour()
            
        if keys[pygame.K_DOWN] and y < 355:
            y += vel
            random_colour()
            
        if keys[pygame.K_SPACE]:
            jump = True

    else:
        if jump_count >= -10:
            y -= (jump_count ** 2) * 0.5
            jump_count -= 1

        else:
            jump = False
            jump_count = 10

    pygame.draw.rect(win, (255, 0, 255), (x, y, width, height))
    pygame.display.update()

pygame.quit() 