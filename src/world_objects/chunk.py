from meshes.chunk_mesh import ChunkMesh
from settings import *


class Chunk:
    def __init__(self, world, position):
        self.app = world.app
        self.world = world
        self.position = position
        self.m_model = self.get_model_matrix()
        self.voxels: np.array = None
        self.mesh: ChunkMesh = None

    def get_model_matrix(self):
        m_model = glm.translate(glm.mat4(), glm.vec3(self.position) * CHUNK_SIZE)
        return m_model

    def set_uniform(self):
        self.mesh.program['m_model'].write(self.m_model)

    def build_mesh(self):
        self.mesh = ChunkMesh(self)

    def render(self):
        self.set_uniform()
        self.mesh.render()

    def build_voxels(self):
        # empty chunk
        voxels = np.zeros(CHUNK_VOL, dtype='uint8')

        # fill chunk
        for x in range(CHUNK_SIZE):
            for z in range(CHUNK_SIZE):
                for y in range(CHUNK_SIZE):
                    voxels[x + CHUNK_SIZE * z + CHUNK_AREA * y] = (
                        x + y + z if int(glm.simplex(glm.vec3(x, y, z) * 0.1) + 1) else 0
                    )
        return voxels
