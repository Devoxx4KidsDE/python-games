from random import randint

import pgzrun
from pgzero.actor import Actor

fruechte = ['apple', 'orange', 'pineapple']
frucht = Actor(fruechte[randint(0, len(fruechte) - 1)])


score = 0
timer = 30
player_lives = 3

WIDTH = 800
HEIGHT = 600
TITLE = 'Fruchthuhn'


def update(dt):
    global timer, player_lives
    if timer >= 0 and player_lives > 0:
        timer -= dt


def draw():
    screen.clear()
    screen.blit("background", (0, 0))
    screen.draw.text(str(score), (400, 0), fontsize=50, color="black")
    frucht.draw()
    screen.draw.text("Verbleibende Zeit: %s" % round(timer), (0, 0), color="black")

    move_frucht()

    draw_lives()
    if player_lives == 0 or timer < 0:
        draw_game_over()


def move_frucht():
    frucht.x += randint(-20, 20)
    frucht.y += randint(-20, 20)

    if WIDTH - 20 <= frucht.x <= 0:
        frucht.x = 10
    if HEIGHT - 20 <= frucht.y <= 0:
        frucht.y = 10


def draw_lives():
    for life in range(player_lives):
        screen.blit('heart', (WIDTH-30-(life*16), 10))


def draw_game_over():
    global timer, score
    if timer > 0:
        screen.draw.textbox("Game Over!\n %s Punkte erreicht\n mit %s Sekunden Restzeit!" % (score, round(timer)), Rect(100, 100, 600, 400), background="black")
    else:
        screen.draw.textbox("Game Over!\n %s Punkte erreicht" % score, Rect(100, 100, 600, 400), background="black")


def place_fruit():
    frucht.x = randint(10, WIDTH)
    frucht.y = randint(10, HEIGHT)
    frucht.image = fruechte[randint(0, len(fruechte) - 1)]


def on_mouse_down(pos):
    global score, timer

    if timer > 0:
        if frucht.collidepoint(pos):
            print("Treffer!")
            place_fruit()
            score += 1
        else:
            print("Daneben!")


def on_key_down(key):
    if key == keys.R:
        init()


def init():
    global score, timer, player_lives
    score = 0
    place_fruit()
    timer = 30
    player_lives = 3


init()
pgzrun.go()