import numpy as np

cos = lambda th : np.cos(np.deg2rad(th))
sin = lambda th : np.sin(np.deg2rad(th))

Rx = lambda th : np.array([
    [1, 0,       0],
    [0, cos(th), -sin(th)],
    [0, sin(th), cos(th)]])

Ry = lambda th : np.array([
    [cos(th),  0, sin(th)],
    [0      ,  1, 0],
    [-sin(th), 0, cos(th)]
])

Rz = lambda th : np.array([
    [cos(th) , sin(th), 0],
    [-sin(th), cos(th), 0],
    [0       , 0,       1]])

