
class Stars():

    class Star():
    
        def __init__(self, x, y, r, speed):
            self.x = x
            self.y = y
            self.r = r
            self.speed = speed

        def run(self):
            self.show()
            self.spawn()

        def show(self):
            self.y += self.speed
            fill(255,255,255)
            noStroke()
            ellipse(self.x, self.y, self.r, self.r)
            stroke(1)

        def spawn(self):
            if self.y > height:
                self.x = random(25, width-25)
                self.y = random(0, -500)


    def __init__(self):
        self.listOfStars = []
        for _ in range(0, 20):
            self.listOfStars.append(Stars.Star(random(25, width-25), random(0, height), random(5, 10), 0.2))

    def run(self):
        for star in self.listOfStars:
            star.run()
