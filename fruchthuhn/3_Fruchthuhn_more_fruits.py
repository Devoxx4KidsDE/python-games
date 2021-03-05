from random import randint, choice

import pgzrun
from pgzero.actor import Actor

# array mit den frucht bildern
fruechte = ['apple', 'orange', 'pineapple']
# waehle ein bild zufaellig aus 'fruechte' aus
frucht = Actor(choice(fruechte))


score = 0
WIDTH = 800
HEIGHT = 600

def draw():
    screen.clear()
    screen.blit("background", (0, 0))

    screen.draw.text(str(score), (400, 0), fontsize=50, color="black")

    frucht.draw()


def place_fruit():
    frucht.x = randint(10, WIDTH)
    frucht.y = randint(10, HEIGHT)

    # aendere das bild der aktuellen frucht durch ein neues zufaelliges bild aus 'fruechte'
    frucht.image = choice(fruechte)


def on_mouse_down(pos):
    if frucht.collidepoint(pos):
        print("Treffer!")
        place_fruit()
        score += 1
    else:
        print("Daneben!")


def init():
    global score
    score = 0
    place_fruit()


init()
pgzrun.go()