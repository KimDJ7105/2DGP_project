from pico2d import *
from random import randint
import game_framework
import states.map_select_state as map_select_state
import states.game_world as game_world
import states.save_state as save_state
import states.load_state as load_state
import classes.map_class as map_class
import classes.player_class as player_class

map = None
cat = None
font = None
timer = None

def enter() :
    global map
    global cat
    global font
    global timer
    timer = 0
    font = load_font('menus/ENCR10B.TTF', 16)
    map = map_class.Map()
    map.set_map_type(0)
    map.set_image()
    cat = player_class.Player()
    game_world.add_object(cat,'player')
    game_world.add_object(map,'player')

def exit():
    global font
    del font
    game_world.clear()

def update():
    game_world.world_update(cat, map)
    game_world.spawn_monster(map.map_type,randint(0, 2))

def draw():
    clear_canvas()
    map.draw_wide()
    for monster in game_world.monsters :
        monster.cur_state.draw(monster,cat.x)
    cat.cur_state.draw(cat)
    if map.map_type != 0 :
        font.draw(750, 550, f'{(get_time() - timer):.2f}', (255, 255, 255))
    update_canvas()


def handle_events():
    events = get_events()
    for event in events :
        if event.type == SDL_KEYDOWN or event.type == SDL_KEYUP:
            if event.key == SDLK_s :
                # if cat.x > 1860 and cat.x < 2000 :
                # game_framework.push_state(map_select_state)
                game_framework.push_state(save_state)
            elif event.key == SDLK_l :
                game_framework.push_state(load_state)
            elif event.key == SDLK_z and event.type == SDL_KEYDOWN:
                cat.set_sword()
            elif event.key == SDLK_w :
                if cat.y == 90 :
                    cat.add_jump()
            elif event.key == SDLK_SPACE:
                if cat.stamina > 30 and cat.roll == False:
                    cat.add_roll()
            elif event.key == SDLK_r and event.type == SDL_KEYUP:
                cat.heal_hp()
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