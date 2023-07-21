import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import imageio
from initial_demo import Rx, Ry, Rz
from rotation import Reshape

def saveGif(X,Y,Z, gifs, th):
    plt.cla()
    ax = plt.subplot(projection='3d')
    filled = np.ones((1,1,1))
    ax.voxels(*Reshape(X, Y, Z), filled=filled)
    ax.set_xlim(-0.5,1.5)
    ax.set_ylim(-0.5,1.5)
    ax.set_zlim(-0.5,1.5)
    ax.set_title(f"theta={th}")
    plt.tight_layout()
    plt.savefig(f"tmp.jpg")
    gifs.append(imageio.imread(f"tmp.jpg"))

def spinning():
    x, y, z = np.indices((2, 2, 2))
    xyz = np.array([x,y,z]).reshape(3,-1)
    gifImgs = []
    th = 0
    for i in range(30):
        X,Y,Z = Rx(th)@xyz
        th += 3
        saveGif(X, Y, Z, gifImgs, th)
    imageio.mimsave("test.gif",gifImgs,duraion=100)

if __name__ == "__main__":
    spinning()

