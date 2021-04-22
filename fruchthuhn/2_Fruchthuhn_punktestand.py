from random import randint

import pgzrun
from pgzero.actor import Actor

frucht = Actor("apfel")

# erstelle eine punktestand variable
punktestand = 0

WIDTH = 800
HEIGHT = 600

def draw():
    screen.clear()
    screen.blit("hintergrund", (0, 0))

    # zeige den Punktestand oben links an
    screen.draw.text(str(punktestand), (400, 0), fontsize=50, color="black")

    frucht.draw()


def platziere_frucht():
    frucht.x = randint(10, WIDTH)
    frucht.y = randint(10, HEIGHT)


def on_mouse_down(pos):
    global punktestand
    if frucht.collidepoint(pos):
        print("Treffer!")
        platziere_frucht()

        # update punktestand
        punktestand += 1
    else:
        print("Daneben!")


# setze alle start werte auf den entsprechenden Anfangswert
def init():
    global punktestand
    punktestand = 0
    platziere_frucht()


init()
pgzrun.go()