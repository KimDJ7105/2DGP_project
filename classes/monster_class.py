from pico2d import *
import classes.player_class as cat

class Monster :
    def __init__ (self) :
        self.sprite = load_image('boss/temp.png')
        self.hp = 100
        self.atk_count = 0
        self.x = 1400
        self.y = 300

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
        #if self.x > x - 400 and self.x < x + 400 :
        self.sprite.draw(400, 300)
        pass