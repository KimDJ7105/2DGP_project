from pico2d import *

RD, LD, RU, LU, WD, WU, MD, MU, SPACED, SPACEU, END  = range(11)

key_event_table = {
    (SDL_KEYDOWN, SDLK_a) : LD,
    (SDL_KEYDOWN,SDLK_d) : RD,
    (SDL_KEYUP, SDLK_a) : LU,
    (SDL_KEYUP, SDLK_d) : RU,
    (SDL_KEYDOWN,SDLK_w) : WD,
    (SDL_KEYUP, SDLK_w) : WU,
    (SDL_KEYDOWN, SDLK_SPACE) : SPACED,
    (SDL_KEYUP, SDLK_SPACE) : SPACEU
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
    def exit(self) :
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
    def exit(self) :
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
    def exit(self) :
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
    def exit(self) :
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
        self.atking = True
        if self.last_dir == 1:
            self.line = 9
        elif self.last_dir == -1:
            self.line = 8
        self.frame = 0

    @staticmethod
    def exit(self) :
        self.atking = False
        pass

    @staticmethod
    def do(self):
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


next_state = {
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, WD : JUMP, WU: JUMP, SPACED: ROLL, SPACEU : ROLL, END : IDLE, MD : ATTACK, MU : ATTACK},
    RUN: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, WD : JUMP, WU: JUMP, SPACED: ROLL, SPACEU : ROLL, END : IDLE, MD : ATTACK, MU : ATTACK},
    ROLL : {RU: ROLL, LU: ROLL, RD: ROLL, LD: ROLL, WD : ROLL, WU: ROLL, SPACED: ROLL, SPACEU : ROLL, END : IDLE, MD : ROLL, MU : ROLL},
    JUMP : {RU: JUMP, LU: JUMP, RD: RUN, LD: RUN, WD : JUMP, WU: JUMP, SPACED: ROLL, SPACEU : ROLL, END : IDLE, MD : ATTACK, MU : ATTACK},
    ATTACK : {RU: ATTACK, LU: ATTACK, RD: ATTACK, LD: ATTACK, WD : ATTACK, WU: ATTACK, SPACED: ROLL, SPACEU : ROLL, END : IDLE, MD : ATTACK, MU : ATTACK},
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
        self.jump = False
        self.roll = False
        self.atk_on = False
        self.atking = False
        self.stamina = 100
        self.q = []
        self.cur_state = IDLE

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

    def attack(self) :
        if self.atk_on == False :
            self.atk_on = True
            if self.last_dir == 1:
                self.line = 6
            elif self.last_dir == -1:
                self.line = 7
            self.frame = 0
        elif self.atk_on == True and self.frame == 2 :
            self.line = 6
            self.frame = 3

    def set_default(self) :
        self.sprite = load_image('player/standard.png')

    def set_sword(self) :
        self.sprite = load_image('player/sword.png')
        self.atk_on = True

    def update(self) :
        self.cur_state.do(self)

        if self.q :
            event = self.q.pop()
            if event != self.cur_state :
                self.cur_state.exit(self)
                self.cur_state = next_state[self.cur_state][event]
                self.cur_state.enter(self, event)

    def handle_event(self, event) :
        if (event.type , event.key) in key_event_table :
            key_event = key_event_table[(event.type , event.key)]
            self.add_event(key_event)

    def add_roll(self) :
        self.add_event(SPACED)

    def add_jump(self) :
        self.add_event(WD)