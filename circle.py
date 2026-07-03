import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Helper function to plot a single pixel at (x, y)
def draw_pixel(x, y):
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    glEnd()

# Plots symmetric pixels across all 8 octants of the circle
def plot_circle_points(xc, yc, x, y):
    draw_pixel(xc + x, yc + y)
    draw_pixel(xc - x, yc + y)
    draw_pixel(xc + x, yc - y)
    draw_pixel(xc - x, yc - y)
    draw_pixel(xc + y, yc + x)
    draw_pixel(xc - y, yc + x)
    draw_pixel(xc + y, yc - x)
    draw_pixel(xc - y, yc - x)

# Bresenham's Circle Drawing Algorithm
def bresenham_circle(xc, yc, r):
    x = 0
    y = r
    d = 3 - (2 * r) # Initial decision parameter
    
    plot_circle_points(xc, yc, x, y)
    
    while y >= x:
        x += 1
        
        # Check decision parameter
        if d > 0:
            y -= 1
            d = d + 4 * (x - y) + 10
        else:
            d = d + 4 * x + 6
            
        plot_circle_points(xc, yc, x, y)

def main():
    # Initialize Pygame and creation window
    pygame.init()
    display_width = 500
    display_height = 500
    pygame.display.set_mode((display_width, display_height), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Bresenham's Circle Algorithm")

    # Set background color to black and point size larger for visibility
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glPointSize(5.0) 

    # Setup the projection grid matrix
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # View window limits set tight around (10, 10) to see the small circle clearly
    gluOrtho2D(0, 20, 0, 20) 

    # Main Application Loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glColor3f(1.0, 1.0, 1.0) # Set drawing color to White

        # Draw a circle with center (10, 10) and radius 5
        bresenham_circle(10, 10, 5)

        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()

if __name__ == "__main__":
    main()
