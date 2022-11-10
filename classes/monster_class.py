from pico2d import *
import classes.player_class as cat

class Monster :
    def __init__ (self) :
        self.sprite = load_image('boss/temp.png')
        self.hp = 10000
        self.atk_count = 0
        self.x = 1400
        self.y = 120

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

    def draw(self, x) :
        if self.x > x - 641 and self.x < x + 641 :
            if self.x > x :
                self.sprite.clip_composite_draw(0,0,482,146,0,'',400 - (x - self.x), self.y)
            elif self.x <= x :
                self.sprite.clip_composite_draw(0,0,482,146,0,'h',400 + (self.x -x), self.y)
        pass