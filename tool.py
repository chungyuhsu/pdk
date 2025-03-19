"""
Some useful tools for drawing your design
"""

def ruler(port1: tuple, port2: tuple) -> tuple:
    """Return the difference between **port1** and **port2**."""
    dx = port2[0] - port1[0]
    dy = port2[1] - port1[1]
    dtheta = port2[2] - port1[2]
    return (dx, dy, dtheta)

def add(port1: tuple, port2: tuple) -> tuple:
    """Return the summation of **port1** and **port2**."""
    x = port1[0] + port2[0]
    y = port1[1] + port2[1]
    theta = port1[2] + port2[2]
    return (x, y, theta)