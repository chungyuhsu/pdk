import gdspy
from component.component import Component

Component().put('og', (0, 0, 0))
gdspy.write_gds('component.gds')