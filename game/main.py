import numpy as np
import pygame as pg
import os
from game_resources import Resources

from viewer import Viewer

field = np.zeros((5,5))

res = Resources()

def main():
    X = np.zeros((1000,1000,3))
    screen = pg.surfarray.make_surface(X)
    screen.blit(res.terrian['land'], (10, 10))
    return screen

if __name__ == "__main__":
    viewer = Viewer(main, (1000,1000))
    res.load()
    viewer.start()