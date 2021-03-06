class Enemy():

    class Hp():

        def __init__(self, x, y, w, h):
            self.x = x
            self.y = y
            self.wRect = w
            self.h = h

            self.wHp = w

        def run(self, enemyX, enemyY):
            self.showRect(enemyX, enemyY)
            self.showHp()

        def showRect(self, enemyX, enemyY):
            noFill()
            self.x = enemyX
            self.y = enemyY-65
            rect(self.x, self.y, self.wRect, self.h, 3)

        def showHp(self):
            fill(255,0,0)
            rect(self.x, self.y, self.wHp, self.h, 3)


    def __init__(self, x, y, w, h, speed):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = speed
        self.skin = loadImage('image/nlo.png')
        self.hp = Enemy.Hp(self.x, self.y, self.w, 10)
        self.listOfBullets = []

    def run(self, firstWeaponListOfBullets, secondWeaponListOfBullets):
        self.show()
        self.hp.run(self.x, self.y)
        self.setBullets(firstWeaponListOfBullets, secondWeaponListOfBullets)
        self.giveDamageToEnemy()
        self.distationToHeight()

    def giveDamageToEnemy(self):
        for bullet in self.listOfBullets:
            if bullet.x > self.x-self.w/2 and bullet.x < self.x+self.w/2 and bullet.y > self.y-self.h/2 and bullet.y < self.y+self.h/2:
                self.hp.wHp -= 5

    def setBullets(self, firstWeaponListOfBullets, secondWeaponListOfBullets):
        self.listOfBullets = []
        for bullet in firstWeaponListOfBullets:
            self.listOfBullets.append(bullet)
        for bullet in secondWeaponListOfBullets:
            self.listOfBullets.append(bullet)

    def show(self):
        self.y += self.speed
        image(self.skin, self.x, self.y, self.w, self.h)

    def KillSpaceShip(self):
        pass

    def spawn(self):
        self.y = -300
        self.x = random(0+75/2, width-75/2)
        self.hp.wHp = 75

    def distationToHeight(self):
        if self.y > height:
            self.spawn()
