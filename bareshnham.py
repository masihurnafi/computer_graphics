import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def draw_pixel(x, y):
    """Plots a single point on the screen."""
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    glEnd()

def bresenham_line(x1, y1, x2, y2):
    """Generalized Bresenham's Line Algorithm handling all octants."""
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    
    # Determine the step direction (+1 or -1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    
    x, y = x1, y1

    # Case 1: Slope is less than or equal to 1 (|m| <= 1)
    if dx > dy:
        p = 2 * dy - dx  # Initial decision parameter
        for _ in range(dx + 1):
            draw_pixel(x, y)
            if p >= 0:
                y += sy
                p -= 2 * dx
            x += sx
            p += 2 * dy
            
    # Case 2: Slope is greater than 1 (|m| > 1)
    else:
        p = 2 * dx - dy  # Initial decision parameter
        for _ in range(dy + 1):
            draw_pixel(x, y)
            if p >= 0:
                x += sx
                p -= 2 * dy
            y += sy
            p += 2 * dx

def main():
    # Initialize Pygame and the window display
    pygame.init()
    display_width = 500
    display_height = 500
    pygame.display.set_mode((display_width, display_height), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Bresenham's Line Algorithm (Python)")

    # Initialize OpenGL settings
    glClearColor(0.0, 0.0, 0.0, 1.0) # Black background
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, display_width, 0, display_height) # Match screen pixel space
    
    # Main application loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen buffer
        glClear(GL_COLOR_BUFFER_BIT)
        
        # Set line drawing color to Green
        glColor3f(0.0, 1.0, 0.0) 
        
        # Test lines: varying slopes, directions, and vertical/horizontal types
        bresenham_line(50, 50, 450, 350)   # Shallow line
        bresenham_line(50, 450, 450, 100)  # Steep/negative slope line
        bresenham_line(250, 50, 250, 450)  # Perfectly vertical line
        bresenham_line(50, 250, 450, 250)  # Perfectly horizontal line

        # Swap buffers to display the rendered lines
        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()

if __name__ == "__main__":
    main()
