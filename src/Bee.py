import math

from Movable import MovableObjects
import Draw


#Bees Algorithm
class HoneyBee(MovableObjects):
    objects = []

    color = (255, 255, 0)

    # 6000 milimeters per second
    SPEED = 6000



    # will only be called from hive
    def __init__(self, x, y, hive, hunger):

        super().__init__(x, y, self.SPEED, 0)
        self.radius = 10#mm
        self.age = 0
        self.hive = hive
        # honey is the amount fed to the bee at birth
        # this also signifies hunger (if it hits 0, the bee is dead)
        self.hunger = hunger
        self.pollen = 0

        self.objects.append(self)

        # 0 - wants to get flower
        # 1 - return necter to hive
        self.status = -1

        self.changeStatus()

    def update(self):
        super().update()
        #self.honey -= 1



    def death(self):
        pass

    def draw(self, canvas):
        Draw.draw_circle(canvas, self.x, self.y, self.radius, self.color)

    def returnToHive(self):
        self.goto(self.hive)

    def goto(self, posn):
        vec = (posn.x - self.x, posn.y - self.y)
        vecm = math.sqrt(vec[0] * vec[0] + vec[1] * vec[1])
        self.dx = vec[0] * self.SPEED / vecm
        self.dy = vec[1] * self.SPEED / vecm

    def changeStatus(self):
        self.status += 1
        self.status = self.status % 2

        if self.status == 0:
            self.findFlower()
        elif self.status == 1:
            self.returnToHive()