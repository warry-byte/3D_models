from enum import Enum
from solid2 import *
from utils.utils import connect_points

import numpy as np


def quadrinity(
        edge_length=3,
        sphere_radius=0.2,
        bridge_radius=0.1
):
    spheres = []
    bridges = []

    # Spherical coordinates of the 4 corners
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
            sphere_coords[0], sphere_coords[i + 1], bridge_radius, colors[i]
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
    center_coord = np.asarray([0, 0, edge_length * np.sqrt(6) / 12])
    s = sphere(sphere_radius).translate(center_coord)
    spheres.append(s)

    for i in range(4):
        b = connect_points(center_coord, sphere_coords[i], bridge_radius)
        bridges.append(b)

    return spheres, bridges


if __name__ == "main":
    set_global_fn(100)
    spheres, bridges = quadrinity()
    combined_model = union()(spheres, bridges)
    combined_model.save_as_scad()
