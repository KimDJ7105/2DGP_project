import game_framework
import states.game_over_state as game_over_state
import classes.monster_class as monster_class
import parameter.boss_parameter as boss_parameter

spawn = False
spawn_timer = 0

monsters = []
players = []
world = [monsters, players]

def add_object(o, depth) :
    if depth == 'monster' :
        world[0].append(o)
    elif depth == 'player' :
        world[1].append(o)

def remove_object(o) :
    for list in world :
        if o != None and o in list :
            list.remove(o)
            del o
            return

def all_objects():
    for layer in world:
        for o in layer:
            yield o


def clear():
    for o in all_objects():
        del o
    for layer in world:
        layer.clear()

def clear_monsters() :
    for m in monsters :
        monsters.remove(m)
        del m

def monster_update(player) :
    for monster in monsters :
        monster.update(player)

def player_update(player) :
    player.update(monsters)
    if player.hp <= 0 : #if player is dead
        game_framework.push_state(game_over_state)

def map_update(_map, player) :
    _map.map_move(int(player.x))

def world_update(player, _map) :
    player_update(player)
    monster_update(player)
    map_update(_map, player)

def spawn_monster(_type, _pos):
    global spawn, spawn_timer
    if spawn == True:
        spawn_timer += boss_parameter.FRAME_PER_SPAWN * boss_parameter.SPAWN_PER_TIME* game_framework.frame_time
        if int(spawn_timer) == 15:
            if _type == 0 :
                spawn = False
            elif _type == 1 :
                pass
            elif _type == 2 :
                if _pos == 0 :
                    add_object(monster_class.Monster(2000, 90,'boss/mon1.png',boss_parameter.MIRA_RUN_SPEED_PPS, 60, 100, 100),'monster')
                else :
                    add_object(monster_class.Monster(0, 90,'boss/mon1.png',boss_parameter.MIRA_RUN_SPEED_PPS, 60, 100, 100),'monster')
            elif _type == 3 :
                pass
            spawn_timer = 0.0
            print('monster spawned')
