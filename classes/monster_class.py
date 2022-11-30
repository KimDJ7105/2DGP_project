from pico2d import *
from parameter.boss_parameter import *
import game_framework
from random import randint
import states.game_world as game_world

RU, AT, KIA = range(3)

class mRUN :
    @staticmethod
    def enter(self,player) :
        pass

    @staticmethod
    def exit(self) :
        pass

    @staticmethod
    def do(self,player) :
        self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME* game_framework.frame_time) % 5
        if self.dir == 1 and self.x < 2000 or self.dir == -1 and self.x > 0 :
            self.x += self.dir * self.speed * game_framework.frame_time
        if abs(player.x - self.x)  < 15 :
            self.get_event(AT)
        pass

    def draw(self, x) :
        self.draw(x)

class mATTACK :
    @staticmethod
    def enter(self,player) :
        pass

    @staticmethod
    def exit(self) :
        pass

    @staticmethod
    def do(self,player) :
        if player.attack_able() == True :
            self.get_event(KIA)
        else :
            self.get_event(RU)
        pass

    def draw(self, x) :
        self.draw(x)

class mDEAD :
    @staticmethod
    def enter(self,player) :
        if self.hp > 0 :
            player.get_damage(1, self)
        pass

    @staticmethod
    def exit(self) :
        pass

    @staticmethod
    def do(self,player) :
        game_world.remove_object(self)
        pass

    def draw(self, x) :
        self.draw(x)

mNext_state = {
    mRUN : { RU : mRUN, AT : mATTACK, KIA : mDEAD},
    mATTACK : { RU : mRUN, AT : mATTACK, KIA : mDEAD},
    mDEAD : {RU : mDEAD, AT : mDEAD, KIA : mDEAD} 
}

class Monster :
    def __init__ (self, _x, _y, name, _speed, _hp, _w,_h) :
        self.sprite = load_image(name)
        self.hp = _hp
        self.atk_count = 0
        self.x = _x
        self.y = _y
        self.speed = _speed
        self.wide = _w
        self.hight = _h
        self.frame = 0
        if self.x == 2000 :
            self.dir = -1
        elif self.x == 0 :
            self.dir = 1
        self.q = []
        self.cur_state = mRUN

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
        if x > 400 and x < 1600 :
            if self.x > x - (400 + self.wide // 2) and self.x < x + (400 + self.wide // 2) :
                if self.x > x :
                    self.sprite.clip_composite_draw(int(self.frame)* 150,0,self.wide,self.hight,0,'',400 - (x - self.x), self.y,150,150)
                    self.dir = -1
                elif self.x <= x :
                    self.sprite.clip_composite_draw(int(self.frame) * 150,0,self.wide,self.hight,0,'h',400 + (self.x -x), self.y,150,150)
                    self.dir = 1
        elif x <= 400:
            if self.x > 0 and self.x < 800 :
                if self.x > x :
                    self.sprite.clip_composite_draw(int(self.frame) * 150,0,self.wide,self.hight,0,'',self.x, self.y,150,150)
                    self.dir = -1
                elif self.x <= x :
                    self.sprite.clip_composite_draw(int(self.frame) * 150,0,self.wide,self.hight,0,'h',self.x, self.y,150,150)
                    self.dir = 1
        elif x >= 1600 :
            if self.x > 1200 and self.x < 2000 :
                if self.x > x :
                    self.sprite.clip_composite_draw(int(self.frame) * 150,0,self.wide,self.hight,0,'',400 - (1600 - self.x), self.y,150,150)
                    self.dir = -1
                elif self.x <= x :
                    self.sprite.clip_composite_draw(int(self.frame) * 150,0,self.wide,self.hight,0,'h',400 + (self.x - 1600), self.y,150,150)
                    self.dir = 1
        pass

    def get_event(self, event) :
        self.q.append(event)

    def update(self,player) :
        self.cur_state.do(self, player)

        if self.q :
            event = self.q.pop()
            if mNext_state[self.cur_state][event] != self.cur_state :
                self.cur_state.exit(self)
                self.cur_state = mNext_state[self.cur_state][event]
                self.cur_state.enter(self,player)