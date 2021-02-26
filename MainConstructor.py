from SpaceShip import SpaceShip
from Enemy import Enemy
from objects import Objects
from DropedObjects import DropedObjects
from stars import Stars

class MainConstructor():

    def __init__ (self):
        self.spaceShip = SpaceShip(width/2, height/2+150, 150, 150, 5)
        self.enemy = Enemy(random(0+75/2, width-75/2), -300, 75, 75, 3)
        self.objects = Objects()
        self.spaceShip.setSecondWeapon(self.objects.secondWeapon)
        self.spaceShip.setSecondWeaponTimer(self.objects.secondWeaponTimer)
        self.dropedObjects = DropedObjects(random(0+25, width-25), -2400, 50, 50, 2, random(0+25, width-25))
        self.spaceShip.setDropedSecondWeapon(self.dropedObjects.dropedSecondWeapon)
        self.stars = Stars()

    def run(self):
        self.stars.run()
        self.spaceShip.score.setAllowPlusScorePlayer(self.enemy.allowPlusScorePlayer)
        self.spaceShip.run()
        self.enemy.run(self.spaceShip.firstWeapon.listOfBullets, self.objects.secondWeapon.listOfBullets)
        self.objects.run()
        self.dropedObjects.run()

    def shootWithFirstWeapon(self):
        if self.spaceShip.state == 'ShootWithFirstGun':
            self.spaceShip.firstWeapon.runToShoot(self.spaceShip.x)

    def shootWithSecondWeapon(self):
        if self.spaceShip.state == 'ShootWithSecondGun':
            self.objects.secondWeapon.shoot(self.spaceShip.x)
