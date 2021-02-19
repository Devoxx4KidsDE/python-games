from random import randint

import pgzrun
from pgzero.actor import Actor
from pygame import Rect

fruits = ['apple', 'orange', 'pineapple']
fruit = Actor(fruits[randint(0, len(fruits) - 1)])
TITLE = 'Fruchthuhn'
player_lives = 3

score = 0
timer = 30
WIDTH = 800
HEIGHT = 600


def update(dt):
    global timer, player_lives
    if timer >= 0 and player_lives > 0:
        timer -= dt


def draw():
    screen.clear()
    screen.blit("background", (0, 0))
    screen.draw.text(str(score), (400, 0), fontsize=50, color="black")
    fruit.draw()

    fruit.x += randint(-20, 20)
    fruit.y += randint(-20, 20)

    if fruit.x >= WIDTH - 20:
        fruit.x = 10

    if fruit.y >= HEIGHT - 20:
        fruit.y = 10

    screen.draw.text("Verbleibende Zeit: %s" % round(timer), (0, 0), color="black")

    draw_lives()

    if player_lives == 0 or timer < 0:
        draw_game_over()


def draw_centre_text(t):
    screen.draw.text(t, center=(400, 300), owidth=0.5, ocolor=(255, 255, 255), color=(255, 64, 0), fontsize=60)


def draw_lives():
    for life in range(player_lives):
        screen.blit('heart', (WIDTH-30-(life*16), 10))


def place_fruit():
    fruit.x = randint(10, 800)
    fruit.y = randint(10, 600)
    fruit.image = fruits[randint(0, len(fruits) - 1)]


def draw_game_over():
    global timer, score
    if timer > 0:
        screen.draw.textbox("Game Over!\n %s Punkte erreicht\n mit %s Sekunden Restzeit!" % (score, round(timer)), Rect(100, 100, 600, 400), background="black")
    else:
        screen.draw.textbox("Game Over!\n %s Punkte erreicht" % score, Rect(100, 100, 600, 400), background="black")


def on_mouse_down(pos):
    global score, timer, player_lives
    if timer > 0:
        if fruit.collidepoint(pos):
            print("Treffer!")
            place_fruit()
            score += 1
        else:
            print("Daneben!")
            player_lives -= 1


def on_key_down(key):
    if key == 'R':
        init()


def init():
    global score, player_lives, timer
    score = 0
    player_lives = 3
    timer = 30


place_fruit()
init()
pgzrun.go()
