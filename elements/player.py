if __name__ == "__main__": # Solo para que no ejecutes este archivo
    import sys
    print(
        "\033[38;2;255;0;0mESTE MODULO NO DEBE EJECUTARSE. EJECUTAR main.py\033[0m\n"
        * 3
    )
    sys.exit()

import pygame
from pygame.locals import (K_a, K_d, RLEACCEL)

from elements.bullet import Bullet

POU_IMG = pygame.image.load('assets/JorgePou.png')
POU_IMG_scaled = pygame.transform.scale(POU_IMG, (140, 140))

class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        # nos permite invocar métodos o atributos de Sprite
        super(Player, self).__init__()
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        self.surf = POU_IMG_scaled
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect(center=(self.screen_width // 2, self.screen_height - 20))
        # POR HACER (2.3): Lista de proyectiles
        self.projectiles = pygame.sprite.Group()


    def update(self, pressed_keys):
        if pressed_keys[K_a]:
            self.rect.move_ip(-8.5, 0)
        if pressed_keys[K_d]:
            self.rect.move_ip(8.5, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.screen_height:
            self.rect.bottom = self.screen_height

        # POR HACER (2.3): Actualizar las balas
        self.projectiles.update()

    def shoot(self, mouse_pos):
        x_distance = mouse_pos[0] - self.rect.centerx
        y_distance = mouse_pos[1] - self.rect.centery
        length = ((mouse_pos[0] - self.rect.centerx) ** 2 + (mouse_pos[1] - self.rect.centery) ** 2) ** (1 / 2)
        direction = (x_distance / length, y_distance / length)
        # POR HACER (2.3): Crear bala y calcular su direccion
        bullet = Bullet(self.rect.center, direction, self.screen_width, self.screen_height)
        self.projectiles.add(bullet)
        