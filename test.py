# Import every components you need
import gdspy
from MMI1X2.MMI1X2 import MMI1X2
from Routing.Routing import Routing
from FGC.FGC import FGC
from Waveguide.Waveguide import Waveguide

# Draw an input GC.
gc = FGC()
gc.put('o0', (0, 0, 0))

# Draw a taper because of the waveguide width difference.
taper = Waveguide(2.1, 20, 1.2)
taper.put('o0', gc.port['o0'], flip_port=True)
# Sometimes, you need to connect two ports that have opposite directions.
# Enabling flip_port can make your life easier.

# Draw an U turn because the coupling angle of the GC is minus.
turn = Routing(path=['l', 'l', 100])
turn.put('o0', taper.port['o1'])

# Draw the first MMI.
mmi = MMI1X2()
mmi.put('o0', turn.port['o1'])

# Draw the lower arm of MZI.
wg1 = Routing(path=['r', 'l', 100, 'l', 'r'])
wg1.put('o0', mmi.port['o1'])

# Draw the upper arm of MZI.
wg2 = Routing(path=['l', 'r', 100, 'r', 'l'])
wg2.put('o0', mmi.port['o2'])

# Draw the second MMI.
# Because two MMIs are the same, we do not need to create another one.
mmi.put('o1', wg2.port['o1'], flip_port=True)

# Draw another U turn.
turn = Routing(path=[100, 'l', 'l'])
turn.put('o0', mmi.port['o0'], flip_port=True)

# Draw another taper.
taper = Waveguide(1.2, 20, 2.1)
taper.put('o0', turn.port['o1'])

# Draw an output GC.
gc.put('o0', taper.port['o1'])

# Generate the GDSII layout.
gdspy.write_gds('test.gds')