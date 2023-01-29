import numpy as np
import pygame as pg
import os

from viewer import Viewer

field = np.zeros((5,5))

data = 'data'
land = 'land.png'
mountain = 'mountain.png'
sea = 'sea.pmg'

get_land_path = os.path.join('game', data, land)



def main():
    X = np.zeros((1000,1000,3))
    return pg.surfarray.make_surface(X)

if __name__ == "__main__":
    viewer = Viewer(main, (1000,1000))
    viewer.start()