from random import randint, choice

import pgzrun
from pgzero.actor import Actor

fruechte = ['apple', 'orange', 'pineapple']
frucht = Actor(choice(fruechte))


score = 0
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
    screen.blit("background", (0, 0))

    screen.draw.text(str(score), (400, 0), fontsize=50, color="black")

    frucht.draw()

    # zeigt die verbleibende Zeit in der mitte des bildschirms an
    screen.draw.text("Verbleibende Zeit: %s" % round(timer), (0, 0), color="black")

    # zeigt ein Game Over wenn der Timer abgelaufen ist
    if timer < 0:
        screen.draw.textbox("Game Over!\n %s Punkte erreicht" % score, Rect(100, 100, 600, 400), background="black")


def place_fruit():
    frucht.x = randint(10, WIDTH)
    frucht.y = randint(10, HEIGHT)
    frucht.image = choice(fruechte)


def on_mouse_down(pos):
    global score, timer

    # reagiere nur auf maus klicks wenn der timer noch nicht abgelaufen ist
    if timer > 0:
        if frucht.collidepoint(pos):
            print("Treffer!")
            place_fruit()
            score += 1
        else:
            print("Daneben!")


def init():
    global score, timer
    score = 0
    place_fruit()

    # timer reseten
    timer = 30


init()
pgzrun.go()