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
import math
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
pi = 3.141592653
pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

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
    screen.fill(WHITE)
    # Dibuja en la pantalla una línea verde desde (0,0) hasta (100,100)
    # y 5 píxeles de grosor.

    pygame.draw.line(screen, GREEN, [0,0], [100,100], 5)
    pygame.draw.line(screen, RED, [5,0], [100,105], 5)


    # Dibuja sobre la pantalla varias líneas desde (0,10) hasta (100,110)
    # de 5 píxeles de grosor usando un bucle while
    desplazar_y = 0
    while  desplazar_y < 100:
        pygame.draw.line(screen,RED, [0,10+desplazar_y], [100,110+desplazar_y], 5)
        desplazar_y = desplazar_y + 10

    for i in range(400):

        radianes_x = i / 20
        radianes_y = i / 6

        x = int( 75 * math.sin(radianes_x)) + 200
        y = int( 75 * math.cos(radianes_y)) + 200

        pygame.draw.line(screen,BLACK, [x,y], [x+5,y], 5)

    for desplazamiento_x in range(30,300,30):
        pygame.draw.line(screen,BLACK,[desplazamiento_x,100],[desplazamiento_x-10,90], 2 )
        pygame.draw.line(screen,BLACK,[desplazamiento_x,90],[desplazamiento_x-10,100], 2 )

    # Dibuja un rectángulo.
    pygame.draw.rect(screen,BLACK,[60,260,250,100],2)

    # Representa una elipse, usando un rectángulo como perímetro exterior
    pygame.draw.ellipse(screen,BLACK,[20,120,250,100],2)

    # Representa un arco como parte de una elipse. Usamos radianes para determianr qué
    # ángulo dibujar.
    pygame.draw.arc(screen,GREEN,[300,100,250,200],  pi/2,     pi, 2)
    pygame.draw.arc(screen,BLACK,[300,100,250,200],     0,   pi/2, 2)
    pygame.draw.arc(screen,RED,  [300,100,250,200],3*pi/2,   2*pi, 2)
    pygame.draw.arc(screen,BLACK, [300,100,250,200],    pi, 3*pi/2, 2)

    # Esto dibuja un triángulo usando el comando polygon
    pygame.draw.polygon(screen,BLACK,[[100,100],[0,200],[200,200]],5)

    # Selecciona la fuente. Fuente Default, tamaño 25 pt.
    fuente = pygame.font.Font(None, 25)

    # Reproduce el texto. "True" significa texto suavizado(anti-aliased).
    # El color es Negro. Recordemos que ya hemos definido anteriormente la variable NEGRO
    # como una lista de [0,0,0]
    # Observación: Esta línea crea una imagen de las letras,
    # Pero aún no la pone sobre la pantalla.
    texto = fuente.render("Diego R. Paez",True,BLACK)

    # Coloca la imagen del texto sobre la pantalla en 250x250
    screen.blit(texto, [350,250])


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()