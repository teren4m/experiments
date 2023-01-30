import pygame as pg
import numpy as np
from game_resources import Resources
from game_core import Core
import game_core as gc

from viewer import Viewer

res = Resources()
core = Core()

def draw_screen_tile(screen):
    def draw_tile(x: int, y: int, field: np.ndarray):
        tile = field[x][y][gc.tile_position]
        screen.blit(res.land, (0, 0))
    return draw_tile

def draw_field(screen: pg.Surface):
    gc.map_field(core.field, draw_screen_tile(screen))
    return screen

def main():
    core.field
    X = np.zeros((1000,1000,3))
    screen = pg.surfarray.make_surface(X)
    screen = draw_field(screen)
    return screen

if __name__ == "__main__":
    core.generate_map()
    print(core.field)
    viewer = Viewer(main, (1000,1000))
    res.load()
    viewer.start()