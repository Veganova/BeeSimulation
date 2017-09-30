from Movable import MovableObjects
import Draw
from Flower import Flower

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
        self.home = hive
        # honey is the amount fed to the bee at birth
        # this also signifies hunger (if it hits 0, the bee is dead)
        self.hunger = hunger
        self.pollen = 0
        self.nectar = 0 #MAX VAlUE of 2
        self.objects.append(self)

        # 0 - wants to get flower
        # 1 - return necter to hive
        self.status = 0

    def update(self):
        super().update()
        #self.honey -= 1

        if (self.status == 0):
            self.findFlower()
        elif (self.status == 1):
            self.returnToHive()

    def choose_flower(self):
        Flower.objects
        bestFlower = Flower.objects[0]
        if self.nectar > 2:
            pass#back to hive
        for i in range(Flower.object.size):
            if bestFlower.nectar < Flower.objects[i]:
                bestFlower = Flower.objects[i]

    def death(self):
        pass

    def draw(self, canvas):
        Draw.draw_circle(canvas, self.x, self.y, self.radius, self.color)