import gdspy
import numpy as np
from Component.Component import Component

def arrow(location: tuple) -> list:
    """
    **location** : Polar coordinate (r, θ). θ is in degree.
    """

    vtx = [(0, 0),
           (4, 3),
           (4, 1.5),
           (10, 1.5),
           (10, -1.5),
           (4, -1.5),
           (4, -3)]
    
    # Translate
    vtx_new = []
    for i in vtx:
        x = i[0] + location[0]
        y = i[1]
        vtx_new.append((x, y))
    vtx = vtx_new

    # Rotate
    theta = location[1] / 180 * np.pi # degree -> radian
    vtx_new = []
    for i in vtx:
        x = i[0] * np.cos(theta) - i[1] * np.sin(theta)
        y = i[0] * np.sin(theta) + i[1] * np.cos(theta)
        vtx_new.append((x, y))
    vtx = vtx_new
    
    return vtx

class AlignEBL(Component):
    """
    Alignment mark for Ebeam.
    """
    
    def __init__(self, layer: int = 11) -> None:
        
        # Attributes
        self.obj = []
        self.port = {}
        
        #----- center boxes -----
        self.obj.append(gdspy.Rectangle((-1, -1), (0, 0), layer=layer))
        self.obj.append(gdspy.Rectangle((0, 0), (1, 1), layer=layer))
            
        #----- arrows -----
        # four arrows near boxes
        for i in range(4):
                arrow_ = arrow(location=(2, 90 * i))
                arrow_ = gdspy.Polygon(arrow_, layer=layer)
                self.obj.append(arrow_)

        for i in range(11):
            for j in range(12):
                arrow_ = arrow(location=(22 + 20 * i, 30 * j))
                arrow_ = gdspy.Polygon(arrow_, layer=layer)
                self.obj.append(arrow_)

        # Update self.port
        self.port.update({'og': (0, 0, 0)})