# coding=utf-8
# Importa  la libraría de funciones llamada 'pygame'
import pygame
# Inicializa el motor de juegos
pygame.init()


# Definir algunos colores
NEGRO   = (   0,   0,   0)
BLANCO  = ( 255, 255, 255)
VERDE   = (   0, 255,   0)
ROJO    = ( 255,   0,   0)

dimensiones = (700, 500)                            # Dimensiones Ventan
pantalla = pygame.display.set_mode(dimensiones)     # Crear Pantalla
pygame.display.set_caption("Super Juego del Profesor Craven") # Titulo de la ventana

#Itera hasta que el usuario pincha sobre el botón de cierre.
hecho = False

# Se usa para gestionar cuan rápido se actualiza la pantalla
reloj = pygame.time.Clock()

# -------- Bucle Principal del Programa -----------
while not hecho:
    # TODOS LOS EVENTOS DE PROCESAMIENTO DEBERÍAN IR DEBAJO DE ESTE COMENTARIO
    for evento in pygame.event.get(): # El usuario hizo algo
        if evento.type == pygame.QUIT: # Si el usuario pincha sobre cerrar
            hecho = True # Marca que indica que hemos acabado y sale de este bucle

    # TODOS LOS EVENTOS DE PROCESAMIENTO DEBERÍAN IR ENCIMA DE ESTE COMENTARIO


    # TODA LA LÓGICA DEL JUEGO DEBERÍA IR DEBAJO DE ESTE COMENTARIO

    # TODA LA LÓGICA DEL JUEGO DEBERÍA IR ENCIMA DE ESTE COMENTARIO


    # TODO EL CÓDIGO DE DIBUJO DEBERÍA IR DEBAJO DE ESTE COMENTARIO

    # TODO EL CÓDIGO DE DIBUJO DEBERÍA IR ENCIMA DE ESTE COMENTARIO

    # Limita a 20 fotogramas por segundo (frames per second)
    reloj.tick(20)
