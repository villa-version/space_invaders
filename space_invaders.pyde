from MainConstructor import MainConstructor

main_constructor = None

def setup():
    size(1000,800)
    imageMode(CENTER)
    rectMode(CENTER)
    textSize(24)
    global main_constructor
    main_constructor = MainConstructor()


def draw():
    background(70,174,183)
    main_constructor.run()

    if mousePressed:
        main_constructor.shootWithSecondWeapon()

def mousePressed():
    main_constructor.shootWithFirstWeapon()
