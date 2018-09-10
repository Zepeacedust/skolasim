import pygame, sys
pygame.init()
screen = pygame.display.set_mode((200,200))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN: print("KEYDOWN")
        print(event.type)