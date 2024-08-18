from enum import Enum
from solid2 import *
import numpy as np

set_global_fn(100)


def connect_points(p1, p2, cylinder_radius, color="blue"):
    """
    Draw cylinder by giving a start point and an end point.
    :param p1: Center coordinates of point 1
    :param p2: Center coordinates of point 2
    :return:
    """
    dist = np.linalg.norm(p2 - p1)  # dist = R in spherical coords - not to confuse with r of cylinder
    s2_s1 = (p2 - p1) / dist  # unit vector
    x = s2_s1[0]
    y = s2_s1[1]
    z = s2_s1[2]
    theta_deg = np.arccos(z / 1) * 180 / np.pi

    if not (x == 0 and y == 0):
        phi_deg = np.sign(y) * np.arccos(
            x / (np.sqrt(x**2 + y**2))
        ) * 180 / np.pi
    else:
        phi_deg = 0

    b = cylinder(
        r=cylinder_radius, h=dist
    ).rotateY(theta_deg).rotateZ(phi_deg).translate(p1).color(color)
    # ).rotateY(90).rotateZ(phi_deg).color(color)

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

# Connect spheres
# S0 to Si
for i in range(3):
    b = connect_points(
        sphere_coords[0], sphere_coords[i+1], bridge_radius, colors[i]
    )
    bridges.append(b)

# Bottom bridges
b = connect_points(
    sphere_coords[1], sphere_coords[2], bridge_radius, colors[0]
)
bridges.append(b)
b = connect_points(
    sphere_coords[1], sphere_coords[3], bridge_radius, colors[0]
)
bridges.append(b)
b = connect_points(
    sphere_coords[2], sphere_coords[3], bridge_radius, colors[0]
)
bridges.append(b)

# Tetrahedron center and connect bridges
center_coord = np.asarray([0, 0, edge_length * np.sqrt(6)/12])
s = sphere(sphere_radius).translate(center_coord)
spheres.append(s)

for i in range(4):
    b = connect_points(center_coord, sphere_coords[i], bridge_radius)
    bridges.append(b)

combined_model = union()(spheres, bridges)
combined_model.save_as_scad()
