from random import randint

import pgzrun
from pgzero.actor import Actor

apple = Actor("apple")


def draw():
    screen.clear()
    apple.draw()


def place_apple():
    apple.x = randint(10, 800)
    apple.y = randint(10, 600)


def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print("Treffer!")
        place_apple()
    else:
        print("Daneben!")


place_apple()
pgzrun.go()
