import gdspy
import numpy as np
pi = np.pi
from Component.Component import Component

def polar2cartesianX(r, phi, a):
    # convert polar to Cartesian
    return r * np.cos(phi) - r * (1 - a**2)**0.5

def polar2cartesianY(r, phi, a):
    # convert polar to Cartesian
    return a * r * np.sin(phi)

def unitCell(og, shift=False, r=10, phi=pi/6,
             dr=0.65, dphi=pi/6, a=0.97):
    """
    **og** : Original point\n
    **shift** : If True, shift the cell for half period in φ-direction.\n
    **r** : How far is the cell from original point (**og**).
    """
    
    # shift the unit cell by half period in phi-direction
    if shift == False:
        vtx_polar1 = [
        (r         , phi - dphi / 2),
        (r + dr / 2, phi - dphi / 2),
        (r         , phi           ),
        ]
        
        vtx_polar2 = [
        (r + dr / 2, phi - dphi / 2),
        (r + dr    , phi - dphi / 2),
        (r + dr    , phi           )
        ]
        
        vtx_polar3 = [
        (r + dr / 2, phi + dphi / 2),
        (r + dr    , phi           ),
        (r + dr    , phi + dphi / 2)
        ]
        
        vtx_polar4 = [
        (r         , phi           ),
        (r + dr / 2, phi + dphi / 2),
        (r         , phi + dphi / 2)
        ]
        
        vtx_polar_set = [vtx_polar1, vtx_polar2, vtx_polar3, vtx_polar4]
        
    else: # shift == True
        vtx_polar1 = [
        (r         , phi - dphi / 2),
        (r + dr / 2, phi           ),
        (r         , phi + dphi / 2),
        (r         , phi           )
        ]
        
        vtx_polar2 = [
        (r + dr    , phi - dphi/2),
        (r + dr    , phi         ),
        (r + dr    , phi + dphi/2),
        (r + dr / 2, phi         )
        ]
        
        vtx_polar_set = [vtx_polar1, vtx_polar2]

    # convert Polar to Cartesian for all points
    vtx_cartesian_set = []
    for i in vtx_polar_set:
        vtx_cartesian = []
        for j in i:
            x = og[0] + polar2cartesianX(j[0], j[1], a)
            y = og[1] + polar2cartesianY(j[0], j[1], a)
            vtx_cartesian.append((x, y))
        vtx_cartesian_set.append(vtx_cartesian)
    
    return vtx_cartesian_set # [vtx for gdspy object1, vtx for gdspy object2,...]

class Gc_fully(Component):
    """
    Fully etched broadband focusing grating coupler (FGC)\n
    **xperiod** : The period of the first unit cell in x-direction\n
    **yperiod** : The period of the first unit cell in y-direction\n
    **a** : Equal to minor axis/major axis, indicating the curve\n
    **radius** : The distance of the first period in r-direction\n
    **W_wg** : The width of the waveguide at the input\n
    **L_grating** : The length of the grating structure\n
    **W_grating** : The width of the device\n
    """
    
    def __init__(self,
                 xperiod: float = 0.65,
                 yperiod: float = 0.4,
                 a: float = 0.97,
                 radius: float = 40,
                 W_wg: float = 2.1,
                 L_grating: float = 20,
                 W_grating: float = 25,
                 layer: int = 11) -> None:
        
        # Attributes
        self.obj = []
        self.port = {'og': (0, 0, 0)}

        # Draw your design here. Everything respects to port 'og'.

        # abbreviation
        xp = xperiod
        yp = yperiod
        R = radius
        Wwg = W_wg
        Lgra = L_grating
        Wgra = W_grating

        # because of the distortion when a is not one,
        # we need to compensate the values before transforming
        R = R / (1 - (1 - a**2)**0.5)
        dr = xp / (1 - (1 - a**2)**0.5)
        Lgra = Lgra / (1 - (1 - a**2)**0.5)
        Wgra = Wgra / a
        dphi = yp / a / R
        
        # each r has difference maximum phi
        phimax = lambda Wgra, r, a: np.arcsin(Wgra / 2 / a / r)
        Ndphi = lambda r, dphi, a, Wgra: 2 * round(phimax(Wgra, r, a) / dphi) - 1
        
        # calculate number of periods in r-direction
        Ndr = round(Lgra / dr)
        Lgra = Ndr * dr
        
        # 1um WG at the input
        wg = gdspy.Path(Wwg, initial_point=(-1, 0))
        wg.segment(1, layer=layer)
        self.obj.append(wg)
        
        # slab in front of the grating
        vtx = []
        
        # left border
        x = 0
        y = Wwg/2
        vtx.append((x, y))
        
        x = 0
        y = -Wwg/2
        vtx.append((x, y))
        
        # curve at R
        start = -(Ndphi(R, dphi, a, Wgra) - 1)
        end = (Ndphi(R, dphi, a, Wgra) - 1)
        
        for i in range(start, end + 1):
            x = polar2cartesianX(R, dphi / 2 * i, a)
            y = polar2cartesianY(R, dphi / 2 * i, a)
            vtx.append((x, y))
            
        self.obj.append(gdspy.Polygon(vtx, layer=layer))
        
        # grating structure
        for i in range(Ndr):
            r = R + dr * i
            start = int(-(Ndphi(r, dphi, a, Wgra) - 1) / 2)
            end = int((Ndphi(r, dphi, a, Wgra) - 1) / 2)
            
            for j in range(start, end + 1):
                phi = dphi * j
                
                if i % 2 == 0: # even
                    shift = False
                elif i % 2 == 1: # odd
                    shift = True
                    
                unit = unitCell(og=(0, 0), shift=shift, r=r,
                phi=phi, dr=dr, dphi=dphi, a=a)
                
                for k in unit:
                    self.obj.append(gdspy.Polygon(k, layer=layer))
        
        # Update self.port
        self.port.update({'o0': (-1, 0, 0)})