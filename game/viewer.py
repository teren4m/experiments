import pygame as pg

class Viewer:
    def __init__(self, update_func, display_size):
        self.update_func = update_func
        pg.init()
        self.display = pg.display.set_mode(display_size)
    
    def set_title(self, title):
        pg.display.set_caption(title)
    
    def start(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

            X = self.update_func()
            self.display.blit(X, (0, 0))

            pg.display.update()

        pg.quit()