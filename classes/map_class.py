from pico2d import *

class Map :
    def __init__(self) :
        self.land = load_image('map/grass.png')
        self.background = load_image('map/town.png')
        self.map_type = 0
        self.map_x = 0

    def draw(self) :
        self.background.draw(400,300,800,600)
        self.land.draw(400,30)

    def draw_wide(self) :
        if self.map_type == 0 :
            self.background.draw(400,300,800,600)
            self.land.clip_draw(self.map_x,0,800,200,400,100)
        else :
            self.background.draw(400,300,800,600)
            self.land.clip_draw(self.map_x,0,800,60,400,30)

    def map_move(self, x) :
        # if dir == -1 and self.map_x > 0 or dir == 1 and self.map_x < 1600:
        #     self.map_x += 2 * dir
        if x < 400 :
            self.map_x = 0
        elif x >= 400 and x < 1600 :
            self.map_x = x
        elif x>= 1600 :
            self.map_x = 1600

    def set_map_type(self,num) :
        self.map_type = num
        self.set_image()

    def set_image(self) :
        if self.map_type == 0 : #town
            self.land = load_image('map/town_land.png')
            self.background = load_image('map/town.png')
        elif self.map_type == 1 : #snowland
            self.land = load_image('map/snowland_land.png')
            self.background = load_image('map/snowland.png')
        elif self.map_type == 2 : #desert
            self.land = load_image('map/desert_land.png')
            self.background = load_image('map/desert.png')
        elif self.map_type == 3 : #volcano
            self.land = load_image('map/volcano_land.png')
            self.background = load_image('map/volcano.png')