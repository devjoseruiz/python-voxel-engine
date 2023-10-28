import moderngl as mgl
import pygame as pg

from settings import *


class Textures:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx

        # load texture
        self.texture_0 = self.load('frame.png')

        # assign texture unit
        self.texture_0.use(location=0)

    def load(self, file_name):
        texture = pg.image.load(f'{ROOT_DIR}/assets/{file_name}')
        texture = pg.transform.flip(texture, flip_x=True, flip_y=False)

        texture = self.ctx.texture(
            size=texture.get_size(),
            components=4,
            data=pg.image.tostring(texture, 'RGBA', False)
        )
        texture.anisotropy = 32.0
        texture.build_mipmaps()
        texture.filter = (mgl.NEAREST, mgl.NEAREST)
        return texture
