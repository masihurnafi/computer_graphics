import glfw
from OpenGL.GL import *
import numpy as np

VERTEX_SHADER = """
#version 330 core
layout(location = 0) in vec3 aPos;
layout(location = 1) in vec3 aColor;
out vec3 vertexColor;
void main() {
    gl_Position = vec4(aPos, 1.0);
    vertexColor = aColor;
}
"""

FRAGMENT_SHADER = """
#version 330 core
in vec3 vertexColor;
out vec4 FragColor;
void main() {
    FragColor = vec4(vertexColor, 1.0);
}
"""

def compile_shader(source, shader_type):
    shader = glCreateShader(shader_type)
    glShaderSource(shader, source)
    glCompileShader(shader)
    if not glGetShaderiv(shader, GL_COMPILE_STATUS):
        raise RuntimeError(glGetShaderInfoLog(shader).decode())
    return shader

def create_program():
    vs = compile_shader(VERTEX_SHADER, GL_VERTEX_SHADER)
    fs = compile_shader(FRAGMENT_SHADER, GL_FRAGMENT_SHADER)
    program = glCreateProgram()
    glAttachShader(program, vs)
    glAttachShader(program, fs)
    glLinkProgram(program)
    glDeleteShader(vs)
    glDeleteShader(fs)
    return program

def main():
    if not glfw.init():
        raise RuntimeError("Failed to initialize GLFW")

    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)

    window = glfw.create_window(800, 600, "OpenGL Triangle", None, None)
    if not window:
        glfw.terminate()
        raise RuntimeError("Failed to create GLFW window")

    glfw.make_context_current(window)

    vertices = np.array([
        # position         # color
        -0.5, -0.5, 0.0,  1.0, 0.0, 0.0,   # bottom-left  red
         0.5, -0.5, 0.0,  0.0, 1.0, 0.0,   # bottom-right green
         0.0,  0.5, 0.0,  0.0, 0.0, 1.0,   # top          blue
    ], dtype=np.float32)

    vao = glGenVertexArrays(1)
    vbo = glGenBuffers(1)

    glBindVertexArray(vao)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

    stride = 6 * vertices.itemsize
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, stride, ctypes.c_void_p(0))
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, stride, ctypes.c_void_p(3 * vertices.itemsize))
    glEnableVertexAttribArray(1)

    program = create_program()

    print("OpenGL Version:", glGetString(GL_VERSION).decode())
    print("Press ESC or close the window to quit.")

    while not glfw.window_should_close(window):
        glfw.poll_events()
        if glfw.get_key(window, glfw.KEY_ESCAPE) == glfw.PRESS:
            break

        glClearColor(0.1, 0.1, 0.1, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        glUseProgram(program)
        glBindVertexArray(vao)
        glDrawArrays(GL_TRIANGLES, 0, 3)

        glfw.swap_buffers(window)

    glDeleteVertexArrays(1, [vao])
    glDeleteBuffers(1, [vbo])
    glDeleteProgram(program)
    glfw.terminate()

if __name__ == "__main__":
    import ctypes
    main()
