from pgzero.builtins import Actor
import math

SPEED = 6

def normalised(x, y):
    # Return a unit vector
    # Get length of vector (x,y) - math.hypot uses Pythagoras' theorem to get length of hypotenuse
    # of right-angle triangle with sides of length x and y
    # todo note on safety
    length = math.hypot(x, y)
    return (x / length, y / length)


class Bullet(Actor):
    def __init__(self, player, pos, heading):
        self.player = player
        self.heading = heading

        super().__init__(f"bullet{self.player}0", pos)

        self.done = False
        self.timer = 100

        self.speed = 6

        rad = math.radians(self.heading - 90)
        self.dx = math.cos(rad)
        self.dy = math.sin(rad)
        self.dx, self.dy = normalised(self.dx, self.dy)



    def update(self):
        for i in range(self.speed):
            # Move the ball based on dx and dy
            self.x += self.dx
            self.y += self.dy

        self.timer -= 1
        if self.timer == 0:
            self.done = True

