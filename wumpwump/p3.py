import math

""" This program compute the volumne and surface area of a cylinder """
def compute_volume(r,h):
    if r<=0 or h<=0:
        raise ValueError
    return math.pi*r**2*h


def compute_surface_area(r,h):
    if r<=0 or h<=0:
        raise ValueError
    return (2*math.pi*r**2)+(2*math.pi*r*h)
