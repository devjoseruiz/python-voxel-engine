import moderngl as mgl

from settings import *
from world import World
from world_objects.water import Water


class Scene:
    def __init__(self, app):
        self.app = app
        self.world = World(self.app)
        self.water = Water(app)

    def render(self):
        # chunks rendering
        self.world.render()

        # rendering without cull face
        self.app.ctx.disable(mgl.CULL_FACE)
        self.water.render()
        self.app.ctx.enable(mgl.CULL_FACE)
