import os

data = 'data'
land = 'land.png'
mountain = 'mountain.png'
sea = 'sea.png'

terrian = {
    'land': os.path.join('game', data, land),
    'mountain': os.path.join('game', data, mountain),
    'sea': os.path.join('game', data, sea),
}
