from constants import *
from tank import Tank

class Game:
    def __init__(self, controls=(None, None)):
        HALF_HEIGHT = HEIGHT // 2   # Vertical Middle of Screen
        TANK_START_FROM_EDGE = 50   # Horizontal Distance of tank from side, at start

        # Create a list of two tanks, giving each a player number and a function to use to receive
        # control inputs (or the value None if this is intended to be an AI player)
        self.tanks = [
            Tank(0, (TANK_START_FROM_EDGE, HALF_HEIGHT), 90, controls[0]),
            Tank(1, (WIDTH - TANK_START_FROM_EDGE, HALF_HEIGHT), 270, controls[1]),
        ]

    def update(self):
        # Update all active objects
        for obj in self.tanks:
            obj.update()

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