if __name__ == "__main__": # Solo para que no ejecutes este archivo
    import sys
    print(
        "\033[38;2;255;0;0mESTE MODULO NO DEBE EJECUTARSE. EJECUTAR main.py\033[0m\n"
        * 3
    )
    sys.exit()

import pygame
import scenes.game_scene as game_scene
from pygame.locals import (K_ESCAPE, KEYDOWN, QUIT)

def gameloop(screen):

    # inicializamos el reloj
    clock = pygame.time.Clock()

    running = True

    # fuente y texto
    font = pygame.font.Font(None, 48)
    line1 = font.render("Estamos en basic_scene", True, (255, 255, 255))
    line2 = font.render("Aprieta ESC para salir de esta escena", True, (255, 255, 255))
    line3 = font.render("Has muerto xd", True, (255, 255, 255))

    # posiciones
    line1_rect = line1.get_rect(
        center=(screen.get_width() // 2, screen.get_height() // 2 - 25)
    )

    line2_rect = line2.get_rect(
        center=(screen.get_width() // 2, screen.get_height() // 2 + 25)
    )
    line3_rect = line3.get_rect(
        center=(screen.get_width() // 2, screen.get_height() // 2 + 80)
    )
    # loop principal
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == KEYDOWN:
                    game_scene.gameloop(screen)
            elif event.type == QUIT:
                running = False

        # limpiar pantalla (fondo negro)
        screen.fill((0, 0, 0))

        # dibujar textos
        screen.blit(line1, line1_rect)
        screen.blit(line2, line2_rect)
        screen.blit(line3, line3_rect)

        # actualizar pantalla
        pygame.display.flip()

        # limitar FPS
        clock.tick(30)