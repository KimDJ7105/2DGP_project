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
        self.role = False
        self.role_count = 0

    def draw(self) :
        self.sprite.clip_draw(self.frame * 100, self.line * 100 ,100, 100, self.x, self.y)

    def move(self) :
        if self.role == True :
            if self.last_dir == 0 or self.last_dir == 1 :
                if self.x < 800 and self.role_count == 10:
                    self.x += 30
            elif self.last_dir == -1 :
                if self.x > 0 and self.role_count == 10 :
                    self.x -= 30
            if self.frame == 3 :
                self.role = False
                self.set_dir(self.last_dir)
                self.set_dir(0)
        elif self.role == False :
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
        elif self.line == 4 or self.line == 5 and self.role == False:
            self.frame = (self.frame + 1) % 4
        elif self.role == True :
            self.role_count += 1
            if self.role_count == 11 :
                self.frame += 1
                self.role_count = 0

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
        if self.role == False and self.y == 90:
            self.jump = jump_bool

    def set_role(self, role_bool) :
        if self.role == False :
            self.role = role_bool
            self.frame = 1
            if self.last_dir == 0 or self.last_dir == 1:
                self.line = 1
            elif self.last_dir == -1 :
                self.line = 0