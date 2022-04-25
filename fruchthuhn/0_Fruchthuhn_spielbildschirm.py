# random bietet verschiedene möglichkeiten um Zufällige Sachen zu erstellen (randint = Zufällige zahl,
# choise = zufälliges Element aus einer liste)
from random import randint, choice

# python game zero --> unterstützt uns bei der spiele programmierung
import pgzrun
# Actor sind z.B. Spielfiguren auf dem Spielbildschirm
from pgzero.actor import Actor

# lege die größe des Spielbildschirms fest
WIDTH = 800
#Breite

HEIGHT = 600
#hoehe

# standard methode wird ca. 60 * pro Minute aufgerufen
def draw():
    # leere den bildschirm
    screen.clear()

    # fülle den hintergrund mit einer farbe
    # screen.fill(farbe) --> erwartet eine farbe
    # mit der doppelten Klammern wird ein RGB wert erwartet
    # von 0-255 (Rot, Grün, Blau)
    screen.fill((128,0,0))

    # zeige ein hintergrundbild an
    # --> nehm das hashtag bei der nächsten Zeile raus
    # screen.blit("hintergrund", (0, 0))



# fuehrt die Anwendung aus -> pgzrun ist das python game zero, welches die spiele programmierung in
# python erleichtert und einiges an programmieraufwand/code abnimmt. (Z.B erstellen eines Speielmonitors, etc)
pgzrun.go()
