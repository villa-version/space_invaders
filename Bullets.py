class Bullet():

    def __init__(self, x, y, w, h, speed):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = speed

    def show(self):
        self.y -= self.speed
        fill(0,0,0)
        rect(self.x, self.y, self.w, self.h)
