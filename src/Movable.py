class MovableObjects(BaseException):

    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy


    def update(self):
        self.x += self.dx / 50
        self.y += self.dy / 50