import pygame
pygame.init()

class student(pygame.sprite.Sprite):#generic social humanoid
    def __init__(self, x, y):
        pygame.sprite.Sprite().__init__(self)
        self.image = pygame.surface([3, 3])
        self.image.fill(0,0,0)
        self.rect = self.image.get_rect()
        self.connections = []
        self.coords = [X, Y]
    def connect(self, target, score):
        self.connections.append((target, score))
        target.connections.append((self, score))