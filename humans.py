import pygame     
pygame.init()

class student(pygame.sprite.Sprite):#generic social humanoid
    def __init__(self, X, Y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./sprites/test.JPEG")
        self.rect = self.image.get_rect(x = X,y = Y)
        self.connections = []
        self.coords = [X, Y]
    def connect(self, target, score):
        self.connections.append((target, score))
        target.connections.append((self, score))