import sys, pygame, random


ball = pygame.image.load("blip.jpeg")

pygame.init()

size = width, height = 750, 750

black = 255, 255, 255

screen = pygame.display.set_mode(size)

screen.fill(black)

class orb():
    def __init__(self, spawn_x, spawn_y, speed):
        self.hitbox = ball.get_rect(center = (spawn_x, spawn_y))
        self.speed = speed

    def scooch(self):#hreifa hitboxið og checka border collisions
        self.hitbox = self.hitbox.move(self.speed)
        if self.hitbox.left < 0 or self.hitbox.right > width:
            self.speed[0] = -self.speed[0]
        if self.hitbox.top < 0 or self.hitbox.bottom > height:
            self.speed[1] = -self.speed[1]

    def paste(self):#updatea skjáinnn
        screen.blit(ball, self.hitbox)
    
    def doodle(self, bean):
        print(bean)
x = orb(3, 3, [1,1])
balls = [orb(100, 200, [5,1])]
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit() 
    balls[0].scooch()
    buttons = pygame.key.get_pressed()
    if buttons[300] == 1:balls[0].paste()
    balls[0].speed = [buttons[275] - buttons[276], buttons[274] - buttons[273]]
    if buttons[32] == 1: screen.fill(black)
    pygame.display.flip()