from random import randint, choice

import pgzrun
from pgzero.actor import Actor

fruechte = ['apfel', 'orange', 'ananas']
frucht = Actor(choice(fruechte))


punktestand = 0
timer = 30
leben = 3

WIDTH = 800
HEIGHT = 600
TITLE = 'Fruchthuhn'


def update(dt):
    global timer, leben
    if timer >= 0 and leben > 0:
        timer -= dt


def draw():
    screen.clear()
    screen.blit("hintergrund", (0, 0))
    screen.draw.text(str(punktestand), (400, 0), fontsize=50, color="black")
    frucht.draw()
    screen.draw.text("Verbleibende Zeit: %s" % round(timer), (0, 0), color="black")

    move_frucht()

    draw_leben()
    if leben == 0 or timer < 0:
        draw_game_over()


def move_frucht():
    frucht.x += randint(-20, 20)
    frucht.y += randint(-20, 20)

    if frucht.x <= 10:
        frucht.x = 30

    if WIDTH - 20 <= frucht.x:
        frucht.x = WIDTH - 30

    if frucht.x <= 10:
        frucht.y = 30

    if HEIGHT - 20 <= frucht.y:
        frucht.y = HEIGHT - 20


def draw_leben():
    for verbleibendes_leben in range(leben):
        screen.blit('herz', (WIDTH-30-(verbleibendes_leben*16), 10))


def draw_game_over():
    global timer, punktestand
    if timer > 0:
        screen.draw.textbox("Game Over!\n %s Punkte erreicht\n mit %s Sekunden Restzeit!" % (punktestand, round(timer)), Rect(100, 100, 600, 400), background="black")
    else:
        screen.draw.textbox("Game Over!\n %s Punkte erreicht" % punktestand, Rect(100, 100, 600, 400), background="black")


def platziere_frucht():
    frucht.x = randint(10, WIDTH)
    frucht.y = randint(10, HEIGHT)
    frucht.image = choice(fruechte)


def on_mouse_down(pos):
    global punktestand, timer, leben
    if timer > 0:
        if frucht.collidepoint(pos):
            print("Treffer!")
            platziere_frucht()
            punktestand += 1
        else:
            leben -= 1
            print("Daneben!")


def on_key_down(key):
    if key == keys.R:
        init()


def init():
    global punktestand, timer, leben
    punktestand = 0
    platziere_frucht()
    timer = 30
    leben = 3


init()
pgzrun.go()