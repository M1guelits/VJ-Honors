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

pistola = pygame.image.load('assets/pistola.png')
pistola_scaled = pygame.transform.scale(pistola, (150, 150))

imagenes_enemigos = [pistola_scaled]

class Pistola(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(Pistola, self).__init__()
        self.surf = random.choice(imagenes_enemigos)
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # la posicion inicial es generada aleatoriamente, al igual que la velocidad
        self.rect = self.surf.get_rect(
            center=(random.randint(10, screen.get_width() - 10), screen.get_height() - 800))
        self.speed = random.randint(3, 4)



    def update(self):
        self.rect.move_ip(0, self.speed)
        # Destruir a los enemigos
        if self.rect.top > 700:
            self.kill()

        # si se salen de la pantalla