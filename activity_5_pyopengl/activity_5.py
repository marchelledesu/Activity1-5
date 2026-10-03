import math

import pygame
from pygame.locals import DOUBLEBUF, OPENGL
from OpenGL.GL import *
from OpenGL.GLU import *


pygame.init()
display = (800, 600)
try:
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
except pygame.error:
    print("OpenGL context unavailable in this environment. Activity 5 requires a desktop display with OpenGL support.")
    raise SystemExit(0)
pygame.display.set_caption("Activity 5: Hardware-Accelerated 3D Pipeline")

# Perspective setup.
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

glEnable(GL_DEPTH_TEST)
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

def draw_cube(size=1.0):
    vertices = [
        [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
        [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1],
    ]
    faces = [
        (0, 1, 2, 3), (4, 5, 6, 7),
        (0, 1, 5, 4), (1, 2, 6, 5),
        (2, 3, 7, 6), (3, 0, 4, 7),
    ]
    colors = [(1, 0, 0, 0.8), (0, 1, 0, 0.8), (0, 0, 1, 0.8), (1, 1, 0, 0.8), (1, 0, 1, 0.8), (0, 1, 1, 0.8)]

    for face, color in zip(faces, colors):
        glBegin(GL_QUADS)
        glColor4f(*color)
        for index in face:
            x, y, z = [vertices[index][i] * size for i in range(3)]
            glVertex3f(x, y, z)
        glEnd()


def draw_axis():
    glBegin(GL_LINES)
    glColor3f(1, 0, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(2, 0, 0)

    glColor3f(0, 1, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 2, 0)

    glColor3f(0, 0, 1)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, 2)
    glEnd()


angle = 0.0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0.05, 0.07, 0.1, 1.0)

    glPushMatrix()
    glRotatef(angle, 1, 0.4, 0.3)
    draw_axis()
    draw_cube(1.0)
    glPopMatrix()

    pygame.display.flip()
    pygame.time.wait(16)
    angle += 1.0

pygame.quit()


if __name__ == "__main__":
    pass
