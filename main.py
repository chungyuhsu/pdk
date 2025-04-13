import gdspy
from AlignEBL.AlignEBL import AlignEBL

align = AlignEBL()
align.put('og', (0, 0, 0))

gdspy.write_gds('AlignEBL.gds')