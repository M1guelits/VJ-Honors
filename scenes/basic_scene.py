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
    fondo = pygame.image.load("assets/fondoprincipio.png").convert()
    fondo = pygame.transform.scale(fondo, (1000, 700))
    # inicializamos el reloj
    clock = pygame.time.Clock()
    font = pygame.font.Font("assets/fuente.ttf", 80)
    decir_jugar = font.render(f"JUGAR", True, (0, 0, 0))
    decir_jugar_rect = decir_jugar.get_rect(
        center=(screen.get_width() // 2, screen.get_height() // 2 + 50)
    )
    running = True
    # loop principal
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if decir_jugar_rect.collidepoint(event.pos):
                    running = False

        # limpiar pantalla (fondo negro)
        screen.blit(fondo, [0, 0])
        screen.blit(decir_jugar, decir_jugar_rect)
        # actualizar pantalla
        pygame.display.flip()
        
        # limitar FPS
        clock.tick(30)