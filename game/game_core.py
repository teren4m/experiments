import numpy as np

tile_position = 0


def map_field(field, f):
    x_size, y_size, _ = field.shape
    for x in range(x_size):
        for y in range(y_size):
            f(x, y, field)


def get_randome_tile():
    return np.random.randint(3, size=1)[0]


def add_tile(x: int, y: int, field: np.ndarray):
    field[x][y][tile_position] = get_randome_tile()


class Core:
    def __init__(self) -> None:
        self.field = np.zeros((5, 5, 2))
        self.sea = 0
        self.land = 1
        self.mountain = 2

    def generate_map(self):
        map_field(self.field, add_tile)
