class Posn(BaseException):

    updatables = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.updatables.append(self)
