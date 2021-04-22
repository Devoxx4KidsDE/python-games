import pgzrun

# lege die größe des Spielbildschirms fest
WIDTH = 800
HEIGHT = 600

# standard methode wird ca. 60 * pro Minute aufgerufen
def draw():
    # leere den bildschirm
    screen.clear()

    # fülle den hintergrund mit einer farbe
    # screen.fill(color) --> erwartet eine farbe
    # mit der doppelten Klammern wird ein RGB wert erwartet
    # von 0-255 (Rot, Grün, Blau)
    screen.fill((128,0,0))

    # zeige ein hintergrundbild an
    # --> nehm das hashtag bei der nächsten Zeile raus
    # screen.blit("hintergrund", (0, 0))

pgzrun.go()
