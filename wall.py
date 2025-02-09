from pgzero.builtins import Actor

class Wall(Actor):
    def __init__(self, position, image):
        x, y = position
        super().__init__(image, (x, y))
