from Position import Posn

class MovableObjects(Posn):

    def __init__(self, x, y, dx, dy):
        super().__init__(x, y)
        self.dx = dx
        self.dy = dy


    def update(self):
        self.x += self.dx / 5000
        self.y += self.dy / 5000
