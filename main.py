import glfw
from OpenGL.GL import *

def main():
    if not glfw.init():
        raise SystemExit("GLFW init failed")

    window = glfw.create_window(800, 600, "HCI-CG Lab 01", None, None)
    if not window:
        glfw.terminate()
        raise SystemExit("Could not create window")

    glfw.make_context_current(window)

    print("GL %s on %s" % (
        glGetString(GL_VERSION).decode(),
        glGetString(GL_RENDERER).decode()))

    while not glfw.window_should_close(window):
        glClearColor(0.95, 0.50, 0.10,1)
        glClear(GL_COLOR_BUFFER_BIT)
        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

main()