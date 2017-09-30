import Draw
from Bee import HoneyBee
from Position import Posn


class Hive(Posn):
    objects =[]

    MAX_HONEY = 100
    POPULATION_MAX = 10
    BEE_COUNT = 0

    BIRTH_COOLDOWN = 1000
    color = (180, 180, 0)

    def __init__(self, x, y):
        super().__init__(x, y)
        self.honey = 100
        self.radius = 50
        self.cooldown = self.BIRTH_COOLDOWN

        self.objects.append(self)

    def update(self):
        # every second
        if (self.cooldown == 0):
            self.birthABee()
            self.cooldown = self.BIRTH_COOLDOWN
        else:
            self.cooldown -= 1


    def feed(self, bee):
        bee.honey += self.extractHoney()

    def birthABee(self):
        if (self.honey > 0):
            HoneyBee(self.x, self.y, self, self.extractHoney())
        else:
            print("insufficient honey")


    def extractHoney(self) -> int:
        self.honey -= 1;
        return 1

    def draw(self, canvas):
        Draw.draw_circle(canvas, self.x, self.y, self.radius, self.color)

    def interact(self, bee):
        self.honey += bee.nectar
        bee.nectar = 0
        bee.changeStatus()



