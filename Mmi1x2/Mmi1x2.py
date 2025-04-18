import gdspy
from Component.Component import Component

class MMI1X2(Component):
    """
    Loss is 0.06 dB for 1550 nm.\n
    Ref: https://doi.org/10.1364/OFC.2016.W2A.19
    """
    
    def __init__(self, layer: int=12) -> None:
        
        # Attributes
        self.obj = []
        self.port = {}

        # Draw your design here.
        vtx = [(0, -0.6),
               (1, -0.6),
               (1, -1.8),
               (12.5, -1.8),
               (12.5, -1.5),
               (13.5, -1.5),
               (13.5, -0.3),
               (12.5, -0.3),
               (12.5, 0.3),
               (13.5, 0.3),
               (13.5, 1.5),
               (12.5, 1.5),
               (12.5, 1.8),
               (1, 1.8),
               (1, 0.6),
               (0, 0.6)]

        mmi = gdspy.Polygon(vtx, layer=layer)
        
        # Update self.obj with new objects
        self.obj.append(mmi)

        # Update self.port
        self.port.update({'o0': (0, 0, 0),
                          'o1': (13.5, -0.9, 0),
                          'o2': (13.5, 0.9, 0)})