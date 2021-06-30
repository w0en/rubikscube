import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (-1, 1, 1),
    (1, 1, 1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, -1),
    (1, -1, 1),
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

def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:








            glVertex3fv(vertices[vertex])

    glEnd()


def main():
    pygame.init()
    DISPLAY = (800, 600)
    pygame.display.set_mode(DISPLAY, DOUBLEBUF|OPENGL)

    gluPerspective(45, (DISPLAY[0]/DISPLAY[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    glRotatef(0, 0, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)

main()
