import numpy as np

from quadrinity import quadrinity
from solid2 import *

quad_list = []
set_global_fn(10)

combined_model = quadrinity()

for i in range(10):
    combined_model += quadrinity().translateX((3) * i)
    combined_model += quadrinity().translateY((-3*np.sqrt(6)/3)).translateX(3/2+3*i)
combined_model.save_as_scad()
