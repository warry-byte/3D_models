from typing import Tuple

from solid2 import OpenSCADObjectPlus, linear_extrude, translate, text

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