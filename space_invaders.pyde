from MainConstructor import MainConstructor

main_constructor = None

def setup():
    size(800,600)
    imageMode(CENTER)
    rectMode(CENTER)
    ellipseMode(CENTER)
    textSize(24)
    global main_constructor
    main_constructor = MainConstructor()


def draw():
    background(70,174,183)
    main_constructor.game(mousePressed)

    if mousePressed:
        main_constructor.shootWithSecondWeapon()


def mousePressed():
    global main_constructor
    main_constructor.shootWithFirstWeapon()
