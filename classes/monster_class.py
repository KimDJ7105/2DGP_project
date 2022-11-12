from pico2d import *
import classes.player_class as cat
from parameter.boss_parameter import *
import game_framework
from random import randint

ID, RU, AT = range(3)

class mIDLE :
    @staticmethod
    def enter(self) :
        print('boss enter idle')
        self.timer = 0
        pass

    @staticmethod
    def exit(self) :
        pass

    @staticmethod
    def do() :
        pass

    def draw(self, x) :
        self.draw(x)

class mRUN :
    @staticmethod
    def enter(self) :
        print('boss enter run')
        self.timer = 0
        pass

    @staticmethod
    def exit(self) :
        pass

    @staticmethod
    def do() :
        pass

    def draw(self, x) :
        self.draw(x)

class mATTACK :
    @staticmethod
    def enter(self) :
        print('boss enter attack')
        self.timer = 0
        pass

    @staticmethod
    def exit(self) :
        pass

    @staticmethod
    def do() :
        pass

    def draw(self, x) :
        self.draw(x)

mNext_state = {
    mIDLE : {ID : mIDLE, RU : mRUN, AT : mATTACK},
    mRUN : {ID : mIDLE, RU : mRUN, AT : mATTACK},
    mATTACK : {ID : mIDLE, RU : mRUN, AT : mATTACK},
}

class Monster :
    def __init__ (self) :
        self.sprite = load_image('boss/temp.png')
        self.hp = 100
        self.atk_count = 0
        self.x = 1400
        self.y = 120
        self.wide = 482
        self.hight = 146
        self.q = []
        self.cur_state = mIDLE

    def get_distance(self, player) :
        pass

    def attack_far(self) :
        pass

    def attack_close(self) :
        pass

    def attack_mid(self) :
        pass

    def deliver_damage(self,start, end, y, player) :
        if player.x >= start and player.x <= end and player.y <= y :
            player.get_damage()

    def get_damage(self, damage):
        self.hp -= damage
        print(f'get {damage} damage, remain HP {self.hp}')

    def draw(self, x) :
        if self.x > x - 641 and self.x < x + 641 :
            if self.x > x :
                self.sprite.clip_composite_draw(0,0,self.wide,self.hight,0,'',400 - (x - self.x), self.y)
            elif self.x <= x :
                self.sprite.clip_composite_draw(0,0,self.wide,self.hight,0,'h',400 + (self.x -x), self.y)
        pass

    def update(self) :
        self.cur_state.do(self)

        if self.q :
            event = self.q.pop()
            if mNext_state[self.cur_state][event] != self.cur_state :
                self.cur_state.exit(self)
                self.cur_state = mNext_state[self.cur_state][event]
                self.cur_state.enter(self)