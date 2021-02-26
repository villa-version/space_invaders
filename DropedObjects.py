class DropedObjects():

    class DropedSecondWeapon():

        def __init__(self, x, y, w, h, speed):
            self.x = x
            self.y = y
            self.w = w
            self.h = h
            self.speed = speed
            self.skin = loadImage('image/secondweapon.png')

        def run(self):
            self.show()
            self.spawn()

        def show(self):
            self.y += self.speed
            image(self.skin, self.x, self.y, self.w, self.h)

        def spawn(self):
            if self.y > height:
                self.x = random(0+25, width-25)
                self.y = -10000

    class DropedArmor():

        def __init__(self, x, y, w, h, speed):
            self.x = x
            self.y = y
            self.w = w
            self.h = h
            self.speed = speed
            self.skin = loadImage('image/armor.png')

        def run(self):
            self.show()
            self.spawn()

        def spawn(self):
            if self.y > height:
                self.x = random(0+25, width-25)
                self.y = -8000

        def show(self):
            self.y += self.speed
            image(self.skin, self.x, self.y, self.w, self.h)


    def __init__(self, xForSecondWeapon, y, w, h, speed, xForArmor):
        self.xForSecondWeapon = xForSecondWeapon
        self.xForArmor = xForArmor
        self.y = y
        self.w = w
        self.h = h
        self.speed = speed
        self.dropedSecondWeapon = DropedObjects.DropedSecondWeapon(self.xForSecondWeapon, self.y, self.w, self.h, self.speed)
        self.dropedAromor = DropedObjects.DropedArmor(self.xForArmor, self.y, self.w, self.h, self.speed)

    def run(self):
        self.dropedSecondWeapon.run()
        self.dropedAromor.run()
