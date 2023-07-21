import matplotlib.pyplot as plt
import numpy as np
from initial_demo import Rx, Ry, Rz

Reshape = lambda x,y,z : [x.reshape(2,2,2), y.reshape(2,2,2), z.reshape(2,2,2)]

def rotation():
    filled = np.ones((1,1,1))
    x, y, z = np.indices((2, 2, 2))
    xyz = np.array([x,y,z]).reshape(3,-1)
    fig = plt.figure("rotate")
    ax = fig.add_subplot(1,4,1, projection='3d')
    ax.voxels(x,y,z, filled=filled)
    X, Y, Z = Rx(30) @ xyz
    ax = fig.add_subplot(1,4,2, projection='3d')
    ax.voxels(*Reshape(X, Y, Z), filled=filled)
    X, Y, Z = Ry(30) @ xyz
    ax = fig.add_subplot(1,4,3, projection='3d')
    ax.voxels(*Reshape(X, Y, Z), filled=filled)
    X, Y, Z = Rz(30) @ xyz
    ax = fig.add_subplot(1,4,4, projection='3d')
    ax.voxels(*Reshape(X, Y, Z), filled=filled)
    plt.show()

if __name__ == "__main__":
    rotation()

