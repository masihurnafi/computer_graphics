import glfw
from OpenGL.GL import *
from OpenGL.GLU import *

def draw_pixel(x, y):
    """Plots a single point on the screen."""
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    glEnd()

def midpoint_line(x1, y1, x2, y2):
    """Midpoint Line Drawing Algorithm handling all octants."""
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1

    x, y = x1, y1

    if dx > dy:
        d = 2 * dy - dx
        delta_e = 2 * dy
        delta_ne = 2 * (dy - dx)
        for _ in range(dx + 1):
            draw_pixel(x, y)
            if d <= 0:
                d += delta_e
            else:
                d += delta_ne
                y += sy
            x += sx
    else:
        d = 2 * dx - dy
        delta_e = 2 * dx
        delta_ne = 2 * (dx - dy)
        for _ in range(dy + 1):
            draw_pixel(x, y)
            if d <= 0:
                d += delta_e
            else:
                d += delta_ne
                x += sx
            y += sy

def midpoint_circle(xc, yc, r):
    """Midpoint Circle Drawing Algorithm, 8-way symmetry."""
    x = 0
    y = r
    d = 1 - r

    def plot_points(x, y):
        draw_pixel(xc + x, yc + y)
        draw_pixel(xc - x, yc + y)
        draw_pixel(xc + x, yc - y)
        draw_pixel(xc - x, yc - y)
        draw_pixel(xc + y, yc + x)
        draw_pixel(xc - y, yc + x)
        draw_pixel(xc + y, yc - x)
        draw_pixel(xc - y, yc - x)

    plot_points(x, y)
    while x < y:
        x += 1
        if d < 0:
            d += 2 * x + 1
        else:
            y -= 1
            d += 2 * (x - y) + 1
        plot_points(x, y)

def main():
    if not glfw.init():
        raise RuntimeError("Failed to init GLFW")

    display_width = 500
    display_height = 500
    window = glfw.create_window(display_width, display_height,
                                 "Midpoint Line & Circle Algorithm (Python)", None, None)
    if not window:
        glfw.terminate()
        raise RuntimeError("Failed to create GLFW window")

    glfw.make_context_current(window)

    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, display_width, 0, display_height)

    while not glfw.window_should_close(window):
        glfw.poll_events()

        glClear(GL_COLOR_BUFFER_BIT)

        glColor3f(0.0, 1.0, 0.0)
        midpoint_line(50, 50, 450, 350)
        midpoint_line(50, 450, 450, 100)
        midpoint_line(250, 50, 250, 450)
        midpoint_line(50, 250, 450, 250)

        glColor3f(1.0, 0.0, 0.0)
        midpoint_circle(250, 250, 250)

        glfw.swap_buffers(window)

    glfw.terminate()

if __name__ == "__main__":
    main()
