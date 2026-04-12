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

bug1 = pygame.image.load('assets/bug1.png')
bug1_scaled = pygame.transform.scale(bug1, (45, 45))

bug2 = pygame.image.load('assets/bug2.png')
bug2_scaled = pygame.transform.scale(bug2, (45, 45))

cocacola = pygame.image.load('assets/cocacola.png')
cocacola_scaled = pygame.transform.scale(cocacola, (45, 45))

imagenes_enemigos = [bug1_scaled, bug2_scaled, cocacola_scaled]

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(Enemy, self).__init__()
        self.surf = random.choice(imagenes_enemigos)
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # la posicion inicial es generada aleatoriamente, al igual que la velocidad
        self.rect = self.surf.get_rect(
            center=(random.randint(10, screen.get_width() - 10), screen.get_height() - 800))
        
        self.speed = random.randint(3, 6)



    def update(self):
        self.rect.move_ip(0, self.speed)
        # Destruir a los enemigos
        # si se salen de la pantalla
        if self.rect.top > 700:
            self.kill()

