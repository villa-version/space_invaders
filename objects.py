from Bullets import Bullet

class Objects():

    class ArmorIndicator():

        def __init__(self, x, y, w, h, powerProtection, breaking):
            self.x = x
            self.y = y
            self.w = w
            self.h = h
            self.skin = loadImage('image/armor.png')
            self.powerProtection = powerProtection
            self.breaking = breaking

        def run(self):
            self.show()
            self.indicator()
            self.protection()

        def show(self):
            image(self.skin, self.x, self.y, self.w, self.h)

        def indicator(self):
            pass

        def protection(self):
            def breakingAfterProtection(self):
                pass

            breakingAfterProtection(self)

    class SecondWeapon():

        class Timer():

            def __init__(self, x, y, w, h, speed):
                self.x = x
                self.y = y
                self.wRect = w
                self.wTimer = w
                self.h = h
                self.speed = speed

            def run(self):
                self.showRect()
                self.showTimer()

            def showRect(self):
                noFill()
                rect(self.x, self.y, self.wRect, self.h)

            def endOfTimer(self):
                if self.wTimer <= 0:
                    self.x = 0
                    self.y = 0
                    self.wRect = 0
                    self.h = 0
                    self.wTimer = 0
                    self.speed = 0
                    return 'ShootWithFirstGun'

                return 'ShootWithSecondGun'

            def showTimer(self):
                self.wTimer -= self.speed
                fill(0,255,0)
                rect(self.x, self.y, self.wTimer, self.h)

        def __init__(self, x, y, soundGun):
            self.x = x
            self.y = y
            self.listOfBullets = []
            self.soundGun = soundGun

        def run(self):
            self.showBullets()

        def shoot(self, spaceShip_x):
            self.listOfBullets.append(Bullet(spaceShip_x, self.y, 10, 10, 40))
            self.soundGun.play()
            self.soundGun.rewind()

        def showBullets(self):
            for bullet in self.listOfBullets:
                bullet.show()

    def __init__(self, soundGun):
        self.armorIndicator = Objects.ArmorIndicator(width-100, height-75, 100, 75, 0, 0)
        self.secondWeapon = Objects.SecondWeapon(0, height/2+150, soundGun)
        self.secondWeaponTimer = Objects.SecondWeapon.Timer(0, 0, 0, 0, 0)

    def run(self):
        self.armorIndicator.run()
