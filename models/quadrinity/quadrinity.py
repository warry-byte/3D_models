from solid2 import *
import numpy as np

set_global_fn(100)

sphere_radius = 0.2
quadrinity_radius = 2
spheres = []
edges = []
spheres_coords = np.asarray([[quadrinity_radius, 0, 0],
                  [-quadrinity_radius*np.sqrt(3)/2, -1/2, 0],
                  [1/2, quadrinity_radius*np.sqrt(3)/2, 0]])

# Spheres S0 to S2: place first sphere at eg (0, 2, 0), then rotate at 120° 3 times
for angle in [0, 120, 240]:
    s = (sphere(sphere_radius)
         .translateY(-quadrinity_radius)
         .rotateZ(angle))  # Spheres S0 to S2
    spheres.append(s)

# Sphere S3: Must be placed such that the 6 edges of the quadrinity are of equal length
# Edge: cos30° = Edge/2/radius <-> edge = 2r cos30° = 2r.sqrt(3)/2 = r sqrt(3)
edge = quadrinity_radius * np.sqrt(3)
# alpha: angle O-S0-S3. We have cos(alpha) = r/edge
alpha = np.arccos(quadrinity_radius/edge)
h = quadrinity_radius * np.tan(alpha)  # height of S3
s = (sphere(sphere_radius)
     .translateZ(h))
spheres.append(s)

combined_model = union()(spheres)
combined_model.save_as_scad()