from random import randint

import pgzrun
from pgzero.actor import Actor

# neue Figur mit dem Bild "apple"
frucht = Actor("apple")

# lege die größe des Spielbildschirms fest
WIDTH = 800
HEIGHT = 600

# standard methode wird ca. 60 * pro Minute aufgerufen
def draw():
    # leere den bildschirm
    screen.clear()
    # zeichne die frucht
    frucht.draw()


# setzt legt die Position der Frucht fest
def place_fruit():
    frucht.x = randint(10, WIDTH)
    frucht.y = randint(10, HEIGHT)

# standard funktion die immer dann auf gerufen wird,
# wenn während des spiel läuft ein Maus klick erfolgt
def on_mouse_down(pos):

    # prüfen ob die maus klick position gleich der Frucht position ist
    if frucht.collidepoint(pos):
        print("Treffer!")
        # positioniere die frucht neu
        place_fruit()
    else:
        # gebe auf der console aus, dass daneben geklickt wurde
        print("Daneben!")


# ist eine initiale function die dafür verwendet wird
# alle Werte auf den Spielanfangswerte zurück
def init():
    place_fruit()

init()
# starte das spiel
pgzrun.go()
