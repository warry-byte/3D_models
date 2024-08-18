from solid2 import *

# Step 1: Define and Translate Primitive Objects
translated_cube = cube([10, 10, 10]).translate([5, 0, 0])
translated_sphere = sphere(5).translate([0, 5, 0])

# Step 2: Create a Union of the Translated Primitives
combined = translated_cube + translated_sphere

# Step 3: Optionally Translate the Entire Union (if needed)
final_object = combined.translate([20, 30, 40])

# Step 4: Render the result
scad_render_to_file(final_object, 'translated_combined_union2.scad')
