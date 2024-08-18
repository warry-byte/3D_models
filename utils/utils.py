from typing import Tuple
import numpy as np

from solid2 import OpenSCADObjectPlus, linear_extrude, translate, text, cylinder


def make_label(message: str,
               text_loc: Tuple[float, float],
               text_size=0.5,
               height=5,
               font="gordion") -> OpenSCADObjectPlus:

    return translate(text_loc)(
        linear_extrude(height)(
            text(text=message,
                 size=text_size,
                 halign="center",
                 valign="center",
                 _fn=100,
                 font=font)
        )
    )


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
            x / (np.sqrt(x ** 2 + y ** 2))
        ) * 180 / np.pi
    else:
        phi_deg = 0

    b = (cylinder(r=cylinder_radius, h=dist)
         .rotateY(theta_deg)
         .rotateZ(phi_deg)
         .translate(p1).color(color)
         )

    return b