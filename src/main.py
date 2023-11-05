import sys

import moderngl as mgl
import pygame as pg

from player import Player
from scene import Scene
from settings import *
from shader_program import ShaderProgram
from textures import Textures


class VoxelEngine:
    def __init__(self):
        pg.init() # initialize pygame
        # set some opengl attributes such as opengl version
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3) 
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK,
                                    pg.GL_CONTEXT_PROFILE_CORE)
        pg.display.gl_set_attribute(pg.GL_DEPTH_SIZE, 24)

        # set window resolution and create opengl context
        pg.display.set_mode(WIN_RES, flags=pg.OPENGL | pg.DOUBLEBUF)
        self.ctx = mgl.create_context()

        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE | mgl.BLEND)
        self.ctx.gc_mode = 'auto' # enable automatic garbage collection

        self.clock = pg.time.Clock()
        self.delta_time = 0
        self.time = 0

        pg.event.set_grab(True)
        pg.mouse.set_visible(False)

        self.is_running = True
        self.on_init()

    def on_init(self):
        self.textures = Textures(self)
        self.player = Player(self)
        self.shader_program = ShaderProgram(self)
        self.scene = Scene(self)

    # update state of objects
    def update(self):
        self.player.update()
        self.shader_program.update()

        self.delta_time = self.clock.tick()
        self.time = pg.time.get_ticks() * 0.001
        # show fps on screen
        pg.display.set_caption(f'{self.clock.get_fps() :.0f}')

    def render(self):
        self.ctx.clear(color=BG_COLOR) # clear buffers
        self.scene.render()
        pg.display.flip() # display new frames

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.is_running = False

    def run(self):
        while self.is_running:
            self.handle_events()
            self.update()
            self.render()
        
        pg.quit()
        sys.exit()

if __name__ == '__main__':
    app = VoxelEngine()
    app.run()