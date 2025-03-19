import gdspy
from component import Component
from mmi1x2 import Mmi1x2

if __name__ == "__main__":
    cell = gdspy.Cell('cell')
    
    mmi = Mmi1x2(50, 80)
    wg = Component()
    mmi.put('pout', wg.port['pin'])

    cell.add(mmi.obj)
    cell.add(wg.obj)
    
    gdspy.write_gds('mmi1x2.gds')