from Movable import MovableObjects
import Draw

class HoneyBee(MovableObjects):
    color = (255, 255, 0)

    def __init__(self, x, y, hive):
        super().__init__(x, y, 6000, 0)
        self.radius = 10#mm
        self.age = 0
        self.home = hive
        # feed the bee at birth
        # this also signifies hunger (if it hits 0, the bee is dead)
        self.honey = hive.feed(self)

        self.pollen = 0

    def update(self):
        super().update()
        self.honey -= 1

    def death(self):
        pass

    def draw(self, canvas):
        Draw.draw_circle(canvas, self.x, self.y, self.radius, self.color)