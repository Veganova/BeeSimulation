from Movable import MovableObjects
import Draw

class HoneyBee(MovableObjects):
    color = (255, 255, 0)

    # 6000 milimeters per second
    SPEED = 6000

    # will only be called from hive
    def __init__(self, x, y, hive, hunger):

        super().__init__(x, y, self.SPEED, 0)
        self.radius = 10#mm
        self.age = 0
        self.home = hive
        # honey is the amount fed to the bee at birth
        # this also signifies hunger (if it hits 0, the bee is dead)
        self.hunger = hunger
        self.pollen = 0

    def update(self):
        super().update()
        #self.honey -= 1

    def death(self):
        pass

    def draw(self, canvas):
        Draw.draw_circle(canvas, self.x, self.y, self.radius, self.color)