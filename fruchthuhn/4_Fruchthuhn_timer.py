from random import randint, choice

import pgzrun
from pgzero.actor import Actor

fruechte = ['apfel', 'orange', 'ananas']
frucht = Actor(choice(fruechte))


punktestand = 0
# neue variable timer mit 30
timer = 30

WIDTH = 800
HEIGHT = 600


# standard methode updated den screen etc.
def update(dt):
    global timer
    if timer >= 0:
        timer -= dt


def draw():
    screen.clear()
    screen.blit("hintergrund", (0, 0))

    screen.draw.text(str(punktestand), (400, 0), fontsize=50, color="black")

    frucht.draw()

    # zeigt die verbleibende Zeit in der mitte des bildschirms an
    screen.draw.text("Verbleibende Zeit: %s" % round(timer), (0, 0), color="black")

    # zeigt ein Game Over wenn der Timer abgelaufen ist
    if timer < 0:
        screen.draw.textbox("Game Over!\n %s Punkte erreicht" % punktestand, Rect(100, 100, 600, 400), background="black")


def platziere_frucht():
    frucht.x = randint(10, WIDTH)
    frucht.y = randint(10, HEIGHT)
    frucht.image = choice(fruechte)


def on_mouse_down(pos):
    global punktestand, timer

    # reagiere nur auf maus klicks wenn der timer noch nicht abgelaufen ist
    if timer > 0:
        if frucht.collidepoint(pos):
            print("Treffer!")
            platziere_frucht()
            punktestand += 1
        else:
            print("Daneben!")


def init():
    global punktestand, timer
    punktestand = 0
    platziere_frucht()

    # timer reseten
    timer = 30


init()
pgzrun.go()