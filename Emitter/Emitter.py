import gdspy
from Component.Component import Component

class Emitter(Component):
    """
    Shallow etched grating for light emitting.\n
    **width** : The width of the slab waveguide.\n
    **length** : The length of the slab waveguide.\n
    **period** : The period of the etched grating.\n
    **duty_cycle** : The duty cycle of the etched grating. `period × duty_cycle` is the length of the etched area.\n
    **layer** : A list with two elements. `layer = [slab waveguide, etched grating]`
    """
    
    def __init__(self, width: float, length: float, period: float, duty_cycle: float, layer: list = [12, 20]) -> None:
        
        # Attributes
        self.obj = []
        self.port = {}

        # Etching
        number_of_periods = round(length / period)
        length = period * number_of_periods
        
        etch = []
        for i in range(number_of_periods):
            etch_ = gdspy.Path(width + 2, initial_point=(period * i, 0))
            etch_.segment(period * duty_cycle, layer=layer[1])
            etch.append(etch_)

        # Slab waveguide
        slab = gdspy.Path(width)
        slab.segment(length, layer=layer[0])

        # Update self.obj with new objects
        self.obj.append(slab)
        self.obj.extend(etch)

        # Update self.port
        self.port.update({'o0': (0, 0, 0)})