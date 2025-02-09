from pgzero.keyboard import keyboard
from constants import TANK_SPEED


def p1_controls():
    rotate = 0
    move = 0
    fire = False

    if keyboard.w:
        move = TANK_SPEED
    elif keyboard.s:
        move = -TANK_SPEED

    if keyboard.a:
        rotate = -2
    elif keyboard.d:
        rotate = 2

    if keyboard.space:
        fire = True

    return (rotate, move, fire)

def p2_controls():
    rotate = 0
    move = 0
    fire = False

    if keyboard.up:
        move = TANK_SPEED
    elif keyboard.down:
        move = -TANK_SPEED

    if keyboard.left:
        rotate = -2
    elif keyboard.right:
        rotate = 2

    if keyboard.p:
        fire = True

    return (rotate, move, fire)