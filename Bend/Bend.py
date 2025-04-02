import gdspy
from scipy import optimize
from scipy import integrate
import numpy as np
pi = np.pi
from Component.Component import Component

class Bend(Component):
    """
    Bend with Euler curve (Adiabatic bend)\n
    **radius** : Effective bend radius\n
    **width** : Width of waveguide\n
    Ref:\n
    https://doi.org/10.1364/OL.476873\n
    https://doi.org/10.1364/OE.25.009150
    """
    
    def __init__(self, radius: float=14, width: float=1.2, layer: int=12) -> None:
        
        # Attributes
        self.obj = []
        self.port = {}
        
        # Draw your design here.
        # find Lmax and A
        x = lambda L, A: -A*integrate.quad(lambda theta: np.sin(theta**2/2), 0, L/A)[0] + radius
        y = lambda L, A:  A*integrate.quad(lambda theta: np.cos(theta**2/2), 0, L/A)[0]
        Lmax = lambda A: A*np.sqrt(pi/2) # constrain of ending at slope=-1
        f = lambda A: x(Lmax(A), A) - y(Lmax(A), A) # constrain of ending at 45 degrees
        A = optimize.newton(f, 10)
        Lmax = Lmax(A)
        
        self.length = 2*Lmax

        # parametric functions of Euler curve
        def curve(u):
            x = lambda L, A: -A*integrate.quad(lambda theta: np.sin(theta**2/2), 0, L/A)[0]
            y = lambda L, A:  A*integrate.quad(lambda theta: np.cos(theta**2/2), 0, L/A)[0]
            L = Lmax*u
            x = x(L, A)
            y = y(L, A)
            return (y, -x)

        # generate curve1 points
        number_of_pts = 100
        curve1 = []
        for i in range(number_of_pts):
            x = curve(i/(number_of_pts-1))[0]
            y = curve(i/(number_of_pts-1))[1]
            curve1.append((x, y))

        # generate curve2 points
        curve2 = []
        for i in curve1:
            x = -i[1] + radius
            y = -i[0] + radius
            curve2.append((x, y))
        
        # merge curve1 and curve2 to ensure continuity.
        curve2.pop(-1)
        curve2.reverse()
        curve_all = curve1 + curve2
        
        # generate gdspy object
        wg3 = gdspy.FlexPath(curve_all, width, gdsii_path=True, layer=layer)
        
        # Update self.obj with new objects
        self.obj.append(wg3)

        # Update self.port
        self.port.update({'o0': (0, 0, 0),
                          'o1': (radius, radius, 90)})