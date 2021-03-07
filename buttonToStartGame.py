class StartGame():

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.skin = loadImage('image/startgame.png')

    def run(self):
        self.show()

    def show(self):
        image(self.skin, self.x, self.y, self.w, self.h)

    def aiming(self):
        if (self.x-self.w/2 < mouseX and self.x+self.w/2 > mouseX and
            self.y-self.h/2 < mouseY and self.y+self.h/2 > mouseY):
            self.skin = loadImage('image/startgame2.png')
            return True
        else:
            self.skin = loadImage('image/startgame.png')
            return False

    def pressed(self, pressed):
        return (self.x-self.w/2 < mouseX and self.x+self.w/2 > mouseX and
                self.y-self.h/2 < mouseY and self.y+self.h/2 > mouseY and pressed)
