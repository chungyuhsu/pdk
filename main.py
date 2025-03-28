import gdspy
from Gc_fully.Gc_fully import Gc_fully

Gc_fully().put('og', (0, 0, 0))
gdspy.write_gds('Gc_fully.gds')