import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, 1, 1),
    (-1, -1, 1)
)

edges = (
    (0, 1),
    (0, 3),
    (0, 7),
    (1, 2),
    (1, 6),
    (2, 3),
    (2, 5),
    (3, 4),
    (4, 5),
    (4, 7),
    (5, 6),
    (6, 7)
)
