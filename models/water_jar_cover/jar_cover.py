# import openscad
from solid2 import cylinder, sphere, polygon
import numpy as np

from utils.utils import make_label

# assuming cm

text_size = 2
jar_label = "Jean-Michel"
jar_label2 = "Jarre"
jar_label_depth = 0.8

insert = cylinder(h=2, r=14.2, _fn=300)
base = cylinder(h=1, r=16.2, _fn=300)
jar_label_model = make_label(message=jar_label,
                 text_loc=(0, 3),
                 text_size=text_size,
                 height=jar_label_depth+0.1)  # add 0.1 to avoid zero thickness features
jar_label_model2 = make_label(message=jar_label2,
                 text_loc=(0, -3),
                 text_size=text_size,
                 height=jar_label_depth+0.1)  # add 0.1 to avoid zero thickness features

# Create a nice wobbly circle
diam = 13
oscillation_diam = 1
angles_rad = [a * np.pi / 180 for a in range(0, 360, 3)]
wobbly_depth = 0.3

polygon_points = list()

# Putting in a loop for more clarity (not very time-consuming anyway)
for a in angles_rad:
    oscillation_period_deg = 45  # 1 oscillation over defined angle
    oscillation_period_rad = oscillation_period_deg * np.pi / 180
    oscillation_diam = diam + np.cos(2 * np.pi * a / oscillation_period_rad)
    x_coord = oscillation_diam * np.cos(a)
    y_coord = oscillation_diam * np.sin(a)
    polygon_points.append((x_coord, y_coord))

lid_cavity = polygon(polygon_points)  # also to avoid zero thickness (we extrude from a lower Z
# position)

# Create handle for the lid cover: first, create a cylinder that will attach to the main lid
# Then, create a cylinder in the other direction in Z, that will connect to a sphere (handle)
handle = (cylinder(h=wobbly_depth+0.3, _fn=100, r=1)
          + cylinder(h=3, r=1, _fn=100).mirrorZ()
          + sphere(d=3.5, _fn=100).translateZ(-(3+wobbly_depth)))

# Create final model
# model = insert + base - lid_cavity.linear_extrude(height=0.3+0.1).translateZ(-0.1)
model = (insert + base - lid_cavity.linear_extrude(height=wobbly_depth+0.1).translateZ(-0.1)
         - jar_label_model.translateZ(-0.1).mirrorY()
         - jar_label_model2.translateZ(-0.1).mirrorY()
         + handle)


# save your model for use in OpenSCAD
model.save_as_scad()