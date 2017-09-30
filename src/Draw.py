import pygame

scale = 1


def draw_circle(canvas, x, y, radius, color):
    sx = (int(x * scale))
    sy = (int(y * scale))
    sr = int(radius * scale)
    pygame.draw.circle(canvas, color, (sx, sy), sr, 0)