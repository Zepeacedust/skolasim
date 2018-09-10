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

    def scooch(self):
        self.hitbox = self.hitbox.move(self.speed)
        if self.hitbox.left < 0 or self.hitbox.right > width:
            self.speed[0] = -self.speed[0]
        if self.hitbox.top < 0 or self.hitbox.bottom > height:
            self.speed[1] = -self.speed[1]

    def paste(self):
        screen.blit(ball, self.hitbox)
    
    def doodle(self, bean):
        print(bean)
x = orb(3, 3, [1,1])
balls = [orb(100, 200, [5,1])]
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit() 
    balls[0].scooch()
    balls[0].paste()
    pygame.display.flip()
