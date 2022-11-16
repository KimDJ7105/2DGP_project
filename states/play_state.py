from pico2d import *
import game_framework
import classes.map_class as map_class
import classes.player_class as player_class
import classes.monster_class as monster_class
import states.map_select_state as map_select_state
import states.game_over_state as game_over_state
import parameter.boss_parameter as boss_parameter

map = None
cat = None
boss = None
spawn = None
spawn_timer = None

def enter() :
    global map
    global cat, boss, spawn, spawn_timer
    map = map_class.Map()
    map.set_map_type(0)
    map.set_image()
    cat = player_class.Player()
    boss = []
    spawn = False
    spawn_timer = 0

def exit():
    global map, cat, boss, spawn
    del map
    del cat
    del spawn
    for monster in boss :
        del monster

def update():
    global spawn_timer, spawn
    cat.update(boss)
    for monster in boss :
        monster.update(cat)
        if monster.hp <= 0 :
            boss.remove(monster)
            del monster
    map.map_move(int(cat.x))
    cat.regen_stamina()
    if cat.hp <= 0 : #if player is dead
        game_framework.push_state(game_over_state)
    if spawn == True:
        spawn_timer += boss_parameter.FRAME_PER_SPAWN * boss_parameter.SPAWN_PER_TIME* game_framework.frame_time
    if int(spawn_timer) == 15:
        print('monster spawn')
        if map.map_type == 0 :
            spawn = False
        elif map.map_type == 1 :
            pass
        elif map.map_type == 2 :
            boss.append(monster_class.Monster(2000, 90,'boss/mon1.png',boss_parameter.MIRA_RUN_SPEED_PPS, 80))
        elif map.map_type == 3 :
            pass
        spawn_timer = 0.0


def draw():
    clear_canvas()
    map.draw_wide()
    for monster in boss :
        monster.cur_state.draw(monster,map.map_x)
    cat.cur_state.draw(cat)
    update_canvas()


def handle_events():
    events = get_events()
    for event in events :
        if event.type == SDL_KEYDOWN or event.type == SDL_KEYUP:
            if event.key == SDLK_s :
                # if cat.x > 1860 and cat.x < 2000 :
                game_framework.push_state(map_select_state)
            elif event.key == SDLK_z and event.type == SDL_KEYDOWN:
                cat.set_sword()
            elif event.key == SDLK_w :
                if cat.y == 90 :
                    cat.add_jump()
            elif event.key == SDLK_SPACE:
                if cat.stamina > 30 and cat.roll == False:
                    cat.add_roll()
            elif event.type == SDL_KEYDOWN and event.key == SDLK_h :
                cat.get_damage(1)
            else :
                cat.handle_event(event)
        elif event.type == SDL_QUIT :
            game_framework.quit()

def pause() :
    pass

def resume() :
    pass