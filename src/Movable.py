from Position import Posn

class MovableObjects(Posn):

    def __init__(self, x, y, dx, dy):
        super().__init__(x, y)
        self.dx = dx
        self.dy = dy

    def update(self):
        self.x += self.dx
        self.y += self.dy