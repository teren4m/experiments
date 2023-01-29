import pygame as pg
import game_files as gf

class Resources:

    def __init__(self) -> None:
        self.terrian = {}

    def load_terrian(self):
        for key in gf.terrian.keys():
            self.terrian[key] = pg.image.load(gf.terrian[key])

    def load(self):
        self.load_terrian()
