import gdspy
from Component.Component import Component

class Template(Component):
    """
    SNG template\n
    Chip size is 25 mm × 25 mm\n
    Safe zone is 15 mm × 15 mm at the chip center\n
    Each field is 500 µm × 500 µm
    """
    
    def __init__(self) -> None:
        
        # Attributes
        self.obj = []
        self.port = {'og': (0, 0, 0)}

        # Draw your design here.
        # chip
        pt1 = (0, 0)
        pt2 = (25000, 25000)
        chip = gdspy.Rectangle(pt1, pt2, datatype=1)
        self.obj.append(chip)

        # fields
        for i in range(30):
            for j in range(30):
                pt1 = (5000 + 500*i, 5000 + 500*j)
                pt2 = (pt1[0] + 500, pt1[1] + 500)
                field = gdspy.Rectangle(pt1, pt2, datatype=2)
                self.obj.append(field)