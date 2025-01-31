from constants import *
from tank import Tank

class Game:
    def __init__(self, controls=(None, None)):
        HALF_HEIGHT = HEIGHT // 2   # Vertical Middle of Screen
        TANK_START_FROM_EDGE = 50   # Horizontal Distance of tank from side, at start

        # Create a list of two tanks, giving each a player number and a function to use to receive
        # control inputs (or the value None if this is intended to be an AI player)
        self.tanks = [
            Tank(player=0, game=self, position=(TANK_START_FROM_EDGE, HALF_HEIGHT), heading=90, move_func=controls[0]),
            Tank(player=1, game=self, position=(WIDTH - TANK_START_FROM_EDGE, HALF_HEIGHT - 100), heading=270, move_func=controls[1]),
        ]

        self.bullets = []

    def update(self):
        # Update all active objects
        all_objects = self.tanks + self.bullets
        for obj in all_objects:
            if obj:
                obj.update()

        # Recreate the bullets list, which will contain all existing bullets except those which have gone off the screen or have hit something
        self.bullets = [b for b in self.bullets if b.y > 0 and not b.done]

    def draw(self, screen):
        # Draw background
        screen.blit("table", (0,0))

        # Display scores - outer loop goes through each player
        for p in (0,1):
            # Convert score into a string of 2 digits (e.g. "05") so we can later get the individual digits
            score = f"{self.tanks[p].score:02d}"
            # Inner loop goes through each digit
            for i in (0,1):
                image = "digit0" + str(score[i])
                screen.blit(image, (255 + (160 * p) + (i * 55), 46))

        # Display the tanks
        for obj in self.tanks:
            obj.draw(screen)

        for obj in self.bullets:
            obj.draw()