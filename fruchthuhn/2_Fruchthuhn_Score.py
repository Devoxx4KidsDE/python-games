from random import randint

import pgzrun
from pgzero.actor import Actor

frucht = Actor("apple")

# add score variable
score = 0

WIDTH = 800
HEIGHT = 600

def draw():
    screen.clear()
    screen.blit("background", (0, 0))

    # zeige den Score oben links an
    screen.draw.text(str(score), (400, 0), fontsize=50, color="black")

    frucht.draw()


def place_fruit():
    frucht.x = randint(10, WIDTH)
    frucht.y = randint(10, HEIGHT)


def on_mouse_down(pos):
    global score
    if frucht.collidepoint(pos):
        print("Treffer!")
        place_fruit()

        # update score
        score += 1
    else:
        print("Daneben!")


# setze alle start werte auf den entsprechenden Anfangswert
def init():
    global score
    score = 0
    place_fruit()


init()
pgzrun.go()