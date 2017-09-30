import Draw
from Position import Posn

from Bee import HoneyBee

class Flower(Posn):

    def __init__(self, x, y):
        self.x = x;
        self.y = y;
        self.stamen = True # Boolean value indicates presence of pollen
        self.pistil = False

    def draw(self, canvas):
        Draw.draw_circle(canvas, self.x, self.y, self.radius, self.color)

    def bee_close(self, HoneyBee):
        pass

    def death(self):
        pass



