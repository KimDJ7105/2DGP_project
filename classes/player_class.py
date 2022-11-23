from pico2d import *
import game_framework
from parameter.player_parameter import *
import states.game_world as game_world

class IDLE :
    @staticmethod
    def enter(self, event) :
        self.dir = 0
        if self.last_dir == 1 :
            self.line = 5
        elif self.last_dir == -1 :
            self.line = 4
        self.frame = 0

    @staticmethod
    def exit(self, boss) :
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME* game_framework.frame_time) % 4
        if self.y < 90 :
            self.y = 90
        elif self.y > 90 :
            self.y -= JUMP_SPEED_PPS * game_framework.frame_time
            if self.last_dir == 1:
                self.line = 1
                self.frame = 0
            elif self.last_dir == -1 :
                self.line = 0
                self.frame = 0
        elif self.y == 90:
            if self.last_dir == 1:
                self.line = 5
            elif self.last_dir == -1 :
                self.line = 4

    @staticmethod
    def draw(self):
        self.draw()

class RUN :
    @staticmethod
    def enter(self, event) :
        if event == RD :
            self.dir += 1 
            self.line = 3
        elif event == LD:
            self.dir -= 1
            self.line = 2
        elif event == RU :
            self.dir -= 1
            self.line = 2
        elif event == LU :
            self.dir += 1
            self.line = 3
        self.frame = 0

    @staticmethod
    def exit(self, boss) :
        self.last_dir = self.dir;

    @staticmethod
    def do(self):
        self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME* game_framework.frame_time) % 7
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        self.x = clamp(0, self.x, 2000)
        if self.y < 90 :
            self.y = 90
        elif self.y > 90 :
            self.y -= JUMP_SPEED_PPS * game_framework.frame_time
            if self.last_dir == 1:
                self.line = 1
                self.frame = 0
            elif self.last_dir == -1 :
                self.line = 0
                self.frame = 0
        elif self.y == 90 :
            if self.dir == 1:
                self.line = 3
            elif self.dir == -1 :
                self.line = 2

    @staticmethod
    def draw(self):
        self.draw()

class ROLL :
    @staticmethod
    def enter(self, event) :
        self.roll = True
        self.frame = 1
        self.stamina -= 30
        if self.last_dir == 1:
            self.line = 1
        elif self.last_dir == -1 :
            self.line = 0

    @staticmethod
    def exit(self, boss) :
        self.roll = False;
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME* game_framework.frame_time)
        if self.last_dir == 1 :
            if self.x < 2000 :
                self.x += self.last_dir * ROLL_SPEED_PPS * game_framework.frame_time
        elif self.last_dir == -1 :
            if self.x > 0 :
                self.x += self.last_dir * ROLL_SPEED_PPS * game_framework.frame_time
                #30
        if int(self.frame) == 4 :
            self.add_event(END)
        if self.y < 90 :
            self.y = 90
        elif self.y > 90 :
            self.y -= 4

    @staticmethod
    def draw(self):
        self.draw()

class JUMP :
    @staticmethod
    def enter(self, event) :
        self.jump = True
        if self.last_dir == 1 :
            self.line = 1
        elif self.last_dir == -1 :
            self.line = 0
        self.frame = 0

    @staticmethod
    def exit(self, boss) :
        self.jump = False

    @staticmethod
    def do(self):
        if self.y < 160 :
            self.y += JUMP_SPEED_PPS * game_framework.frame_time
        elif self.y >= 160 :
            self.add_event(END)

    @staticmethod
    def draw(self):
        self.draw()

class ATTACK :
    @staticmethod
    def enter(self, event) :
        if self.stamina >= 20 :
            self.atking = True
            if self.last_dir == 1:
                self.line = 9
            elif self.last_dir == -1:
                self.line = 8
            self.frame = 0
            self.stamina -= 20
        else :
            self.add_event(END)

    @staticmethod
    def exit(self, boss) :
        if self.last_dir == 1 :
            self.deal_damage(self.x, self.x + 15, boss, self.atk)
        elif self.last_dir == -1 :
            self.deal_damage(self.x - 15, self.x, boss, self.atk)
        self.atking = False
        pass

    @staticmethod
    def do(self):
        if self.atking == True :
            self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME* game_framework.frame_time)
            if int(self.frame) == 6 :
                self.add_event(END)
            if self.y < 90 :
                self.y = 90
            elif self.y > 90 :
                self.y -= JUMP_SPEED_PPS * game_framework.frame_time

    @staticmethod
    def draw(self):
        self.draw()

class HIT : #time parameter needed
    timer = 0

    @staticmethod
    def enter(self, event) :
        HIT.timer = 0
        if self.last_dir == 1 :
            self.frame = 0
            self.line = 11
        elif self.last_dir == -1 :
            self.frame = 0
            self.line = 10
        self.atked = True
        pass

    @staticmethod
    def exit(self,boss) :
        self.atked = False
        pass

    @staticmethod
    def do(self):
        HIT.timer += FRAME_PER_HIT * HIT_PER_TIME* game_framework.frame_time
        # if int(HIT.timer) % 2 == 0 :
        if int(self.frame) == 0 :
            self.frame = 1
        elif int(self.frame) == 1 :
            self.frame = 0
        if int(HIT.timer) == 5 :
            self.add_event(END)
        if self.y < 90 :
            self.y = 90
        elif self.y > 90 :
            self.y -= 4

    @staticmethod
    def draw(self):
        self.draw()

charge = None

class SP_1 :
    @staticmethod
    def enter(self, event) :
        global charge
        charge = 0
        if self.last_dir == 1 :
            self.frame = 0
            self.line = 7
        elif self.last_dir == -1 :
            self.frame = 0
            self.line = 6
        self.atking = True
        pass

    @staticmethod
    def exit(self,boss) :
        self.atking = False
        pass

    @staticmethod
    def do(self):
        if self.y > 90 :
            self.y -= JUMP_SPEED_PPS * game_framework.frame_time
        elif self.y < 90 :
            self.y = 90
        if int(self.frame) < 3 :
            self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME* game_framework.frame_time)
        if self.stamina >= 5 :
            global charge
            charge += 3
            self.stamina -= FRAME_PER_REGEN * REGEN_PER_TIME* game_framework.frame_time
            pass
        else :
            self.add_event(END)
        pass

    @staticmethod
    def draw(self):
        self.draw()

class SP_2 :
    @staticmethod
    def enter(self, event) :
        if self.last_dir == 1 :
            self.frame = 4
            self.line = 7
        elif self.last_dir == -1 :
            self.frame = 4
            self.line = 6
        self.atking = True
        pass

    @staticmethod
    def exit(self, boss) :
        self.atking = False
        if self.last_dir == 1 :
            self.deal_damage(self.x, self.x + 15, boss, charge // 10)
        elif self.last_dir == -1 :
            self.deal_damage(self.x - 15, self.x, boss, charge // 10)
        #after boss
        pass

    @staticmethod
    def do(self):
        if self.y > 90 :
            self.y -= JUMP_SPEED_PPS * game_framework.frame_time
        elif self.y < 90 :
            self.y = 90
        if int(self.frame) < 8 :
            self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME* game_framework.frame_time)
        elif int(self.frame) == 8 :
            self.add_event(END)
        pass

    @staticmethod
    def draw(self):
        self.draw()


next_state = {
    IDLE: {RU: IDLE, LU: IDLE, RD: RUN, LD: RUN, WD : JUMP, WU: IDLE, SPACE: ROLL, END : IDLE, MD : ATTACK, ATKED : HIT, QD : SP_1, QU : IDLE},
    RUN: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, WD : JUMP, WU: JUMP, SPACE: ROLL, END : IDLE, MD : ATTACK,ATKED : HIT, QD : SP_1, QU : RUN},
    ROLL : {RU: ROLL, LU: ROLL, RD: ROLL, LD: ROLL, WD : ROLL, WU: ROLL, SPACE: ROLL, END : IDLE, MD : ROLL, ATKED : ROLL, QD : ROLL, QU : ROLL},
    JUMP : {RU: JUMP, LU: JUMP, RD: RUN, LD: RUN, WD : JUMP, WU: JUMP, SPACE: ROLL, END : IDLE, MD : ATTACK, ATKED : HIT, QD : SP_1, QU : JUMP},
    ATTACK : {RU: ATTACK, LU: ATTACK, RD: ATTACK, LD: ATTACK, WD : ATTACK, WU: ATTACK, SPACE: ROLL, END : IDLE, MD : ATTACK, ATKED : HIT, QD : ATTACK, QU : ATTACK},
    HIT : {RU: HIT, LU: HIT, RD: HIT, LD: HIT, WD : HIT, WU: HIT, SPACE: ROLL, END : IDLE, MD : HIT, ATKED : HIT, QD : HIT, QU : HIT},
    SP_1 : {RU: SP_1, LU: SP_1, RD: SP_1, LD: SP_1, WD : SP_1, WU: SP_1, SPACE: ROLL, END : SP_2, MD : SP_1, ATKED : HIT, QD : SP_1, QU : SP_2},
    SP_2 : {RU: SP_2, LU: SP_2, RD: SP_2, LD: SP_2, WD : SP_2, WU: SP_2, SPACE: ROLL, END : IDLE, MD : SP_2, ATKED : HIT, QD : SP_2, QU : SP_2},
}

class Player :
    def __init__(self) :
        self.sprite = load_image('player/standard.png')
        self.heart = load_image('player/heart.png')
        self.stamina_bar = load_image('player/stamina_bar.png')
        self.x = 400
        self.y = 90
        self.hp = 5
        self.atk = 0
        self.frame = 0
        self.dir = 1
        self.last_dir = 1
        self.line = 5 #sprite line
        self.item_level = {'SWORD' : 1,}
        self.item = None
        self.stamina = 100
        self.q = []
        self.cur_state = IDLE
        self.jump = False
        self.roll = False
        self.atk_on = False
        self.atking = False
        self.atked = False
        self.exp = 0
        self.hp_potion = 5

    def draw(self) :
        if self.atk_on == False :
            if self.x > 400 and self.x < 1600 : 
                self.sprite.clip_draw(int(self.frame) * 100, self.line * 100 , 100, 100, 400, self.y)
            elif self.x <= 400 :
                self.sprite.clip_draw(int(self.frame) * 100, self.line * 100 , 100, 100, self.x, self.y)
            elif self.x >= 1600 :
                self.sprite.clip_draw(int(self.frame) * 100, self.line * 100 , 100, 100, 400 + (self.x - 1600), self.y)
        elif self.atk_on == True :
            if self.x > 400 and self.x < 1600 : 
                self.sprite.clip_draw(int(self.frame) * 200, self.line * 200 , 200, 200, 400, self.y + 50)
            elif self.x <= 400 :
                self.sprite.clip_draw(int(self.frame) * 200, self.line * 200 , 200, 200, self.x, self.y + 50)
            elif self.x >= 1600 :
                self.sprite.clip_draw(int(self.frame) * 200, self.line * 200 , 200, 200, 400 + (self.x - 1600), self.y + 50)
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

    def add_event(self, key_event) :
        self.q.insert(0,key_event)

    def set_default(self) :
        self.sprite = load_image('player/standard.png')

    def set_sword(self) :
        if self.atk_on == False :
            self.sprite = load_image('player/sword.png')
            self.atk_on = True
            self.atk = 10
            self.item = 'SWORD'
        elif self.atk_on == True:
            if self.item_level['SWORD'] == 1:
                self.sprite = load_image('player/sword2.png')
                self.atk = 25
                self.item_level['SWORD'] = 2
            elif self.item_level['SWORD'] == 2:
                self.sprite = load_image('player/sword3.png')
                self.atk = 45
                self.item_level['SWORD'] = 3

    def update(self, boss) :
        self.cur_state.do(self)

        if self.q :
            event = self.q.pop()
            if next_state[self.cur_state][event] != self.cur_state :
                self.cur_state.exit(self, boss)
                self.cur_state = next_state[self.cur_state][event]
                self.cur_state.enter(self, event)
        
        if self.atk_on :
            if self.item_level['SWORD'] == 1 and self.exp == 100:
                self.sprite = load_image('player/sword2.png')
                self.atk = 25
                self.item_level['SWORD'] = 2
                self.exp = 0
            elif self.item_level['SWORD'] == 2 and self.exp == 120 :
                self.sprite = load_image('player/sword3.png')
                self.atk = 45
                self.item_level['SWORD'] = 3
                self.exp = 0

        if self.stamina < 100 and self.atking == False:
            self.stamina += FRAME_PER_REGEN * REGEN_PER_TIME* game_framework.frame_time
        if self.stamina > 100 :
            self.stamina = 100

    def handle_event(self, event) :
        if (event.type , event.key) in key_event_table :
            key_event = key_event_table[(event.type , event.key)]
            self.add_event(key_event)

    def add_roll(self) :
        self.add_event(SPACE)

    def add_jump(self) :
        self.add_event(WD)

    def get_damage(self, damage, monster) :
        if self.roll == False and self.atked == False :
            self.hp -= damage
            self.add_event(ATKED)
            game_world.remove_object(monster)

    def deal_damage(self, start, end, boss, damage) :
        for monster in boss :
            if monster.x - (monster.wide / 2) > end or monster.x + (monster.wide / 2) < start:
                pass
            else :
                monster.get_damage(damage)
                if self.last_dir == 1 :
                    monster.x += 25
                elif self.last_dir == -1 :
                    monster.x -= 25
                if monster.hp <= 0 :
                    game_world.remove_object(monster)
                    self.exp += 5

    def heal_hp(self) :
        if self.hp_potion > 0 and self.hp < 5 :
            self.hp += 1
            self.hp_potion -= 1
