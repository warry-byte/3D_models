from solid2 import *

# Step 1: Define Primitive Objects
cube_1 = cube([10, 10, 10])
sphere_1 = sphere(5)

# Step 2: Create a Union of the Primitives
combined = union()(
    cube_1,
    sphere_1
)

# Step 3: Translate the Entire Union
combined = translate([2, 3, 4])(combined)

# Step 4: Render the result
scad_render_to_file(combined, 'translated_union.scad')
