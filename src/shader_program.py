from settings import *


class ShaderProgram:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx # point to opengl context
        self.player = app.player
        # ---------- shaders ---------- #
        self.quad = self.get_program(shader_name='quad')
        # ----------------------------- #
        self.set_uniforms_on_init()

    def set_uniforms_on_init(self):
        self.quad['m_proj'].write(self.player.m_proj)
        self.quad['m_model'].write(glm.mat4())

    # update uniforms
    def update(self):
        self.quad['m_view'].write(self.player.m_view)

    # load shaders
    def get_program(self, shader_name):
        with open(f'{ROOT_DIR}/shaders/{shader_name}.vert') as file:
            vertex_shader = file.read()

        with open(f'{ROOT_DIR}/shaders/{shader_name}.frag') as file:
            fragment_shader = file.read()

        program = self.ctx.program(vertex_shader=vertex_shader,
                                   fragment_shader=fragment_shader)
        return program