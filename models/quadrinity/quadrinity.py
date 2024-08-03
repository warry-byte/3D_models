from solid2 import *
import numpy as np

set_global_fn(100)

sphere_radius = 0.2
quadrinity_radius = 2
bridge_radius = 0.1  # TODO choose a more meaningful value
spheres = []
bridges = []
angle = 2*np.pi/3
edge_length = quadrinity_radius*np.sqrt(3)  # Edge: cos30° = Edge/2/radius <-> edge = 2r cos30° = 2r.sqrt(3)/2 = r sqrt(3)

# Spheres S0 to S2: place first sphere at eg (2, 0, 0), then rotate at 120° 3 times
spheres_coords = quadrinity_radius*np.asarray(
    [[1, 0, 0],
    [np.cos(angle), np.sin(angle), 0],
    [np.cos(2*angle), np.sin(2*angle), 0]]
)
for i in range(3):
    s = sphere(sphere_radius).translate(spheres_coords[i, :])
    spheres.append(s)

    # Bridge spheres S0 to S2 with cylinders
    b = (cylinder(
            r=bridge_radius,
            h=edge_length
        )
    .rotateY(90)
    .rotateZ(30+120*(i+1))
    .translate(spheres_coords[i, :]))

    bridges.append(b)

# Sphere S3: Must be placed such that the 6 edges of the quadrinity are of equal length
# alpha: angle O-S0-S3. We have cos(alpha) = r/edge
alpha_rad = np.arccos(quadrinity_radius/edge_length)
h = quadrinity_radius * np.tan(alpha_rad)  # height of S3
s = (sphere(sphere_radius)
     .translateZ(h))
spheres.append(s)

# Bridge sphere S3 with other spheres
for i in range(3):
    b = (cylinder(
        r=bridge_radius,
        h=edge_length
    )
         .rotateY(90+alpha_rad*180/np.pi)
         .rotateZ(i * 120)
         .translateZ(h)
    )
    bridges.append(b)

combined_model = union()(spheres, bridges)
combined_model.save_as_scad()