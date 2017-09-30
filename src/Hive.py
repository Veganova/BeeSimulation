import Draw
from Bee import HoneyBee
from Position import Posn


class Hive(Posn):

    MAX_HONEY = 100
    POPULATION_MAX = 10
    BEE_COUNT = 0

    color = (180, 180, 0)

    def __init__(self, x, y):
        super().__init__(x, y)
        self.honey = 0
        self.radius = 50
        self.cooldown = 10

    def update(self):
        # every second
        HoneyBee(self.x, self.y, self)

    def draw(self, canvas):
        Draw.draw_circle(canvas, self.x, self.y, self.radius, self.color)




