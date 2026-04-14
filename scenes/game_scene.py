if __name__ == "__main__": # Solo para que no ejecutes este archivo
    import sys
    print(
        "\033[38;2;255;0;0mESTE MODULO NO DEBE EJECUTARSE. EJECUTAR main.py\033[0m\n"
        * 3
    )
    sys.exit()

import pygame

from pygame.locals import (K_ESCAPE, KEYDOWN, QUIT)

from elements.player import Player

from elements.enemy import Enemy, Boss

from elements.mirilla import Mirilla

from elements.comida import Comida

""""
Este es el modulo game_scene, aqui se encuentra 
la escena en donde ocurre nuestro juego
"""


def gameloop(screen):
    ''' 1.- Definimos el fondo de nuestra escena'''
    background_image = pygame.image.load("assets/fondo_pou.png").convert()
    background_image = pygame.transform.scale(background_image, (1000, 700))

    ''' 2.- generador de enemigos'''
    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 1000)
    ADDFOOD=pygame.USEREVENT+2
    pygame.time.set_timer(ADDFOOD, 1250)
    ''' 3.- creamos la instancia de jugador'''
    player = Player(screen)
    mirilla=Mirilla((25,25), screen.get_width(),screen.get_height())
    ''' 4.- contenedores de enemigos y jugador'''
    enemies = pygame.sprite.Group()
    comidas=pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    all_sprites.add(mirilla)

    clock = pygame.time.Clock()
    ct=0
    font = pygame.font.Font("assets/fuente.ttf", 42)
    contador = font.render(f"Score: {ct}", True, (0, 0, 0))
    contador_rect = contador.get_rect(
        center=(screen.get_width() // 2, screen.get_height() // 2 - 25)
    )
    # variable booleana para manejar el loop
    running = True
    lista =[]
    c=0
    ct=0
    ctperdidos=0

    # loop principal del juego
    while running:
        contador = font.render(f"Score: {ct}   Perdidos: {ctperdidos}/8", True, (0, 0, 0))
        contador_rect = contador.get_rect(
        center=(screen.get_width() // 2, screen.get_height() // 2 - 100)
        )
        screen.blit(background_image, [0, 0])
        screen.blit(contador, contador_rect)
        # iteramos sobre cada evento en la cola
        for event in pygame.event.get():
            # se presiono una tecla?
            if event.type == KEYDOWN:
                # era la tecla de escape? -> entonces terminamos
                if event.key == K_ESCAPE:
                    running = False

            # fue un click al cierre de la ventana? -> entonces terminamos
            elif event.type == QUIT:
                running = False

            # es un evento que agrega enemigos?
            elif event.type == ADDENEMY:
                new_enemy = Enemy(screen)
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)
            elif event.type == ADDFOOD:
                new_food = Comida(screen)
                comidas.add(new_food)
                all_sprites.add(new_food)

            # POR HACER (2.4): Detectar click y disparar
            elif event.type==pygame.MOUSEBUTTONDOWN:
                            if c<8:
                                lista.append(pygame.time.get_ticks())
                                player.shoot(pygame.mouse.get_pos())
                                c+=1
                            else:
                                if pygame.time.get_ticks()-lista[-1]>4000:
                                    c=0
                                    player.shoot(pygame.mouse.get_pos())
            # Dispara un proyectil si el usuario hace click

        # dibujamos todos los sprites
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        # POR HACER (2.5): Pintar balas en pantalla
        for bullet in player.projectiles:
            screen.blit(bullet.surf, bullet.rect)

        # POR HACER (2.5): Destruir balas y bugs si chocan
        pygame.sprite.groupcollide(player.projectiles, enemies, True, True)

        # vemos si algun enemigo a chocado con el jugador
        if pygame.sprite.spritecollide(player, enemies, pygame.sprite.collide_rect_ratio(0.02)):
            player.kill()
            running=False

        if pygame.sprite.spritecollideany(player, comidas, pygame.sprite.collide_rect_ratio(0.70)):
            # si pasa, removemos al jugador y detenemos el loop del juego
            ct+=1
            if ct > 0 and ct % 20 == 0:
                billy_boss = Boss(screen)
                enemies.add(billy_boss)
                all_sprites.add(billy_boss)

            for comida in comidas:
                comida.kill()
                break
        for comida in comidas:
            if comida.rect.top>700:
                ctperdidos+=1
                comida.kill()
        if ctperdidos==8:
             running=False
        # obtenemos todas las teclas presionadas actualmente
        pressed_keys = pygame.key.get_pressed()
        # actualizamos el sprite del jugador basado en las teclas presionadas
        player.update(pressed_keys)
        # actualizamos los enemigos
        enemies.update()
        mirilla.update()
        comidas.update()
        # actualizamos la interfaz
        pygame.display.flip()

        clock.tick(60)