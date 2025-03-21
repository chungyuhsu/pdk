import gdspy
from .component import Component

class Metalens(Component):
    """
    Focal length: 200 µm
    Ref: https://doi.org/10.1364/CLEO_SI.2024.SW4O.5
    """
    
    def __init__(self) -> None:
        
        # Attributes
        self.obj = []
        self.port = {'og': (0, 0, 0)}
        self.layer = [10]

        # Draw your design here. Everything respects to port 'og'.
        with open('metalens_data.txt', "r", encoding="utf-8") as file:
            for line in file:
                print(line.strip())  # Removes newline characters

        
        # Update self.obj with new objects
        self.obj.extend([])

        # Update self.port
        self.port.update({'o0': (0, 100, 0),
                          'o1': (3, 100, 0)})

if __name__ == "__main__":
    
    Metalens().put('og', (0, 0, 0))
    
    gdspy.write_gds('metalens.gds')