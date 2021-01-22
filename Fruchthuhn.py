from random import randint

import pgzrun
from pgzero.actor import Actor

fruits = ['apple', 'orange', 'pineapple']
fruit = Actor(fruits[randint(0, len(fruits) - 1)])
TITLE = "Fruchthuhn"

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
    screen.blit("background",(0,0))
    screen.draw.text(str(score), (400, 0), fontsize=50, color="black")
    fruit.draw()

    screen.draw.text(f"Verbleibende Zeit: " + str(round(timer)), (0, 0), color="black")
    if timer < 0:
        screen.draw.textbox(f"Game Over!\n {score} Punkte erreicht", Rect(100, 100, 600, 400), background="black")

def place_fruit():
    fruit.x = randint(10, 800)
    fruit.y = randint(10, 600)
    fruit.image = fruits[randint(0, len(fruits) - 1)]


def on_mouse_down(pos):
    global score, timer
    if timer > 0:
        if fruit.collidepoint(pos):
            print("Treffer!")
            place_fruit()
            score += 1
        else:
            print("Daneben!")
            score -= 1


place_fruit()
pgzrun.go()
