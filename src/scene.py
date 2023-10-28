from meshes.quad_mesh import QuadMesh
from settings import *


class Scene:
    def __init__(self, app):
        self.app = app
        self.quad = QuadMesh(self.app)
    
    def update(self):
        pass

    def render(self):
        self.quad.render()
