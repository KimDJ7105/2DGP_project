from pico2d import *

class Map :
    def __init__(self) :
        self.land = load_image('map/grass.png')
        self.background = load_image('map/town.png')
        self.map_type = 0

    def draw(self) :
        self.background.draw(400,300,800,600)
        self.land.draw(400,30)

    def set_map_type(self,num) :
        self.map_type = num

    def set_image(self) :
        if self.map_type == 0 : #town
            self.land = load_image('map/grass.png')
            self.background = load_image('map/town.png')
        elif self.map_type == 1 : #snowland
            self.land = load_image('map/grass.png')
            self.background = load_image('map/snowland.png')
        elif self.map_type == 2 : #desert
            self.land = load_image('map/grass.png')
            self.background = load_image('map/desert.png')
        elif self.map_type == 3 : #volcano
            self.land = load_image('map/grass.png')
            self.background = load_image('map/volcano.png')