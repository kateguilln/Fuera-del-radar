import pygame, os
from pygame.locals import *

# Pantalla
pygame.init()
pygame.display.set_caption("Fuera del Radar")
pygame.display.set_mode((800, 600), pygame.RESIZABLE)
screen = pygame.display.get_surface()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.fill((31, 206, 189))  #Se ve celeste por esta variable
    pygame.display.flip()
