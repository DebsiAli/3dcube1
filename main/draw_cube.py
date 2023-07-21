import matplotlib.pyplot as plt
import numpy as np

def draw_cube():
    x, y, z = np.indices((2, 2, 2))
    filled = np.ones((1,1,1))
    ax = plt.subplot(projection='3d')
    ax.voxels(x,y,z, filled=filled)
    plt.show()

if __name__ == "__main__":
    draw_cube()
