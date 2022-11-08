from pico2d import *
import game_framework
import classes.map_class as map_class
import classes.player_class as player_class
import states.map_select_state as map_select_state

map = None
cat = None
boss = None

def enter() :
    global map
    global cat
    map = map_class.Map()
    map.set_map_type(0)
    map.set_image()
    cat = player_class.Player()

def exit():
    global map, cat
    del map
    del cat

def update():
    cat.update(boss)
    map.map_move(int(cat.x))
    cat.regen_stamina()

def draw():
    clear_canvas()
    map.draw_wide()
    cat.cur_state.draw(cat)
    if boss != None :
        boss.draw(int(cat.x))
    update_canvas()


def handle_events():
    events = get_events()
    for event in events :
        if event.type == SDL_KEYDOWN or event.type == SDL_KEYUP:
            if event.key == SDLK_s :
                if cat.x > 1860 and cat.x < 2000 :
                    game_framework.push_state(map_select_state)
            elif event.key == SDLK_z and event.type == SDL_KEYDOWN:
                cat.set_sword()
            elif event.key == SDLK_w :
                if cat.y == 90 :
                    cat.add_jump()
            elif event.key == SDLK_SPACE:
                if cat.stamina > 30 and cat.roll == False:
                    cat.add_roll()
            elif event.key == SDLK_h :
                cat.get_damage(1)
            else :
                cat.handle_event(event)
        elif event.type == SDL_QUIT :
            game_framework.quit()

def pause() :
    pass

def resume() :
    pass