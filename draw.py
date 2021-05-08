import pygame

# Initialising pygame 
pygame.init()

# Creating window
win = pygame.display.set_mode((500, 500))

# Window caption.
pygame.display.set_caption("Pixel Draw")

# Defining variables needed in when creating movement
x = y = 230
width = height = 40
vel = 1

win.fill((30,144,255))

# Create main window.

active = True
while active:
    # Time delay for movement.
    pygame.time.delay(10)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
            
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        x -= vel
        
    if keys[pygame.K_RIGHT]:
        x += vel
        
    if keys[pygame.K_UP]:
        y -= vel
        
    if keys[pygame.K_DOWN]:
        y += vel

    pygame.draw.rect(win, (255,140,0), (x, y, width, height))
    pygame.display.update()
            
pygame.quit()