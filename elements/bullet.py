if __name__ == "__main__": # Solo para que no ejecutes este archivo
    import sys
    print(
        "\033[38;2;255;0;0mESTE MODULO NO DEBE EJECUTARSE. EJECUTAR main.py\033[0m\n"
        * 3
    )
    sys.exit()

import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, direction, screen_width, screen_height):
        super(Bullet, self).__init__()
        # POR HACER (2.0): Aspecto inicial de nuestra bala
        self.surf = pygame.Surface((10, 10)) # Tamaño de la bala
        self.surf.fill((255, 255, 255)) # Color de la bala
        self.rect = self.surf.get_rect(center=pos)

        # POR HACER (2.1): Variables requeridas por nuestra bala
        self.direction = direction
        self.speed = 20
        self.screen_width = screen_width
        self.screen_height = screen_height

    def update(self):
        # POR HACER (2.2): Mover la bala y destruirla si se sale de la pantalla
        self.rect.move_ip(self.direction[0] * self.speed, self.direction[1] * self.speed)
        if (self.rect.right < 0 or self.rect.left > self.screen_width or
            self.rect.bottom < 0 or self.rect.top > self.screen_height):
            self.kill()