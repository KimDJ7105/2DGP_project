from pico2d import *
from parameter.boss_parameter import *
import game_framework
from random import randint 
import states.game_world as game_world
import states.stage_clear_state as stage_clear

RU, AT, KIA = range(3)

class mRUN :
    timer = 0

    @staticmethod
    def enter(self,player) :
        self.sprite = self.move_s
        mRUN.timer = get_time()
        pass

    @staticmethod
    def exit(self) :
        pass

    @staticmethod
    def do(self,player) :
        self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME* game_framework.frame_time) % 6
        if self.dir == 1 and self.x < 2000 or self.dir == -1 and self.x > 0 :
            self.x += self.dir * self.speed * game_framework.frame_time
        if (get_time() - mRUN.timer) >= 5 :
            self.get_event(AT)
        pass

    def draw(self, x) :
        self.draw(x)

class mATTACK :
    effect_frame = None

    @staticmethod
    def enter(self,player) :
        self.sprite = self.attack_s
        self.frame = 0
        mATTACK.effect_frame = 0
        pass

    @staticmethod
    def exit(self) :
        pass

    @staticmethod
    def do(self,player) :
        self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME* game_framework.frame_time) % 6
        mATTACK.effect_frame = (mATTACK.effect_frame + FRAME_PER_ACTION2 * ACTION_PER_TIME2* game_framework.frame_time) % 10
        if int(mATTACK.effect_frame) == 5 :
            player.get_damage(0, self)
        if int(self.frame) == 5 :
            self.get_event(RU)
        pass

    def draw(self, x) :
        self.draw(x)
        self.effect_draw(mATTACK.effect_frame,x)

class mDEAD :
    @staticmethod
    def enter(self,player) :
        self.sprite = self.dead_s
        self.frame = 0
        pass

    @staticmethod
    def exit(self) :
        pass

    @staticmethod
    def do(self,player) :
        self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME* game_framework.frame_time) % 6
        if int(self.frame) == 5 :
            game_world.remove_object(self)
            game_framework.push_state(stage_clear)
        pass

    def draw(self, x) :
        self.draw(x)

mNext_state = {
    mRUN : { RU : mRUN, AT : mATTACK, KIA : mDEAD},
    mATTACK : { RU : mRUN, AT : mATTACK, KIA : mDEAD},
    mDEAD : {RU : mDEAD, AT : mDEAD, KIA : mDEAD} 
}

class Boss :
    def __init__ (self, _x, _y, _hp, _w,_h) :
        self.move_s = load_image('boss/boss_move.png')
        self.attack_s = load_image('boss/boss_attack.png')
        self.effect = load_image('boss/boss_effect.png')
        self.dead_s = load_image('boss/boss_dead.png')
        self.symbol = load_image('boss/symbol.png')
        self.sprite = self.move_s
        self.hp = _hp
        self.atk_count = 0
        self.x = _x
        self.y = _y
        self.speed = BOSS_RUN_SPEED_PPS
        self.wide = _w
        self.hight = _h
        self.frame = 0
        self.dir = 1
        self.q = []
        self.cur_state = mRUN
        self.exp = _hp // 10

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
                    self.sprite.clip_composite_draw(int(self.frame) * self.wide,0,self.wide,self.hight,0,'',400 - (x - self.x), self.y,300,250)
                    self.dir = -1
                elif self.x <= x :
                    self.sprite.clip_composite_draw(int(self.frame) * self.wide,0,self.wide,self.hight,0,'h',400 + (self.x - x), self.y,300,250)
                    self.dir = 1
        elif x <= 400:
            if self.x > 0 and self.x < 800 :
                if self.x > x :
                    self.sprite.clip_composite_draw(int(self.frame) * self.wide,0,self.wide,self.hight,0,'',self.x, self.y,300,250)
                    self.dir = -1
                elif self.x <= x :
                    self.sprite.clip_composite_draw(int(self.frame) * self.wide,0,self.wide,self.hight,0,'h',self.x, self.y,300,250)
                    self.dir = 1
        elif x >= 1600 :
            if self.x > 1200 and self.x < 2000 :
                if self.x > x :
                    self.sprite.clip_composite_draw(int(self.frame) * self.wide,0,self.wide,self.hight,0,'',400 - (1600 - self.x), self.y,300,250)
                    self.dir = -1
                elif self.x <= x :
                    self.sprite.clip_composite_draw(int(self.frame) * self.wide,0,self.wide,self.hight,0,'h',400 + (self.x - 1600), self.y,300,250)
                    self.dir = 1

    # self.sprite.clip_composite_draw(int(self.frame) * self.wide,0,self.wide,self.hight,0,'h',self.x, self.y,300,250)

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

    def effect_draw(self, _frame, x) :
        if x <= 400 :
            self.effect.clip_draw(int(_frame)*250,0,250,300,x,180)
            self.symbol.draw(x,200)
        if x > 400 and x < 1600 :
            self.effect.clip_draw(int(_frame)*250,0,250,300,400,180)
            self.symbol.draw(400,200)
        if x >= 1600 :
            self.effect.clip_draw(int(_frame)*250,0,250,300,400 + (x - 1600),180)
            self.symbol.draw(400 + (x - 1600),200)