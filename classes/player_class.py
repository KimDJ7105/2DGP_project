from pico2d import *

class Player :
    def __init__(self) :
        self.sprite = load_image('player/2DGP.png')
        self.x = 400
        self.y = 90
        self.hp = 5
        self.atk = 0
        self.frame = 0
        self.dir = 0
        self.last_dir = 0
        self.line = 5 #sprite line
        self.jump = False

    def draw(self) :
        self.sprite.clip_draw(self.frame * 100, self.line * 100 ,100, 100, self.x, self.y)

    def move(self) :
        if self.jump == False : #not jump or in mid air
            if self.y < 90 :
                self.y = 90
            elif self.y > 90 :
                self.y -= 2
                if self.y == 90 :
                    self.set_dir(self.last_dir)
                    self.set_dir(0)
                else :
                    if self.last_dir == 1 or self.last_dir == 0 :
                        self.line = 1
                        self.frame = 0
                    elif self.last_dir == -1 :
                        self.line = 0
                        self.frame = 0
        elif self.jump == True : #jumping
            if self.y < 160 :
                self.y += 2
                if self.last_dir == 1 or self.last_dir == 0 :
                    self.line = 1
                    self.frame = 0
                elif self.last_dir == -1 :
                    self.line = 0
                    self.frame = 0
            elif self.y >= 160 :
                self.jump = False
        if self.dir == -1 and self.x > 0 or self.dir == 1 and self.x < 800: #left or right
            self.x += 2* self.dir

    def frame_update(self) :
        if self.line == 2 or self.line == 3 :
            self.frame = (self.frame + 1) % 7
        elif self.line == 4 or self.line == 5 :
            self.frame = (self.frame + 1) % 4

    def set_line(self,num) :
        self.line = num

    def set_dir(self, num) :
        self.last_dir = self.dir
        self.dir = num
        if num == 1 :
            self.set_line(3)
        elif num == -1 :
            self.set_line(2)
        elif num == 0 :
            if self.last_dir == -1 :
                self.set_line(4)
            elif self.last_dir == 1 :
                self.set_line(5)

    def set_jump(self, jump_bool) :
        self.jump = jump_bool
