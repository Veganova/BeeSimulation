from Movable import MovableObjects
import Draw

class HoneyBee(MovableObjects):
    color = (255, 255, 0)

    def __init__(self, x, y):
        super().__init__(x, y, 6, 0)
        self.radius = 10#mm

    def update(self):
        super().update()

    def draw(self, canvas):
        Draw.draw_circle(canvas, self.x, self.y, self.radius, self.color)