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
    fondo = pygame.image.load("assets/fondoperdido.png").convert()
    fondo = pygame.transform.scale(fondo, (1000, 700))
    # inicializamos el reloj
    clock = pygame.time.Clock()
    font1 = pygame.font.Font("assets/fuente.ttf", 35)
    font2=pygame.font.Font("assets/fuente.ttf", 50)
    decir_volver_jugar = font1.render(f"VOLVER A JUGAR", True, (0, 0, 0))
    decir_volver_jugar_rect = decir_volver_jugar.get_rect(
        center=(screen.get_width()-1353 // 2, screen.get_height() // 2 + 125)
    )
    decir_salir = font2.render(f"SALIR", True, (0, 0, 0))
    decir_salir_rect = decir_salir.get_rect(
    center=(screen.get_width()-650 // 2, screen.get_height() // 2 + 125)
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
                if decir_salir_rect.collidepoint(event.pos):
                    running = False
                if decir_volver_jugar_rect.collidepoint(event.pos):
                    game_scene.gameloop(screen)

        # limpiar pantalla (fondo negro)
        screen.blit(fondo, [0, 0])
        screen.blit(decir_volver_jugar, decir_volver_jugar_rect)
        screen.blit(decir_salir, decir_salir_rect)
        # actualizar pantalla
        pygame.display.flip()
        
        # limitar FPS
        clock.tick(30)