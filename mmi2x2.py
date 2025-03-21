import gdspy
from .component import Component

class Mmi2x2(Component):
    """
    Loss is ≤0.15±0.01 dB for 1530-1565 nm.\n
    Ref: https://doi.org/10.1109/JPHOT.2012.2230320
    """
    
    def __init__(self) -> None:
        
        # Attributes
        self.obj = []
        self.port = {'og': (0, 0, 0)}
        self.layer = [12]

        # Draw your design here. Everything respects to port 'og'.
        wg0 = gdspy.Rectangle((-1, -1.75), (0, -0.25), layer=self.layer[0])
        wg1 = gdspy.Rectangle((-1, 1.75), (0, 0.25), layer=self.layer[0])
        body = gdspy.Rectangle((0, -1.9), (51.5, 1.9), layer=self.layer[0])
        wg2 = gdspy.Rectangle((51.5, -1.75), (52.5, -0.25), layer=self.layer[0])
        wg3 = gdspy.Rectangle((51.5, 1.75), (52.5, 0.25), layer=self.layer[0])
        
        # Update self.obj with new objects
        self.obj.extend([wg0, wg1, wg2, wg3, body])

        # Update self.port
        self.port.update({'o0': (-1, -1, 0),
                          'o1': (-1, 1, 0),
                          'o2': (52.5, -1, 0),
                          'o3': (52.5, 1, 0)})

if __name__ == "__main__":
    
    Mmi2x2().put('og', (0, 0, 0))
    
    gdspy.write_gds('mmi2x2.gds')