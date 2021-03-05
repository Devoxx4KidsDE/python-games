from random import randint, choice

import pgzrun
from pgzero.actor import Actor

fruechte = ['apple', 'orange', 'pineapple']
frucht = Actor(choice(fruechte))


score = 0
timer = 30

WIDTH = 800
HEIGHT = 600


def update(dt):
    global timer
    if timer >= 0:
        timer -= dt


def draw():
    screen.clear()
    screen.blit("background", (0, 0))

    screen.draw.text(str(score), (400, 0), fontsize=50, color="black")

    frucht.draw()

    screen.draw.text("Verbleibende Zeit: %s" % round(timer), (0, 0), color="black")

    if timer < 0:
        screen.draw.textbox("Game Over!\n %s Punkte erreicht" % score, Rect(100, 100, 600, 400), background="black")


def place_fruit():
    frucht.x = randint(10, WIDTH)
    frucht.y = randint(10, HEIGHT)
    frucht.image = fruechte[choice(fruechte)]


def on_mouse_down(pos):
    global score, timer

    if timer > 0:
        if frucht.collidepoint(pos):
            print("Treffer!")
            place_fruit()
            score += 1
        else:
            print("Daneben!")


# standard methode wird aufgerufen bei jedem Tasten druck
def on_key_down(key):

    # pruefe ob R gedrückt wurde um jederzeit das spiel neu zu starten
    if key == keys.R:
        init()


def init():
    global score, timer
    score = 0
    place_fruit()
    timer = 30


init()
pgzrun.go()