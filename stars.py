
class Stars():

    class Star():
    
        def __init__(self, x, y, w, h, speed):
            self.x = x
            self.y = y
            self.w = w
            self.h = h
            self.speed = speed

        def run(self):
            self.show()
            self.spawn()

        def show(self):
            self.y += 1
            fill(255,255,255)
            rect(self.x, self.y, self.w, self.h)

        def spawn(self):
            if self.y > height:
                self.x = random(25, width-25)
                self.y = random(0, -500)


    def __init__(self):
        self.listOfStars = []
        for _ in range(0, 10):
            self.listOfStars.append(Stars.Star(random(25, width-25), random(25, height/2), 15, 15, 5))

    def run(self):
        for star in self.listOfStars:
            star.run()
