from SpaceShip import SpaceShip
from Enemy import Enemy
from objects import Objects
from DropedObjects import DropedObjects
from stars import Stars
from buttonToStartGame import StartGame

class MainConstructor():

    def __init__ (self):
        self.spaceShip = SpaceShip(width/2, height/2+150, 150, 150, 5)
        self.enemy = Enemy(random(0+75/2, width-75/2), -300, 75, 75, 3)
        self.spaceShip.setEnemy(self.enemy)
        self.objects = Objects()
        self.spaceShip.setSecondWeapon(self.objects.secondWeapon)
        self.spaceShip.setSecondWeaponTimer(self.objects.secondWeaponTimer)
        self.dropedObjects = DropedObjects(random(0+25, width-25), -2400, 50, 50, 2, random(0+25, width-25))
        self.spaceShip.setDropedSecondWeapon(self.dropedObjects.dropedSecondWeapon)
        self.stars = Stars()
        self.gameState = False
        self.buttonToStartGame = StartGame(width/2, height/2, 100, 50)

    def game(self, mouseState):
        if not self.gameState:
            self.buttonToStartGame.run()
            self.gameState = self.buttonToStartGame.pressed(mouseState)
            self.spaceShip.score.timer.workTimer(self.spaceShip.score.bestScore, self.buttonToStartGame.x, self.buttonToStartGame.y)
            self.enemy.spawn()
        else:
            self.spaceShip.score.timer.restartOptions()
            self.run()

    def run(self):
        self.stars.run()
        self.spaceShip.run()
        self.enemy.run(self.spaceShip.firstWeapon.listOfBullets, self.objects.secondWeapon.listOfBullets)
        self.objects.run()
        self.dropedObjects.run()
        self.gameState = self.spaceShip.setGameState(self.gameState)

    def shootWithFirstWeapon(self):
        if self.spaceShip.state == 'ShootWithFirstGun':
            self.spaceShip.firstWeapon.runToShoot(self.spaceShip.x)

    def shootWithSecondWeapon(self):
        if self.spaceShip.state == 'ShootWithSecondGun':
            self.objects.secondWeapon.shoot(self.spaceShip.x)
