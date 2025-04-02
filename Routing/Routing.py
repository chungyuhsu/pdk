from Component.Component import Component
from Bend.Bend import Bend
from Waveguide.Waveguide import Waveguide
import tool

class Routing(Component):
    """
    Waveguide routing\n
    **path** : Control the route. For example: path = [10, 'l', 'r', 20] means go straight for 10 μm, then turn left and turn right, then keep going for 20 μm.\n
    **bend_radius** : Bend radius used in the route
    **wg_width** : Width of the route
    **layer** :  Layer of the route
    """
    
    def __init__(self, path: list, bend_radius: float=14, wg_width: float=1.2, layer: int = 12) -> None:
        
        # Attributes
        self.obj = []
        self.port = {}

        # Draw your design here.
        # combine numbers which is not separated by a letter
        path.insert(0, 'dummy')
        path.append('dummy')

        li = [] # letter index
        for i in range(len(path)):
            if isinstance(path[i], str):
                li.append(i)

        new = []
        for i in range(len(li)-1):
            new.append(path[li[i]])
            
            summ = 0 # summ = summation
            for j in range(li[i]+1, li[i+1]):
                summ = summ + path[j]
            summ = abs(summ)
            
            if summ != 0:
                new.append(summ)

        new.pop(0)
        
        # path must be start and end with a number
        if isinstance(new[0], str):
            new.insert(0, 0)
        
        if isinstance(new[-1], str):
            new.append(0)
        
        path = new
        
        # start of the path
        end = (0, 0, 0)
        
        # segments #1 ~ #N (total is N)
        for i in range(len(path)): # exclude first and last one
            
            if path[i] == 'l':
                
                wg = Bend(radius=bend_radius, width=wg_width, layer=layer)
                wg.hold('o0', end)
                self.obj.extend(wg.obj)
                end = wg.port['o1']

            elif path[i] == 'r':
                
                wg = Bend(radius=bend_radius, width=wg_width, layer=layer)
                wg.hold('o1', tool.add(end, (0, 0, 180)))
                self.obj.extend(wg.obj)
                end = tool.add(wg.port['o0'], (0, 0, 180))
            
            elif isinstance(path[i], (int, float)):
                
                wg = Waveguide(wg_width, path[i], layer=layer)
                wg.hold('o0', end)
                if wg.length != 0:
                    self.obj.extend(wg.obj)
                end = wg.port['o1']

        # Update self.port
        self.port.update({'o0': (0, 0, 0),
                          'o1': end})