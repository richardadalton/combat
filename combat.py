import pgzrun, pgzero

from game import Game
from controls import p1_controls, p2_controls
screen: pgzero.screen.Screen

def update():
    game.update()

def draw():
    game.draw(screen)

controls = [p1_controls, p2_controls]
game=Game(controls)
pgzrun.go()
