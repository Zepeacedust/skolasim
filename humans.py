import pygame     
pygame.init()

class student(pygame.sprite.Sprite):#generic social humanoid
    def __init__(self, X, Y, Personality_type):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./sprites/test.JPEG")
        self.rect = self.image.get_rect(x = X,y = Y)#get_rect tekur bara x og y sem keywords
        self.pers = Personality_type
        self.connections = {}
        self.x_undermove = 0
        self.y_undermove = 0
    def connect(self, target, score):
        self.connections[target] = 1 / (1 + abs(self.pers - target.pers)) * score#lætur fólk mep líkan persónuleika verða vinir hraðar
        target.connections[self] = 1 / (1 + abs(self.pers - target.pers)) * score
    def move(self,  speed):#frábær bit af code sem leifir non integer movement
        self.x_undermove = int(speed[0] + self.x_undermove) * -1 + speed[0] + self.x_undermove
        self.y_undermove = int(speed[1] + self.y_undermove) * -1 + speed[1] + self.y_undermove
        fast = (speed[0] + self.x_undermove, speed[1] + self.y_undermove)
        self.rect = self.rect.move(fast)
