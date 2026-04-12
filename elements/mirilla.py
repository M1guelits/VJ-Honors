if __name__ == "__main__": # Solo para que no ejecutes este archivo
    import sys
    print(
        "\033[38;2;255;0;0mESTE MODULO NO DEBE EJECUTARSE. EJECUTAR main.py\033[0m\n"
        * 3
    )
    sys.exit()

import pygame
MIRILLApng=pygame.image.load("assets/mirilla.png")
MIRILLApng=pygame.transform.scale(MIRILLApng,(100,100))
class Mirilla(pygame.sprite.Sprite):
    def __init__(self, pos, screen_width, screen_height):
        super().__init__()
        self.surf=MIRILLApng.copy()
        self.rect=self.surf.get_rect(center=pos)
        self.screen_width=screen_width
        self.screen_height=screen_height
    def update(self):
        self.rect.center=pygame.mouse.get_pos()