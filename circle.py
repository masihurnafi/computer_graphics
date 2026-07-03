import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


# Draw a single pixel
def draw_pixel(x, y):
    glVertex2i(x, y)


# Plot the 8 symmetric points
def plot_circle_points(xc, yc, x, y):
    draw_pixel(xc + x, yc + y)
    draw_pixel(xc - x, yc + y)
    draw_pixel(xc + x, yc - y)
    draw_pixel(xc - x, yc - y)
    draw_pixel(xc + y, yc + x)
    draw_pixel(xc - y, yc + x)
    draw_pixel(xc + y, yc - x)
    draw_pixel(xc - y, yc - x)


# Bresenham Circle Algorithm
def bresenham_circle(xc, yc, r):
    x = 0
    y = r
    d = 3 - 2 * r

    glBegin(GL_POINTS)

    plot_circle_points(xc, yc, x, y)

    while y >= x:
        x += 1

        if d > 0:
            y -= 1
            d = d + 4 * (x - y) + 10
        else:
            d = d + 4 * x + 6

        plot_circle_points(xc, yc, x, y)

    glEnd()


def main():
    pygame.init()

    width = 600
    height = 600

    pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Bresenham Circle Drawing Algorithm")

    # Background color
    glClearColor(0.0, 0.0, 0.0, 1.0)

    # White drawing color
    glColor3f(1.0, 1.0, 1.0)

    # Draw 1-pixel points
    glPointSize(1.0)

    # Projection
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    running = True

    while running:

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        glClear(GL_COLOR_BUFFER_BIT)

        # Draw circle
        bresenham_circle(300, 300, 150)

        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()


if __name__ == "__main__":
    main()
