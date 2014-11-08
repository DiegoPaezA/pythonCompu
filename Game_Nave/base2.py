# coding=utf-8

__author__ = 'diegopaez'
"""
 Show how to use a sprite backed by a graphic.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Posición de partida del rectángulo
rect_x = 50
rect_y = 50

# Velocidad y rumbo del rectángulo
rect_cambio_x = 5
rect_cambio_y = 5


# Create an empty array
snow_list = []

# Loop 50 times and add a snow flake in a random x,y position
for i in range(50):
    x = random.randrange(0, 400)
    y = random.randrange(0, 400)
    snow_list.append([x, y])

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

    # --- Game logic should go here

    # --- Drawing code should go here

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLACK)
    # Dibuja un rectángulo rojo dentro del blanco
    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50])
    pygame.draw.rect(screen, RED, [rect_x + 10, rect_y + 10 ,30, 30])    # Desplaza el punto de partida del rectángulo
    rect_x += rect_cambio_x
    rect_y += rect_cambio_y

    # Rebota al rectángulo si es necesario
    if rect_y > 450 or rect_y < 0:
        rect_cambio_y = rect_cambio_y * -1

    if rect_x > 650 or rect_x < 0:
        rect_cambio_x = rect_cambio_x * -1


     # Process each snow flake in the list
    for i in range(len(snow_list)):

        # Draw the snow flake
        pygame.draw.circle(screen, WHITE, snow_list[i], 2)

        # Move the snow flake down one pixel
        snow_list[i][1] += 1

        # If the snow flake has moved off the bottom of the screen
        if snow_list[i][1] > 400:
            # Reset it just above the top
            y = random.randrange(-50, -10)
            snow_list[i][1] = y
            # Give it a new x position
            x = random.randrange(0, 400)
            snow_list[i][0] = x


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
