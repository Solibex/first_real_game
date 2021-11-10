import pygame

pygame.init()


class main:
    def loop():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


class images:
    icon = pygame.image.load('data/gfx/logo.png')
    player = pygame.image.load('data/gfx/player.png')

class data:
    caption = 'smile yez'
    canvas = (500, 500)

screen = pygame.display.set_mode(data.canvas)
pygame.display.set_caption(data.caption)
pygame.display.set_icon(images.icon)

while True:
    main.loop()
