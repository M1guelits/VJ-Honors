import scenes.basic_scene as basic_scene
import scenes.game_scene as game_scene
import scenes.muerte_scene as muerte_scene
import pygame




""" Inicializamos PYGAME"""
pygame.init()

pygame.mixer.music.load('assets/musica_pou.mp3')
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)


# 1.- Definimos las medidas de nuestra pantalla
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

# 2.-  Creamos nuestro objeto pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

"""Aqui se ejecutaran las escenas del juego en orden"""
basic_scene.gameloop(screen)
game_scene.gameloop(screen)
muerte_scene.gameloop(screen)