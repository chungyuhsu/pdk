import gdspy
from Component.Component import Component

class MMI2X2(Component):
    """
    Loss is ≤0.15±0.01 dB for 1530-1565 nm.\n
    Ref: https://doi.org/10.1109/JPHOT.2012.2230320
    """
    
    def __init__(self, layer: int=12) -> None:
        
        # Attributes
        self.obj = []
        self.port = {}

        # Draw your design here.
        vtx = [(0, -0.25),
               (-1, -0.25),
               (-1, -1.75),
               (0, -1.75),
               (0, -1.9),
               (51.5, -1.9),
               (51.5, -1.75),
               (52.5, -1.75),
               (52.5, -0.25),
               (51.5, -0.25),
               (51.5, 0.25),
               (52.5, 0.25),
               (52.5, 1.75),
               (51.5, 1.75),
               (51.5, 1.9),
               (0, 1.9),
               (0, 1.75),
               (-1, 1.75),
               (-1, 0.25),
               (0, 0.25)]

        mmi = gdspy.Polygon(vtx, layer=layer)
        
        # Update self.obj with new objects
        self.obj.append(mmi)

        # Update self.port
        self.port.update({'o0': (-1, -1, 0),
                          'o1': (-1, 1, 0),
                          'o2': (52.5, -1, 0),
                          'o3': (52.5, 1, 0)})