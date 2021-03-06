from SpaceShip import SpaceShip
from Enemy import Enemy
from objects import Objects
from DropedObjects import DropedObjects
from stars import Stars
from buttonToStartGame import StartGame

class MainConstructor():

    def __init__ (self, mainMenuSound, soundMouse, soundSpace, soundGun, soundClick, takeSomething):
        self.spaceShip = SpaceShip(width/2, height/2+150, 150, 150, 5, soundGun, takeSomething)
        self.enemy = Enemy(random(0+75/2, width-75/2), -300, 75, 75, 3)
        self.spaceShip.setEnemy(self.enemy)
        self.objects = Objects(soundGun)
        self.spaceShip.setSecondWeapon(self.objects.secondWeapon)
        self.spaceShip.setSecondWeaponTimer(self.objects.secondWeaponTimer)
        self.dropedObjects = DropedObjects(random(0+25, width-25), -2400, 50, 50, 2, random(0+25, width-25))
        self.spaceShip.setDropedSecondWeapon(self.dropedObjects.dropedSecondWeapon)
        self.stars = Stars()
        self.gameState = False
        self.buttonToStartGame = StartGame(width/2, height/2, 100, 50)

        self.mainMenuSound = mainMenuSound
        self.mainMenuSound.loop()

        self.soundMouse = soundMouse

        self.soundSpace = soundSpace

        self.soundClick = soundClick

    def game(self, mouseState):
        if self.gameState == False:
            self.soundClick.rewind()
            self.soundSpace.rewind()
            self.buttonToStartGame.run()
            newGameState = self.buttonToStartGame.pressed(mouseState)
            if newGameState:
                self.mainMenuSound.pause()
                self.gameState = newGameState
            self.spaceShip.score.timer.workTimer(self.spaceShip.score.bestScore, self.buttonToStartGame.x, self.buttonToStartGame.y)
            self.enemy.spawn()

            aiming = self.buttonToStartGame.aiming()
            if aiming:
                self.soundMouse.play()
            else:
                self.soundMouse.rewind()
                self.soundMouse.pause()

        else:
            self.soundClick.play()
            self.soundSpace.play()
            self.spaceShip.score.timer.restartOptions()
            self.run()


    def run(self):
        self.stars.run()
        self.spaceShip.run() 
        self.enemy.run(self.spaceShip.firstWeapon.listOfBullets, self.objects.secondWeapon.listOfBullets)
        self.objects.run()
        self.dropedObjects.run()
        newGameState = self.spaceShip.setGameState(self.gameState)
        if newGameState == False:
            self.mainMenuSound.rewind()
            self.mainMenuSound.loop()

        self.gameState = newGameState

    def shootWithFirstWeapon(self):
        if self.gameState:
            if self.spaceShip.state == 'ShootWithFirstGun':
                self.spaceShip.firstWeapon.runToShoot(self.spaceShip.x)

    def shootWithSecondWeapon(self):
        if self.gameState:
            if self.spaceShip.state == 'ShootWithSecondGun':
                self.objects.secondWeapon.shoot(self.spaceShip.x)
