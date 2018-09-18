import pygame
pygame.init()
class student():# 7
    def __init__(self):
        self.connections = []
    def connect(self, target, score):
        self.connections.append((target, score))
        target.connections.append((self, score))
        if target == y:
            print("yee boi")