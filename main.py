import pygame, humans, sys
pygame.init()
x = humans.student(200, 200, 7)
y = humans.student(000, 600, 7)
z = humans.student(600, 000, 7)
x.connect(y, 200)
school = pygame.display.set_mode((800, 800))
school.fill((255,255,255))

print(x.connections)
print(y.connections)
while 1:#gameplay loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    school.blit(x.image, x.rect)
    school.blit(y.image, y.rect)
    school.blit(z.image, z.rect)
    pygame.display.flip()
    print(x.moveto(y))
    z.move(z.moveto(x))
    x.move(x.moveto(y))
    y.move((1, 0))
    pygame.time.Clock().tick(60)