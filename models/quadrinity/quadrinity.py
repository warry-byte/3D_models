from enum import Enum
from solid2 import *
import numpy as np

set_global_fn(100)


def connect_two_spheres(s1, s2, cylinder_radius, color="blue"):
    """
    Make a bridge between two spheres.
    :param s1: Center coordinates of sphere 1
    :param s2: Center coordinates of sphere 2
    :return:
    """
    dist = np.linalg.norm(s2 - s1)  # dist = R in spherical coords - not to confuse with r of cylinder
    s2_s1 = (s2 - s1) / dist
    x = s2_s1[0]
    y = s2_s1[1]
    z = s2_s1[2]
    theta_deg = np.arccos(z / dist) * 180 / np.pi
    phi_deg = np.arcsin(
        y / (dist * np.sin(theta_deg))
    ) * 180 / np.pi

    b = cylinder(
        r=cylinder_radius, h=dist
    # ).rotateY(theta_deg).rotateZ(phi_deg).translate(s1).color(color)
    ).rotateY(theta_deg).color(color)

    return b


sphere_radius = 0.2
# quadrinity_radius = 2
bridge_radius = 0.1  # TODO choose a more meaningful value
spheres = []
bridges = []

# Spherical coordinates of the 4 corners.
# Physics conventions (R, phi, theta) (phi = rotateZ, theta = angle with Z axis)
# To translate this into OpenSCAD, we do:
# Translate in Z
# RotateY (for theta rotation)
# RotateZ (because Phi is always rotateZ)
# edge_length = quadrinity_radius * np.sqrt(3)
edge_length = 3

# sphere_coords = np.asarray([
#     [quadrinity_radius, 0, 0], # S0
#     [quadrinity_radius, 120, 0],
#     [quadrinity_radius, 120, 120],
#     [quadrinity_radius, 120, 240]]  # S3
# )
sphere_coords = np.asarray([
    [0, 0, edge_length * np.sqrt(6) / 3],  # S0
    [0, -edge_length * np.sqrt(3) / 3, 0],
    [-edge_length / 2, edge_length * np.sqrt(3) / 6, 0],
    [edge_length / 2, edge_length * np.sqrt(3) / 6, 0]]  # S3
)

colors = ["red", "green", "blue", "yellow"]  # Useful for debugging

for i in range(4):
    s = (sphere(sphere_radius)
         .translate(sphere_coords[i])
         )

    spheres.append(s)

    # Bridge spheres S0 to S3 with cylinders
    b = connect_two_spheres(
        sphere_coords[(i + 1) % 4], sphere_coords[i], bridge_radius, colors[i]
    )
    bridges.append(b)

combined_model = union()(spheres, bridges)
combined_model.save_as_scad()
