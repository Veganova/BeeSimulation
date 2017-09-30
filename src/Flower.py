import Draw
import math
from Position import Posn
from Bee import HoneyBee
from Hive import Hive


class Flower(Posn):
    color = (200, 100, 100)

    def __init__(self, x, y):
        super().__init__(x, y)
        self.radius = 30
        self.stamen = True # Boolean value indicates presence of pollen
        self.pistil = False

    def draw(self, canvas):
        Draw.draw_circle(canvas, self.x, self.y, self.radius, self.color)

    def bee_close(self, HoneyBee):
        distance_between = math.sqrt(pow((HoneyBee.x - self.x), 2) + pow((self.y - HoneyBee.y), 2))
        if distance_between <= self.radius + HoneyBee.radius:
            return True
        else:
            return False

    def transfer_pollen(self, HoneyBee):
        if self.bee_close(self, HoneyBee):
            if HoneyBee.pollen == 0 and self.stamen:
                HoneyBee.pollen = 1
                not self.stamen
                print("Pollen transferred")
            elif HoneyBee.pollen == 0 and not self.stamen:
                print("No Pollen transferred")
            elif HoneyBee.pollen == 1 and not self.pistil:
                HoneyBee.pollen = 0
                print("Pollen given to flower")
                not self.pistil
        else:
            pass

    def update(self, HoneyBee):
        self.transfer_pollen()

    def death(self):
        pass
