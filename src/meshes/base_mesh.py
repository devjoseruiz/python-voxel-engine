import numpy as np


class BaseMesh:
    def __init__(self):
        # opengl context
        self.ctx = None
        # shader program
        self.program = None
        # vertex buffer data type format: "3f 3f"
        self.vbo_format = None
        # attribute name according to the format: ("in_position", "in_color")
        # caution: you should handle the case when self.attrs is None
        self.attrs: tuple[str, ...] = None
        # vertex array object
        self.vao = None

    def get_vertex_data(self) -> np.array: ...

    def get_vao(self):
        # obtain the vertex data that will be used to create the VAO
        vertex_data = self.get_vertex_data()
        # create a Vertex Buffer Object and populate it with the vertex data
        vbo = self.ctx.buffer(vertex_data)
        # create VAO that encapsulates a set of VBOs and vertex configurations
        vao = self.ctx.vertex_array(
            self.program, [(vbo, self.vbo_format, *self.attrs)],
            skip_errors= True
        )
        return vao # this can be used to render the voxel data efficiently

    def render(self):
        self.vao.render()
