if __name__ == "__main__": # Solo para que no ejecutes este archivo
    import sys
    print(
        "\033[38;2;255;0;0mESTE MODULO NO DEBE EJECUTARSE. EJECUTAR main.py\033[0m\n"
        * 3
    )
    sys.exit()

import pygame
import random
from pygame.locals import (RLEACCEL)

comida1 = pygame.image.load('assets/minion.png')
comida1_scaled = pygame.transform.scale(comida1, (60, 60))

comida2 = pygame.image.load('assets/donapato.png')
comida2_scaled = pygame.transform.scale(comida2, (60, 60))

comida3 = pygame.image.load('assets/coin.png')
comida3_scaled = pygame.transform.scale(comida3, (60, 60))

imagenes_enemigos = [comida1_scaled, comida2_scaled, comida3_scaled]

class Comida(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(Comida, self).__init__()
        self.surf = random.choice(imagenes_enemigos)
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # la posicion inicial es generada aleatoriamente, al igual que la velocidad
        self.rect = self.surf.get_rect(
            center=(random.randint(10, screen.get_width() - 10), screen.get_height() - 800))
        
        self.speed = random.randint(3, 7)



    def update(self):
        self.rect.move_ip(0, self.speed)
        # Destruir a los enemigos
        # si se salen de la pantalla
        if self.rect.top > 700:
            self.kill()
