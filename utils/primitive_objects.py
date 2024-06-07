# Define the vertices of the polyhedron
from solid2 import polyhedron, OpenSCADObjectPlus


def make_septahedron() -> OpenSCADObjectPlus:
    points = [
        (0, 1, 0),  # A
        (0.5, 0.5, 0.5),  # B
        (1, 0, 0),  # C
        (0.5, -0.5, 0.5),  # D
        (0, -1, 0),  # E
        (-0.5, -0.5, 0.5),  # F
        (-1, 0, 0),  # G
        (-0.5, 0.5, 0.5),  # H
    ]

    # Define the faces of the polyhedron
    faces = [
        [0, 1, 2],  # ABC
        [0, 2, 3],  # ACD
        [0, 3, 4],  # ADE
        [0, 4, 5],  # AEF
        [0, 5, 6],  # AFG
        [0, 6, 7],  # AGH
        [0, 7, 1],  # AHB
    ]

    # Generate the polyhedron
    septahedron_model = polyhedron(points=points, faces=faces)

    return septahedron_model


def make_dodecahedron() -> OpenSCADObjectPlus:

    # Golden ratio
    phi = (1 + 5 ** 0.5) / 2

    # Define the vertices of the dodecahedron
    points = [
        (1, 1, 1), (-1, 1, 1), (-1, -1, 1), (1, -1, 1),
        (0, 1 / phi, phi), (0, -1 / phi, phi), (phi, 0, 1 / phi),
        (-phi, 0, 1 / phi), (1 / phi, phi, 0), (-1 / phi, phi, 0),
        (1 / phi, -phi, 0), (-1 / phi, -phi, 0),
        (phi, 0, -1 / phi), (-phi, 0, -1 / phi),
        (0, 1 / phi, -phi), (0, -1 / phi, -phi),
        (1, 1, -1), (-1, 1, -1), (-1, -1, -1), (1, -1, -1)
    ]

    # Define the faces of the dodecahedron
    faces = [
        [0, 1, 4, 7, 2], [0, 2, 6, 9, 3], [0, 3, 8, 5, 1],
        [10, 11, 6, 2, 7], [10, 7, 4, 13, 14], [10, 14, 15, 8, 3],
        [18, 17, 12, 5, 8], [18, 15, 14, 13, 16], [18, 16, 17, 11, 10],
        [9, 6, 11, 17, 16], [9, 16, 13, 4, 1], [9, 1, 5, 12, 19]
    ]

    # Generate the dodecahedron
    dodecahedron_model = polyhedron(points=points, faces=faces)

    return dodecahedron_model
