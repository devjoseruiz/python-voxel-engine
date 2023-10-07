from settings import *


class ShaderProgram:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx # point to opengl context
        # ---------- shaders ---------- #
        self.quad = self.get_program(shader_name='quad')
        # ----------------------------- #
        self.set_uniforms_on_init()

    def set_uniforms_on_init(self):
        pass

    # update uniforms
    def update(self):
        pass

    # load shaders
    def get_program(self, shader_name):
        with open(f'{ROOT_DIR}/shaders/{shader_name}.vert') as file:
            vertex_shader = file.read()

        with open(f'{ROOT_DIR}/shaders/{shader_name}.frag') as file:
            fragment_shader = file.read()

        program = self.ctx.program(vertex_shader=vertex_shader,
                                   fragment_shader=fragment_shader)