if __name__ == "__main__": # Solo para que no ejecutes este archivo
    import sys
    print(
        "\033[38;2;255;0;0mESTE MODULO NO DEBE EJECUTARSE. EJECUTAR main.py\033[0m\n"
        * 3
    )
    sys.exit()

import pygame
from pygame.locals import (K_ESCAPE, KEYDOWN, QUIT)

def gameloop(screen):

    # inicializamos el reloj
    clock = pygame.time.Clock()

    running = True

    # fuente y texto
    font = pygame.font.Font(None, 48)
    line1 = font.render("Estamos en basic_scene", True, (255, 255, 255))
    line2 = font.render("Aprieta ESC para salir de esta escena", True, (255, 255, 255))

    # posiciones
    line1_rect = line1.get_rect(
        center=(screen.get_width() // 2, screen.get_height() // 2 - 25)
    )

    line2_rect = line2.get_rect(
        center=(screen.get_width() // 2, screen.get_height() // 2 + 25)
    )

    # loop principal
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False

        # limpiar pantalla (fondo negro)
        screen.fill((0, 0, 0))

        # dibujar textos
        screen.blit(line1, line1_rect)
        screen.blit(line2, line2_rect)

        # actualizar pantalla
        pygame.display.flip()

        # limitar FPS
        clock.tick(30)