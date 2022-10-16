from pico2d import *

class Player :
    def __init__(self) :
        self.sprite = load_image('player/2DGP.png')
        self.heart = load_image('player/heart.png')
        self.stamina_bar = load_image('player/stamina_bar.png')
        self.x = 400
        self.y = 90
        self.hp = 5
        self.atk = 0
        self.frame = 0
        self.dir = 0
        self.last_dir = 0
        self.line = 5 #sprite line
        self.jump = False
        self.roll = False
        self.roll_count = 0
        self.stamina = 100

    def draw(self) :
        self.sprite.clip_draw(self.frame * 100, self.line * 100 ,100, 100, self.x, self.y)
        self.draw_heart()
        self.draw_stamina()

    def draw_heart(self) :
        tem_x = 50
        tem_y = 550
        for i in range(0,self.hp) :
            self.heart.draw(tem_x,tem_y,50,50)
            tem_x += 60

    def draw_stamina(self) :
        self.stamina_bar.draw(400,550,self.stamina,25)

    def regen_stamina(self) :
        if self.stamina < 100 :
            self.stamina += 1
        if self.stamina > 100 :
            self.stamina = 100

    def move(self) :
        if self.roll == True :
            if self.last_dir == 0 or self.last_dir == 1 :
                if self.x < 800 and self.roll_count == 10:
                    self.x += 30
            elif self.last_dir == -1 :
                if self.x > 0 and self.roll_count == 10 :
                    self.x -= 30
            if self.frame == 3 :
                self.roll = False
                self.set_dir(self.last_dir)
                self.set_dir(0)
        elif self.roll == False :
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
        elif self.line == 4 or self.line == 5 and self.roll == False:
            self.frame = (self.frame + 1) % 4
        elif self.roll == True :
            self.roll_count += 1
            if self.roll_count == 11 :
                self.frame += 1
                self.roll_count = 0

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
        if self.roll == False and self.y == 90:
            self.jump = jump_bool

    def set_roll(self, roll_bool) :
        if self.roll == False and self.stamina > 30:
            self.roll = roll_bool
            self.stamina -= 30
            self.frame = 1
            if self.last_dir == 0 or self.last_dir == 1:
                self.line = 1
            elif self.last_dir == -1 :
                self.line = 0