import gdspy
from component import Component

class Mmi1x2(Component):
    """
    Loss is 0.06 dB for 1550 nm.\n
    Ref: https://doi.org/10.1364/OFC.2016.W2A.19
    """
    
    def __init__(self) -> None:
        
        # Attributes
        self.obj = []
        self.port = {'og': (0, 0, 0)}
        self.layer = [12]

        # Draw your design here. Everything respects to port 'og'.
        wg0 = gdspy.Rectangle((0, -0.6), (1, 0.6), layer=self.layer[0])
        body = gdspy.Rectangle((1, -1.8), (12.5, 1.8), layer=self.layer[0])
        wg1 = gdspy.Rectangle((12.5, -1.5), (13.5, -0.3), layer=self.layer[0])
        wg2 = gdspy.Rectangle((12.5, 0.3), (13.5, 1.5), layer=self.layer[0])
        
        # Update self.obj with new objects
        self.obj.extend([wg0, wg1, wg2, body])

        # Update self.port
        self.port.update({'o0': (0, 0, 0),
                          'o1': (13.5, -0.9, 0),
                          'o2': (13.5, 0.9, 0)})

if __name__ == "__main__":
    
    Mmi1x2().put('o0', (0, 0, 0))
    
    gdspy.write_gds('mmi1x2.gds')