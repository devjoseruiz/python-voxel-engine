import moderngl as mgl
import pygame as pg

from settings import *


class Textures:
    def __init__(self, app):
        self.app = app
        self.ctx = app.ctx

        # load textures
        self.texture_0 = self.load('frame.png')
        self.texture_array_0 = self.load('tex_array_0.png', is_tex_array=True)

        # assign texture unit
        self.texture_0.use(location=0)
        self.texture_array_0.use(location=1)

    def load(self, file_name, is_tex_array=False):
        texture = pg.image.load(f'{ROOT_DIR}/assets/{file_name}')
        texture = pg.transform.flip(texture, flip_x=True, flip_y=False)

        if is_tex_array:
            # 3 textures per layer
            num_layers = 3 * texture.get_height() // texture.get_width()
            texture = self.app.ctx.texture_array(
                size=(texture.get_width(), texture.get_height() // num_layers, num_layers),
                components=4,
                data=pg.image.tostring(texture, 'RGBA')
            )
        else:
            texture = self.ctx.texture(
                size=texture.get_size(),
                components=4,
                data=pg.image.tostring(texture, 'RGBA', False)
            )
        texture.anisotropy = 32.0
        texture.build_mipmaps()
        texture.filter = (mgl.NEAREST, mgl.NEAREST)
        return texture
