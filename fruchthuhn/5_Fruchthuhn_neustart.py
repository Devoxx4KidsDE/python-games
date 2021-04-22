from random import randint, choice

import pgzrun
from pgzero.actor import Actor

fruechte = ['apfel', 'orange', 'ananas']
frucht = Actor(choice(fruechte))


punktestand = 0
timer = 30

WIDTH = 800
HEIGHT = 600


def update(dt):
    global timer
    if timer >= 0:
        timer -= dt


def draw():
    screen.clear()
    screen.blit("hintergrund", (0, 0))

    screen.draw.text(str(punktestand), (400, 0), fontsize=50, color="black")

    frucht.draw()

    screen.draw.text("Verbleibende Zeit: %s" % round(timer), (0, 0), color="black")

    if timer < 0:
        screen.draw.textbox("Game Over!\n %s Punkte erreicht" % punktestand, Rect(100, 100, 600, 400), background="black")


def platziere_frucht():
    frucht.x = randint(10, WIDTH)
    frucht.y = randint(10, HEIGHT)
    frucht.image = choice(fruechte)


def on_mouse_down(pos):
    global punktestand, timer

    if timer > 0:
        if frucht.collidepoint(pos):
            print("Treffer!")
            platziere_frucht()
            punktestand += 1
        else:
            print("Daneben!")


# standard methode wird aufgerufen bei jedem Tasten druck
def on_key_down(key):

    # pruefe ob R gedrückt wurde um jederzeit das spiel neu zu starten
    if key == keys.R:
        init()


def init():
    global punktestand, timer
    punktestand = 0
    platziere_frucht()
    timer = 30


init()
pgzrun.go()