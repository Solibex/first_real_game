import pygame
from pygame.locals import *
from pygame.math import Vector2

pygame.init()

# Classes
class main:
    def loop():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()


class images:
    icon = pygame.image.load('data/gfx/logo.png')
    player = pygame.image.load('data/gfx/player.png')

class data:
    caption = 'smile yez'
    canvas = (500, 500)
# Screen stuff
screen = pygame.display.set_mode(data.canvas)
pygame.display.set_caption(data.caption)
pygame.display.set_icon(images.icon)
screen.fill((255, 255, 255))
# Main loop
while True:
    main.loop()
