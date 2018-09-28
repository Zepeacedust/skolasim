<<<<<<< HEAD
from menu import valmynd
import humans

valmynd()

x = humans.student()
y = humans.student()
=======
import pygame, humans, sys
pygame.init()
x = humans.student(200, 200, 7)
y = humans.student(200, 600, 7)
>>>>>>> social-attributes
x.connect(y, 200)
school = pygame.display.set_mode((800, 800))
school.fill((255,255,255))

print(x.connections)
print(y.connections)
while 1:#gameplay loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    school.fill((255, 255, 255))
    school.blit(x.image, x.rect)
    school.blit(y.image, y.rect)
    pygame.display.flip()
    print(x.moveto(y))
    x.move(x.moveto(y))
    y.move((+1, 0))
    pygame.time.Clock().tick(60)