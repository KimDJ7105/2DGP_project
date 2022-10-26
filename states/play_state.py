from pico2d import *
import game_framework
import classes.map_class as map_class
import classes.player_class as player_class
import states.map_select_state as map_select_state

map = None
cat = None
frame_rate = None

def enter() :
    global map
    global cat
    global frame_rate
    frame_rate = 0
    map = map_class.Map()
    map.set_map_type(0)
    map.set_image()
    cat = player_class.Player()

def exit():
    global map, cat
    del map
    del cat

def update():
    global frame_rate
    frame_rate = (frame_rate + 1) % 30
    if frame_rate == 29 :
        cat.frame_update()
    cat.move()
    map.map_move(cat.x)
    cat.regen_stamina()

def draw():
    clear_canvas()
    map.draw_wide()
    if cat.size == 100 :
        cat.draw()
    elif cat.size == 200 :
        cat.draw_weapon()
    update_canvas()


def handle_events():
    events = get_events()
    for event in events :
        if event.type == SDL_KEYDOWN :
            if event.key == SDLK_w :
                cat.set_jump(True)
            elif event.key == SDLK_a :
                cat.set_dir(-1)
            elif event.key == SDLK_d :
                cat.set_dir(1)
            elif event.key == SDLK_s :
                if cat.x > 1860 and cat.x < 2000 :
                    game_framework.push_state(map_select_state)
            elif event.key == SDLK_SPACE :
                cat.set_roll(True)
            elif event.key == SDLK_m :
                game_framework.push_state(map_select_state)
            elif event.key == SDLK_z :
                cat.set_sword()
        elif event.type == SDL_KEYUP :
            if event.key == SDLK_a or event.key == SDLK_d:
                cat.set_dir(0)
        elif event.type == SDL_QUIT :
            game_framework.quit()

def pause() :
    pass

def resume() :
    pass