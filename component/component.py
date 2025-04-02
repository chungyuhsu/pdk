import gdspy
import numpy as np

class Component():
    """
    Basic class for components\n
    Two essential attributions\n
    **obj** : Store all gdspy geometric objects\n
    **port** : Store all ports for connecting to other components\n
    Two methods\n
    **hold** : Move the component without putting on GDSII layout\n
    **put** : Put the component on GDSII layout
    """
    
    def __init__(self) -> None:
        # Add parameters after self if you want your design changeable.
        
        # Attributes
        self.obj = [] # store all gdspy geometric objects
        self.port = {'og': (0, 0, 0)} # (x, y, theta) theta is in degrees.
        
        # Draw your design here. Everything respects to port 'og'.
        layer = [1, 2]
        rec = gdspy.Rectangle((0, 0), (17.5, 2.5), layer=layer[0])
        text = gdspy.Text('COMPONENT', 2, (1, 0), layer=layer[1])
        
        # Update self.obj with new objects
        self.obj.append(rec)
        self.obj.append(text)

        # Update self.port
        self.port.update({'o0': (0, 1.25, 0),
                          'o1': (17.5, 1.25, 0),
                          'e0': (8.75, 0, 90),
                          'e1': (8.75, 2.5, 90)})

    def hold(self, port: str, destination: tuple, flip_port: bool=False) -> None:
        """
        This method moves the component without putting on GDSII layout.\n
        **port** : Existing port in this component\n
        **destination** : Where you want to move\n
        **flip_port** : If flip_port is True, rotate the destination direction by 180°.
        """
        # If flip_port is True, rotate the destination direction by 180°.
        # This is useful when the destination has a wrong direction.
        if flip_port == True:
            destination = (destination[0],
                           destination[1],
                           destination[2] + 180)
        
        # We operate three steps in this method.
        # STEP 1: Duplicate self.obj and replace the old one
        # STEP 2: Rotate from port to destination
        # STEP 3: Translate from port to destination
        
        # ---------- STEP 1 ----------
        new_obj = []
        for i in self.obj:
            new_obj.append(gdspy.copy(i))
        self.obj = new_obj

        # ---------- STEP 2 ----------
        # How much to rotate
        angle = destination[2] - self.port[port][2]
        angle = np.deg2rad(angle)

        # What is the reference point for rotating
        # It can be any point, I choose (0, 0, 0) for no particular reason.
        ogx = 0
        ogy = 0
        ogtheta = 0
        
        # Rotate all gdspy geometric objects respecting to the reference point
        for i in self.obj:
            i.rotate(angle, (ogx, ogy))

        # Update self.port
        new_port = {}
        for i, j in self.port.items():
            # coordinate respecting to the reference point before rotating
            x = j[0] - ogx
            y = j[1] - ogy
            theta = j[2] - ogtheta
            # coordinate after rotating by angle
            new_x = ogx + x * np.cos(angle) - y * np.sin(angle)
            new_y = ogy + x * np.sin(angle) + y * np.cos(angle)
            new_theta = ogtheta + theta + np.rad2deg(angle)
            new_port.update({i: (new_x, new_y, new_theta)})
        self.port = new_port
        
        # ---------- STEP 3 ----------
        # How much to translate
        dx = destination[0] - self.port[port][0]
        dy = destination[1] - self.port[port][1]
        
        # Translate all gdspy geometric objects
        for i in self.obj:
            i.translate(dx, dy)

        # Update self.port
        new_port = {}
        for i, j in self.port.items():
            x = j[0] + dx
            y = j[1] + dy
            new_port.update({i: (x, y, j[2])})
        self.port = new_port

    def put(self, port: str, destination: tuple, flip_port: bool=False) -> None:
        """
        This method moves and puts the component on GDSII layout.\n
        **port** : Existing port in this component\n
        **destination** : Where you want to put\n
        **flip_port** : If flip_port is True, rotate the destination direction by 180°.
        """
        # Continue from method hold and add two more steps.
        # STEP 4: Generate labels for ports
        # STEP 5: Add self.obj and label to 'cell'

        # ---------- STEP 1 ~ 3 ----------
        self.hold(port, destination, flip_port=flip_port)
        
        # ---------- STEP 4 ----------
        label = []
        for i, j in self.port.items():
            label.append(gdspy.Label(i, (j[0], j[1])))

        # ---------- STEP 5 ----------
        # If 'cell' exists, add obj and label to 'cell'.
        # Otherwise, create a new cell named 'cell'.
        cell_name = 'cell'
        if cell_name in gdspy.current_library.cells:
            cell = gdspy.current_library.cells[cell_name]
        else:
            cell = gdspy.Cell(cell_name)
        
        cell.add(self.obj)
        cell.add(label)