import Draw
import math
from Position import Posn
from Bee import HoneyBee


class Flower(Posn):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.radius = 2
        self.stamen = True # Boolean value indicates presence of pollen
        self.pistil = False

    def draw(self, canvas):
        Draw.draw_circle(canvas, self.x, self.y, self.radius, self.color)

    def bee_close(self, HoneyBee):
        distance_between = math.sqrt(pow((HoneyBee.x - self.x), 2) + pow((self.y - HoneyBee.x), 2))
        if distance_between <= self.radius + HoneyBee.radius:
            return True
        else:
            return False



    def death(self):
        pass

bee1 = HoneyBee(1, 1)
flower1 = Flower(4, 1)
print(flower1.bee_close(bee1))
