import matplotlib
import matplotlib.pyplot as plt
import matplotlib.projections as pro
import numpy as np
import os
import sys
import matplotlib.projections as pro
from matplotlib import rcParams
from sympy import false
import warnings
import locate_bad_images as lbi
rcParams['figure.dpi'] = 150
#warnings.filterwarnings('ignore')


def get_filename(dir, filetype):
    path, dirs, files = next(os.walk(dir))
    file_count = len(files)
    return str(file_count) + filetype

def gen(color_map, projection, bgcolor):


    
    with open("out.out", "r") as f:
        lines = f.readlines()
    
    if lines[0] == "0\n":
        print(f"[gen.py] no values, exiting")
        return False

    xline = lines[1].strip().split(" ")
    yline = lines[2].strip().split(" ")


    x = np.array([float(x) for x in xline])
    y = np.array([float(y) for y in yline])


    print(f"[gen.py] Read and converted {len(x)} points.")

    fig = plt.figure()

    fig.set_facecolor(bgcolor)
    ax = fig.add_subplot(111, projection=projection)

    colors = x

    ax.scatter(
        y,
        x,
        alpha=0.1,
        c=colors,
        s=(72./fig.dpi)**2, 
        linewidths=0,
        cmap=color_map
    )

    ax.set_axis_off()
    ax.patch.set_zorder(-1)

    print(f"[gen.py] Scatterplot finished")

    filename = get_filename("Images/", ".png")
    plt.savefig(f'Images/{filename}')
    print(filename + "----")
    if lbi.should_delete(f"Images/{filename}", 30000):
        os.remove(f"Images/{filename}")
        return False
    else:
        print(f"[gen.py] Bye:)")
    return True
if __name__ == "__main__":
    gen()
