from settings import *
from world_objects.chunk import Chunk


class Scene:
    def __init__(self, app):
        self.app = app
        self.chunk = Chunk(self.app)
    
    def update(self):
        pass

    def render(self):
        self.chunk.render()
