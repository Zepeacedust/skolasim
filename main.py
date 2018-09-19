import pygame, humans
pygame.init()
x = humans.student(200, 200)
y = humans.student(200, 200)
x.connect(y, 200)
print(x.connections)
print(y.connections)