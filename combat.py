import math

import pygame, pgzrun
from pgzero.builtins import Actor, music, sounds
from pgzero.keyboard import keyboard
from constants import *


class Tank(Actor):
    def __init__(self, player, position, heading, move_func=None):
        x, y = position
        super().__init__("blank", (x, y))

        self.player = player
        self.score = 0
        self.heading = heading

        if move_func != None:
            self.move_func = move_func
        else:
            self.move_func = self.ai

        self.timer = 0

    def draw(self, screen):
        self.image = f"player{self.player}0"
        shipImg, newRect = self.rot_center(self._surf, self.heading)
        screen.blit(shipImg, newRect)

    def rot_center(self, image, angle):
        """rotate an image while keeping its center"""
        center = (self.topleft[0] + (self.width / 2), self.topleft[1] - (self.height / 2))
        old_rect = self._surf.get_rect(center=center)

        rot_image = pygame.transform.rotate(image, -angle)
        rot_rect = rot_image.get_rect(center=old_rect.center)
        return rot_image, rot_rect



    def update(self):
        self.timer -= 1

        # Our movement function tells us how much to move on the Y axis
        rotate, movement = self.move_func()
        self.heading += rotate
        self.heading = self.heading % 360

        rad = math.radians(self.heading - 90)
        dx = math.cos(rad) * movement
        dy = math.sin(rad) * movement

        # Apply movement to position, ensuring bat does not go through the side walls
        new_y = min(490, max(110, self.y + dy))
        new_x = min(760, max(40, self.x + dx))

        if self.x != 40 and self.x != 760:
           self.y = new_y

        if self.y != 110 and self.y != 490:
            self.x = new_x

    def ai(self):
        return (0, 0)


class Game:
    def __init__(self, controls=(None, None)):
        # Create a list of two tanks, giving each a player number and a function to use to receive
        # control inputs (or the value None if this is intended to be an AI player)
        self.tanks = [
            Tank(0, (50, 300), 90, controls[0]),
            Tank(1, (750, 300), 270, controls[1]),
        ]

    def update(self):
        # Update all active objects
        for obj in self.tanks:
            obj.update()

    def draw(self):
        # Draw background
        screen.blit("table", (0,0))

        # Display scores - outer loop goes through each player
        for p in (0,1):
            # Convert score into a string of 2 digits (e.g. "05") so we can later get the individual digits
            score = f"{self.tanks[p].score:02d}"
            # Inner loop goes through each digit
            for i in (0,1):
                colour = "0"
                image = "digit0" + str(score[i])
                screen.blit(image, (255 + (160 * p) + (i * 55), 46))

        # Draw bats, ball and impact effects - in that order. Square brackets are needed around the ball because
        # it's just an object, whereas the other two are lists - and you can't directly join an object onto a
        # list without first putting it in a list
        for obj in self.tanks:
            obj.draw(screen)


def p1_controls():
    rotate = 0
    move = 0
    if keyboard.w:
        move = PLAYER_SPEED
    elif keyboard.s:
        move = -PLAYER_SPEED

    if keyboard.a:
        rotate = -2
    elif keyboard.d:
        rotate = 2

    return (rotate, move)

def p2_controls():
    rotate = 0
    move = 0
    if keyboard.up:
        move = PLAYER_SPEED
    elif keyboard.down:
        move = -PLAYER_SPEED

    if keyboard.left:
        rotate = -2
    elif keyboard.right:
        rotate = 2
    return (rotate, move)


def update():
    game.update()

def draw():
    game.draw()

controls = [p1_controls, p2_controls]
game=Game(controls)

pgzrun.go()