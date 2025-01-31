import math
from constants import *
from bullet import Bullet
import pygame
from pgzero.builtins import Actor

class Tank(Actor):
    def __init__(self, game, player, position, heading, move_func=None):

        x, y = position
        super().__init__("blank", (x, y))

        self.game = game
        self.player = player
        self.score = 0
        self.heading = heading
        self.reload_time = 0

        if move_func != None:
            self.move_func = move_func
        else:
            self.move_func = self.ai

        self.timer = 0


    def draw(self, screen):
        self.image = f"player{self.player}0"
        rotated_image, rotated_rect = self.rotate_image_around_center(self._surf, self.heading)
        screen.blit(rotated_image, rotated_rect)

    def rotate_image_around_center(self, image, angle):
        """rotate an image while keeping its center"""
        old_rect = self._surf.get_rect(center=(self.x, self.y))
        rotated_image = pygame.transform.rotate(image, -angle)
        rotated_rect = rotated_image.get_rect(center=old_rect.center)
        return rotated_image, rotated_rect

    def update(self):
        self.timer -= 1
        if self.reload_time > 0:
            self.reload_time -= 1

        # Our movement function tells us how much to move on the Y axis
        rotate, movement, fire = self.move_func()
        self.heading += rotate
        self.heading = self.heading % 360

        rad = math.radians(self.heading - 90)
        dx = math.cos(rad) * movement
        dy = math.sin(rad) * movement

        # Apply movement to position, ensuring bat does not go through the side walls
        TOP_EDGE = TOP_BORDER
        BOTTOM_EDGE = HEIGHT - BOTTOM_BORDER
        LEFT_EDGE = LEFT_BORDER
        RIGHT_EDGE = WIDTH - RIGHT_BORDER

        new_y = min(BOTTOM_EDGE, max(TOP_EDGE, self.y + dy))
        new_x = min(RIGHT_EDGE, max(LEFT_EDGE, self.x + dx))

        if self.x != LEFT_EDGE and self.x != RIGHT_EDGE:
           self.y = new_y

        if self.y != TOP_EDGE and self.y != BOTTOM_EDGE:
            self.x = new_x

        BULLET_LIMIT = 10
        if fire:
            if self.reload_time == 0:
                my_bullets = [b for b in self.game.bullets if b.player == self.player]
                if len(my_bullets) < BULLET_LIMIT:
                    self.game.bullets.append(Bullet(self.game, self.player,(self.x, self.y), self.heading))
                    self.reload_time = 10

    def ai(self):
        return (0, 0, False)
