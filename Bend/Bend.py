import gdspy
from scipy import optimize
from scipy import integrate
import numpy as np
pi = np.pi
from Component.Component import Component

def euler(radius: float, final_angle: float):
    """
    **radius** : Effective bend radius
    **final_angle** : 0° ~ 90°
    """

    # Parametric function of Euler curve
    x = lambda s, R0: integrate.quad(lambda t: np.cos(t**2 / (2 * R0**2)), 0, s)[0]
    y = lambda s, R0: integrate.quad(lambda t: np.sin(t**2 / (2 * R0**2)), 0, s)[0]
    dx = lambda s, R0: np.cos(s**2 / (2 * R0**2))
    dy = lambda s, R0: np.sin(s**2 / (2 * R0**2))

    # s(θ) = R0 * √(2 * θ)
    s = lambda theta, R0: R0 * np.sqrt(2 * theta)

    # ---------- Find R0 ----------
    # CONDITION 1: θ(s_max) = 45 degrees
    s_max = lambda R0: s(45 / 180 * pi, R0)
    
    # CONDITION 2: y(s_max) = -x(s_max) + radius
    f = lambda R0: x(s_max(R0), R0) + y(s_max(R0), R0) - radius
    
    # Solve R0 by Newton method around R0 = 10
    R0 = optimize.newton(f, 10)
    # -----------------------------

    s_max = s_max(R0)

    # We do not use Euler curve directly for bends.
    # We merge two Euler curves, one is 0° ~ 45° and the other is 45° ~ 0° (mirror)
    def curve_function(u):
        """
        0 ≤ u ≤ 1
        """
        
        # Decide s from final_angle
        if final_angle <= 45:

            s_ = s(final_angle / 180 * pi, R0)
            s_ = u * s_

        elif final_angle > 45:
            
            s_ = 2 * s_max - s((90 - final_angle) / 180 * pi, R0)
            s_ = u * s_

        # Decide x and y from s
        if s_ <= s_max:
            
            # 0° ~ 45° Euler curve
            x_ = x(s_, R0)
            y_ = y(s_, R0)
        
        elif s_ > s_max:
            
            # 45° ~ 0° Euler curve with mirror
            x_ = -y(2 * s_max - s_, R0) + radius
            y_ = -x(2 * s_max - s_, R0) + radius
            
        return (x_, y_)

    def curvature_function(u):
        """
        0 ≤ u ≤ 1
        """

        # Decide s from final_angle
        if final_angle <= 45:
            
            s_ = s(final_angle / 180 * pi, R0)
            s_ = u * s_

        elif final_angle > 45:
            
            s_ = 2 * s_max - s((90 - final_angle) / 180 * pi, R0)
            s_ = u * s_

        # Decide dx and dy from s
        if s_ <= s_max:
            
            # 0° ~ 45° Euler curve
            dx_ = dx(s_, R0)
            dy_ = dy(s_, R0)
        
        elif s_ > s_max:
            
            # 45° ~ 0° Euler curve with mirror
            dx_ = dy(2 * s_max - s_, R0)
            dy_ = dx(2 * s_max - s_, R0)

        return (dx_, dy_)

    return curve_function, curvature_function

class Bend(Component):
    """
    Bend with Euler curve (Adiabatic bend)\n
    **radius** : Effective bend radius\n
    **width** : Width of waveguide\n
    **final_angle** : Final turning angle 0° ~ 90°\n
    Ref: https://doi.org/10.1364/OL.476873
    """

    def __init__(self, radius: float=14, width: float=1.2, final_angle: float=90, layer: int=12) -> None:
        
        # Attributes
        self.obj = []
        self.port = {}

        # Generate gdspy object
        curve = euler(radius, final_angle)
        curve_function = curve[0]
        curvature_function = curve[1]
        
        wg = gdspy.Path(width)
        wg.parametric(curve_function,
                      curve_derivative=curvature_function,
                      tolerance=0.001,
                      layer=layer)
    
        # Update self.obj with new objects
        self.obj.append(wg)

        # Update self.port
        self.port.update({'o0': (0, 0, 0),
                          'o1': (wg.x, wg.y, final_angle)})