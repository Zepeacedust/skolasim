import pygame, sys

pygame.init()
proceed = True
screen = pygame.display.set_mode((255,255))
while proceed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    pygame.display.flip
    print(pygame.key.get_pressed())