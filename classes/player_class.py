from pico2d import *

RD, LD, RU, LU, WD, WU, MD, SPACE, END, ATKED, QD, QU  = range(12)

key_event_table = {
    (SDL_KEYDOWN, SDLK_q) : QD,
    (SDL_KEYUP, SDLK_q) : QU,
    (SDL_KEYDOWN, SDLK_a) : LD,
    (SDL_KEYDOWN,SDLK_d) : RD,
    (SDL_KEYUP, SDLK_a) : LU,
    (SDL_KEYUP, SDLK_d) : RU,
    (SDL_KEYDOWN,SDLK_w) : WD,
    (SDL_KEYUP, SDLK_w) : WU,
    (SDL_KEYDOWN, SDLK_SPACE) : SPACE,
    (SDL_KEYDOWN, SDLK_m) : MD,
}

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
        self.frame = (self.frame + 1) % 4
        if self.y < 90 :
            self.y = 90
        elif self.y > 90 :
            self.y -= 7
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
                self.ine = 4

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
        self.frame = (self.frame + 1) % 7
        self.x += self.dir * 5
        self.x = clamp(0, self.x, 2000)
        if self.y < 90 :
            self.y = 90
        elif self.y > 90 :
            self.y -= 7
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
        self.frame += 1
        if self.last_dir == 1 :
            if self.x < 2000 :
                self.x += 30
        elif self.last_dir == -1 :
            if self.x > 0 :
                self.x -= 30
        if self.frame == 4 :
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
            self.y += 7
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
        #self.deal_damage(self.x, self.x + 10, boss, 10)
        self.atking = False
        pass

    @staticmethod
    def do(self):
        if self.atking == True :
            self.frame += 1
            if self.frame == 6 :
                self.add_event(END)
            if self.y < 90 :
                self.y = 90
            elif self.y > 90 :
                self.y -= 7

    @staticmethod
    def draw(self):
        self.draw()

class HIT :
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
        if self.frame == 0 :
            self.frame = 1
        elif self.frame == 1 :
            self.frame = 0
        HIT.timer += 1
        if HIT.timer == 15 :
            self.add_event(END)

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
        pass

    @staticmethod
    def exit(self,boss) :
        pass

    @staticmethod
    def do(self):
        if self.frame < 3 :
            self.frame += 1
        if self.stamina >= 5 :
            global charge
            charge += 3
            self.stamina -= 5
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
        pass

    @staticmethod
    def exit(self, boss) :
        #self.deal_damage(self.x, self.x + 10, boss, charge)
        #after boss
        pass

    @staticmethod
    def do(self):
        if self.frame < 8 :
            self.frame += 1
        elif self.frame == 8 :
            self.add_event(END)
        pass

    @staticmethod
    def draw(self):
        self.draw()


next_state = {
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, WD : JUMP, WU: JUMP, SPACE: ROLL, END : IDLE, MD : ATTACK, ATKED : HIT, QD : SP_1, QU : IDLE},
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

    def draw(self) :
        if self.atk_on == False :
            if self.x > 400 and self.x < 1600 : 
                self.sprite.clip_draw(self.frame * 100, self.line * 100 , 100, 100, 400, self.y)
            elif self.x <= 400 :
                self.sprite.clip_draw(self.frame * 100, self.line * 100 , 100, 100, self.x, self.y)
            elif self.x >= 1600 :
                self.sprite.clip_draw(self.frame * 100, self.line * 100 , 100, 100, 400 + (self.x - 1600), self.y)
        elif self.atk_on == True :
            if self.x > 400 and self.x < 1600 : 
                self.sprite.clip_draw(self.frame * 200, self.line * 200 , 200, 200, 400, self.y + 50)
            elif self.x <= 400 :
                self.sprite.clip_draw(self.frame * 200, self.line * 200 , 200, 200, self.x, self.y + 50)
            elif self.x >= 1600 :
                self.sprite.clip_draw(self.frame * 200, self.line * 200 , 200, 200, 400 + (self.x - 1600), self.y + 50)
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
            self.stamina += 0.1
        if self.stamina > 100 :
            self.stamina = 100

    def add_event(self, key_event) :
        self.q.insert(0,key_event)

    # def attack(self) :
    #     if self.atk_on == False :
    #         self.atk_on = True
    #         if self.last_dir == 1:
    #             self.line = 6
    #         elif self.last_dir == -1:
    #             self.line = 7
    #         self.frame = 0
    #     elif self.atk_on == True and self.frame == 2 :
    #         self.line = 6
    #         self.frame = 3

    def set_default(self) :
        self.sprite = load_image('player/standard.png')

    def set_sword(self) :
        if self.atk_on == False :
            self.sprite = load_image('player/sword.png')
            self.atk_on = True
            self.item = 'SWORD'
        elif self.atk_on == True:
            if self.item_level['SWORD'] == 1:
                self.sprite = load_image('player/sword2.png')
                self.item_level['SWORD'] = 2
            elif self.item_level['SWORD'] == 2:
                self.sprite = load_image('player/sword3.png')
                self.item_level['SWORD'] = 3

    def update(self, boss) :
        self.cur_state.do(self)

        if self.q :
            event = self.q.pop()
            if event != self.cur_state :
                self.cur_state.exit(self, boss)
                self.cur_state = next_state[self.cur_state][event]
                self.cur_state.enter(self, event)

    def handle_event(self, event) :
        if (event.type , event.key) in key_event_table :
            key_event = key_event_table[(event.type , event.key)]
            self.add_event(key_event)

    def add_roll(self) :
        self.add_event(SPACE)

    def add_jump(self) :
        self.add_event(WD)

    def get_damage(self, damage) :
        if self.roll == False and self.atked == False :
            self.hp -= damage
            self.add_event(ATKED)

    def deal_damage(self, start, end, boss, damage) :
        if boss.x >= start and boss.x <= end :
            boss.get_damage(damage)
