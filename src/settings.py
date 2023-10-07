import math
import os

import glm
import numpy as np
from numba import njit

# src folder path
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# resolution
WIN_RES = glm.vec2(1600, 900)

# colors
BG_COLOR = glm.vec3(0.1, 0.16, 0.25)