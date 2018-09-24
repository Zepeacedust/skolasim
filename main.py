import pygame, humans, sys
pygame.init()
x = humans.student(200, 200, 7)
y = humans.student(200, 200, 7)
x.connect(y, 200)
school = pygame.display.set_mode((400, 400))
school.fill((255,255,255))

print(x.connections)
print(y.connections)
while 1:#gameplay loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    school.blit(x.image, x.rect)
    school.blit(y.image, y.rect)
    pygame.display.flip()
    x.move((22 ,7))
    y.move((22/7, 1))
    pygame.time.Clock().tick(60)