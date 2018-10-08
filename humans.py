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
        self.move_counter = 30
        self.move_angle = 0, 0
    def connect(self, target, score):
        self.connections[target] = 1 / (1 + abs(self.pers - target.pers)) * score#lætur fólk mep líkan persónuleika verða vinir hraðar
        target.connections[self] = 1 / (1 + abs(self.pers - target.pers)) * score
    def move(self,  speed):#frábær bit af code sem leifir non integer movement
        self.x_undermove = -int(speed[0] + self.x_undermove) + speed[0] + self.x_undermove
        self.y_undermove = -int(speed[1] + self.y_undermove) + speed[1] + self.y_undermove
        fast = (speed[0] + self.x_undermove, speed[1] + self.y_undermove)
        self.rect = self.rect.move(fast)
    def moveto(self, target):
        if self.move_counter == 30:
            self.move_counter = 0
            x_dif = self.rect.x - target.rect.x
            y_dif = self.rect.y - target.rect.y
            if x_dif == 0 and y_dif == 0:
                self.move_angle = 0, 0
            else:
                self.move_angle = (-x_dif / abs(max(x_dif, y_dif, key = abs)), -y_dif / abs(max(x_dif, y_dif, key = abs)))
        self.move_counter += 1
        return self.move_angle 
     