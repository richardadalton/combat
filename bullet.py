from pgzero.builtins import Actor, sounds
import math

SPEED = 6

class Bullet(Actor):
    def __init__(self, tank):
        self.tank = tank

        pos = (tank.x, tank.y)
        self.heading = tank.heading

        rad = math.radians(self.heading - 90)
        self.dx = math.cos(rad)
        self.dy = math.sin(rad)
        self.speed = 6

        super().__init__(f"bullet{self.tank.player}0", pos)

        self.done = False
        self.timer = 200
        self.bounce_count = 0


    def update(self):
        for i in range(self.speed):
            self.x += self.dx
            self.y += self.dy

            if self.y < 30 or self.y > 450:
                self.dy = -self.dy
                getattr(sounds, f'bounce{self.bounce_count}').play()
                sounds.bounce_synth0.play()
                self.bounce_count = (self.bounce_count + 1) % 5

            if self.x < 20 or self.x > 780:
                self.dx = -self.dx
                getattr(sounds, f'bounce{self.bounce_count}').play()
                sounds.bounce_synth0.play()
                self.bounce_count = (self.bounce_count + 1) % 5


        for obj in self.tank.game.tanks:
            if obj and obj.player != self.tank.player and obj.collidepoint(self.pos):
                self.done = True
                self.tank.score += 1
                obj.kill(self)

        self.timer -= 1
        if self.timer == 0:
            self.done = True

