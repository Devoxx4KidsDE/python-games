from random import randint, choice

import pgzrun
from pgzero.actor import Actor

# array mit den frucht bildern
fruechte = ['apfel', 'orange', 'ananas']
# waehle ein bild zufaellig aus 'fruechte' aus
frucht = Actor(choice(fruechte))


punktestand = 0
WIDTH = 800
HEIGHT = 600

def draw():
    screen.clear()
    screen.blit("hintergrund", (0, 0))

    screen.draw.text(str(punktestand), (400, 0), fontsize=50, color="black")

    frucht.draw()


def platziere_frucht():
    frucht.x = randint(10, WIDTH)
    frucht.y = randint(10, HEIGHT)

    # aendere das bild der aktuellen frucht durch ein neues zufaelliges bild aus 'fruechte'
    frucht.image = choice(fruechte)


def on_mouse_down(pos):
    global punktestand
    if frucht.collidepoint(pos):
        print("Treffer!")
        platziere_frucht()
        punktestand += 1
    else:
        print("Daneben!")


def init():
    global punktestand
    punktestand = 0
    platziere_frucht()


init()
pgzrun.go()