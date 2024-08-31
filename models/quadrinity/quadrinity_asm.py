import numpy as np

from quadrinity import quadrinity
from solid2 import *

from utils.utils import get_object_rotated_around_edge

quad_list = []
set_global_fn(10)

combined_model = quadrinity()

for x in range(2):
    combined_model += quadrinity().translateX(3 * x)


# Adding top of the y triangle
combined_model += quadrinity().translateX(3/2).translateY(-3 * np.sqrt(3) / 2)  # Translate Y by the height of a face

# Adding inner quadrinity, inside the formed quadrinity trinity
# axis = [3 * np.sqrt(3) / 2, 3/2, 0]
# axis = np.asarray([0, -3 * np.sqrt(3) / 3, 0]) - np.asarray([-3 / 2, 3 * np.sqrt(3) / 6, 0])
vertex2 = np.asarray([0, -3 * np.sqrt(3) / 3, 0])
vertex1 = np.asarray([-3 / 2, 3 * np.sqrt(3) / 6, 0])
axis = vertex2 - vertex1
mid_point = (vertex1 - vertex2) / 2
# check where is the middle point (debug)
# combined_model += sphere(0.1).translate(mid_point + vertex2)
# center_coord = np.asarray([0, 0, 3 * np.sqrt(6) / 12])
interior_quad = quadrinity().translate(-mid_point-vertex2).rotate(v=axis, a=70.53).translate(mid_point+vertex2)
# interior_quad = (quadrinity().rotate(a=45, v=axis))
                 #.rotateY(180).translateY(-3 * np.sqrt(3) / 3 + 3 * np.sqrt(3) / 6).translateX(3/2).translateZ(3 * np.sqrt(6) / 3))
combined_model += interior_quad

# Adding top quadrinity in Z
# combined_model += quadrinity().translateY(-3 * np.sqrt(3) / 3 + 3 * np.sqrt(3) / 6).translateX(3/2).translateZ(3 * np.sqrt(6) / 3)

combined_model.save_as_scad()
