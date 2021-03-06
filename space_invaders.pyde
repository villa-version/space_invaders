from MainConstructor import MainConstructor

main_constructor = None

add_library('minim')

def setup():
    size(800,600)
    imageMode(CENTER)
    rectMode(CENTER)
    ellipseMode(CENTER)
    textSize(24)

    minim_music = Minim(this)
    mainMenuSound = minim_music.loadFile('sound/soundForSpaceInvMainMenu.wav')
    soundMouse = minim_music.loadFile('sound/spaceInvClick.wav')
    soundSpace = minim_music.loadFile('sound/soundForSpaceInvSpace.wav')
    soundGun = minim_music.loadFile('sound/soundForSpaceInvGun.wav')
    soundClick = minim_music.loadFile('sound/soundMouse.mp3')
    takeSomething = minim_music.loadFile('sound/NumberTakeSome/number1/takeSomething_1.wav')
    global main_constructor
    main_constructor = MainConstructor(mainMenuSound, soundMouse, soundSpace, soundGun, soundClick, takeSomething)


def draw():
    background(70,174,183)
    main_constructor.game(mousePressed)

    if mousePressed:
        main_constructor.shootWithSecondWeapon()


def mousePressed():
    global main_constructor
    main_constructor.shootWithFirstWeapon()
