import pygame, sys
from pygame.locals import *
from Bee import HoneyBee
from Hive import Hive
from Position import Posn

# each tick is a second
# a pixel is a milimeter


def main():
    pygame.init()

    canvas = pygame.display.set_mode((1000, 800), 0, 32)

    WHITE = (255, 255, 255)
    blue = (0, 0, 255)

    canvas.fill(WHITE)

    pygame.draw.rect(canvas, blue, (200, 150, 100, 50))
    #pygame.draw.circle(DISPLAY, blue, (0, 0), 20, 0)

    Hive(300, 300)
    #HoneyBee(100, 100)

    # Simulation loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        canvas.fill(WHITE)

        for i in Posn.updatables:
            i.update()
            i.draw(canvas)


        pygame.display.update()
        pygame.time.delay(100)

main()

