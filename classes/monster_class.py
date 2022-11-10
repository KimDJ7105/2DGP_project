from pico2d import *
import classes.player_class as cat

class Monster :
    def __init__ (self) :
        self.sprite = load_image('boss/temp.png')
        self.hp = 100
        self.atk_count = 0
        self.x = 1400
        self.y = 120
        self.wide = 482
        self.hight = 146

    def get_distance(self, player) :
        pass

    def attack_far(self) :
        pass

    def attack_close(self) :
        pass

    def attack_mid(self) :
        pass

    def move(self):
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