import pygame as pg
import game_files as gf
import imageio

class Resources:

    def __init__(self) -> None:
        self.terrian = {}

    def load_terrian(self):
        for key in gf.terrian.keys():
            self.terrian[key] = imageio.imread(gf.terrian[key])

    def load(self):
        self.load_terrian()

    def __getattr__(self, attr):
        return self.terrian[attr].copy()
