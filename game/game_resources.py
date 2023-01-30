import pygame as pg
import game_files as gf
import imageio
import glob

for im_path in glob.glob("path/to/folder/*.png"):
     im = imageio.imread(im_path)
     print(im.shape)

class Resources:

    def __init__(self) -> None:
        self.terrian = {}

    def load_terrian(self):
        for key in gf.terrian.keys():
            self.terrian[key] = pg.image.load(gf.terrian[key])

    def load(self):
        self.load_terrian()

    def __getattr__(self, attr):
        return self.terrian[attr].copy()
