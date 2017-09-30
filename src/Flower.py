import random

import Draw
import math
from Position import Posn



class Flower(Posn):
    objects = []
    color = (200, 100, 100)

    def __init__(self, x, y):
        super().__init__(x, y)
        self.radius = 30
        self.stamen = True # Boolean value indicates presence of pollen
        self.pistil = False
        self.nectar = 50
        self.objects.append(self)

    def draw(self, canvas):
        Draw.draw_circle(canvas, self.x, self.y, self.radius, self.color)

    def bee_close(self, bee):
        distance_between = math.sqrt(pow((bee.x - self.x), 2) + pow((self.y - bee.y), 2))
        if distance_between <= self.radius + bee.radius:
            return True
        else:
            return False

    def interact(self, bee):
        if self.bee_close(bee):
            bee.dx = 0
            bee.dy = 0


            # If has enough nectar, bee leaves
            if self.nectar <= 0 or bee.nectar >= bee.MAX_NECTAR:
                bee.changeStatus()
                pass

            bee.nectar = self.extractNectar()

            if bee.pollen == 0:
                bee.pollen = self.extractPollen()
            elif bee.pollen > 0:
                self.pollinate(bee)
        else:
            pass

    def update(self):
       # self.transfer_pollen()
       # todo: grow nectar and pollen
        pass

    def death(self):
        pass

    def extractPollen(self):
        # 50 percent change of getting pollen
        if random.randint(0, 100) < 50:
            return 1
        return 0

    def extractNectar(self):
        self.nectar -= 1
        return 1

    def pollinate(self, bee):
        if random.randint(0, 100) < 50:
            bee.pollen -= 1
            print("I HAVE BABIES!!")
            # todo seeds