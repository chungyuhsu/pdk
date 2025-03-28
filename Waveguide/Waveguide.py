import gdspy
from Component.Component import Component

class Waveguide(Component):
    """
    Loss: -1 dB/cm for width = 1.2 µm\n
    **width_in** : Initial waveguide width
    **length** : Waveguide length
    **width_out** : Final waveguide width
    **layer** : Layer of waveguide
    """
    
    def __init__(self, width_in: float, length: float, width_out: float = None, layer: int = 12) -> None:
        
        # Attributes
        self.obj = []
        self.port = {'og': (0, 0, 0)}
        self.layer = [layer]
        
        self.width_in = width_in
        self.width_out = width_out
        self.length = length

        # Draw your design here. Everything respects to port 'og'.
        path = gdspy.Path(width_in)
        path.segment(length, final_width=width_out, layer=layer)
        
        # Update self.obj with new objects
        self.obj.append(path)

        # Update self.port
        self.port.update({'o0': (0, 0, 0),
                          'o1': (length, 0, 0)})