"""
Some useful tools for drawing your design
"""
import numpy as np
pi = np.pi

def ruler(port1: tuple, port2: tuple) -> tuple:
    """
    Return the difference between **port1** and **port2**.
    """
    
    dx = port2[0] - port1[0]
    dy = port2[1] - port1[1]
    dtheta = port2[2] - port1[2]
    return (dx, dy, dtheta)

def add(port1: tuple, port2: tuple) -> tuple:
    """
    Return the summation of **port1** and **port2**.
    """
    
    x = port1[0] + port2[0]
    y = port1[1] + port2[1]
    theta = port1[2] + port2[2]
    return (x, y, theta)

def direction2degree(direction):
    """
    Convert gdspy direction to degree
    """

    if isinstance(direction, str):
        
        if direction == '+x': return 0
        elif direction == '-x': return 180
        elif direction =='+y': return 90
        elif direction == '-y': return 270
    
    elif isinstance(direction, (int, float)):

        return direction/pi*180
    
    else:

        print('ERROR: direction needs to be a gdspy direction!')