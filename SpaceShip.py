from Bullets import Bullet

class SpaceShip():

    class FirstWeapon():

        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.listOfBullets = []

        def runToShoot(self, spaceShip_x):
            self.ShootBullet(spaceShip_x)

        def run(self):
            self.showBullets()
            self.deleteBullet()

        def showBullets(self):
            for bullet in self.listOfBullets:
                bullet.show()

        def deleteBullet(self):
            for bullet in self.listOfBullets[:]:
                if bullet.y < 0 or bullet.x < 0 or bullet.x > width:
                    self.listOfBullets.remove(bullet)

        def ShootBullet(self, spaceShip_x):
            self.x = spaceShip_x
            self.listOfBullets.append(Bullet(self.x, self.y, 10, 10, 35))

    class Hp():

        def __init__(self, x, y, w, h):
            self.x = x
            self.y = y
            self.wRect = w
            self.h = h

            self.wHp = w

        def run(self):
            self.showRect()
            self.showHp()
            self.showHpCounter()

        def showRect(self):
            noFill()
            rect(self.x, self.y, self.wRect, self.h)

        def showHp(self):
            fill(255,0,0)
            rect(self.x, self.y, self.wHp, self.h)

        def showHpCounter(self):
            fill(0,0,0)
            text(str(self.wHp), self.x-35, self.y+35)
            text('%', self.x+20, self.y+35)

    class Score():

        def __init__(self, x, y, msgScore):
            self.x = x
            self.y = y
            self.msgScore = msgScore
            self.allowPlusScorePlayer = False

        def run(self):
            self.show()
            self.count()

        def show(self):
            fill(0,0,0)
            text(str(self.msgScore), self.x, self.y)
            text('Score:', self.x-75, self.y)

        def count(self):
            if self.allowPlusScorePlayer:
                self.msgScore += 1


    def __init__(self, x, y, w, h, speed):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = speed
        self.skin = loadImage('image/spaceship.png')
        self.firstWeapon = SpaceShip.FirstWeapon(self.x, self.y)
        self.hp = SpaceShip.Hp(width/2+400, height-175, 100, 25)
        self.score = SpaceShip.Score(width-100, 100, 0)
        self.state = 'ShootWithFirstGun'
        self.dropedSecondWeapon = None
        self.secondWeapon = None
        self.secondWeaponTimer = None
        self.enemy = None

    def run(self):
        self.show()
        self.move()
        self.distationWall()
        self.killEnemy()
        self.hp.run()
        self.score.run()
        self.stateToShoot()
        self.takeSecondGun()
        self.getDamageDist()

    def show(self):
        image(self.skin, self.x, self.y, self.w, self.h)

    def setSecondWeapon(self, weapon):
        self.secondWeapon = weapon

    def setEnemy(self, enemy):
        self.enemy = enemy

    def setDropedSecondWeapon(self, dropWeapon):
        self.dropedSecondWeapon = dropWeapon

    def setSecondWeaponTimer(self, timer):
        self.secondWeaponTimer = timer

    def setGameState(self, gameState):
        if self.hp.wHp <= 0:
            self.hp.wHp = 100
            gameState = False
        else:
            gameState = True
        return gameState

    def move(self):
        if keyPressed:
            if key == 'a':
                self.x -= self.speed
            elif key == 'd':
                self.x += self.speed

    def getDamageDist(self):
        try:
            if (self.enemy.x > self.x-self.w/2 and self.enemy.x < self.x+self.w/2 and
                self.enemy.y > self.y-self.h/2 and self.enemy.y < self.y+self.h/2):
                self.hp.wHp -= 1
        except AttributeError:
            pass

    def killEnemy(self):
        if self.enemy.hp.wHp <= 0:
            self.score.allowPlusScorePlayer = True
            self.enemy.spawn()
        else:
            self.score.allowPlusScorePlayer = False

    def takeSecondGun(self):
        try:
            if (self.dropedSecondWeapon.x > self.x-self.w/2 and self.dropedSecondWeapon.x < self.x+self.w/2  and 
                self.dropedSecondWeapon.y > self.y-self.h/2 and self.dropedSecondWeapon.y < self.y+self.h/2):
                self.state = 'ShootWithSecondGun'
                self.secondWeaponTimer.__init__(0+200, height-75, 100, 50, 0.5)
                self.dropedSecondWeapon.y = -10000
        except AttributeError:
            pass

    def stateToShoot(self):
        if self.state == 'ShootWithFirstGun':
            self.firstWeapon.run()
        elif self.state == 'ShootWithSecondGun':
            try:
                self.state = self.secondWeaponTimer.endOfTimer()
                self.secondWeapon.run()
                self.secondWeaponTimer.run()
            except AttributeError:
                pass

    def distationWall(self):
        if self.x-self.w/2 - 0 < self.speed:
            self.x = self.w/2
        elif width - self.x-self.w/2 < self.speed:
            self.x = width-self.w/2
