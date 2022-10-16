from pico2d import *
import game_framework
import classes.map_class as map_class
import classes.player_class as player_class
import states.map_select_state as map_select_state

map = None
cat = None

def enter() :
    global map
    global cat
    map = map_class.Map()
    cat = player_class.Player()

def exit():
    global map, cat
    del map
    del cat

def update():
    cat.frame_update()
    cat.move()
    
    pass

def draw():
    clear_canvas()
    map.draw()
    cat.draw()
    update_canvas()
    pass

def handle_events():
    events = get_events()
    for event in events :
        if event.type == SDL_KEYDOWN :
            if event.key == SDLK_w :
                if cat.y == 90 :
                    cat.set_jump(True)
            elif event.key == SDLK_a :
                cat.set_dir(-1)
            elif event.key == SDLK_s :
                pass
            elif event.key == SDLK_d :
                cat.set_dir(1)
            elif event.key == SDLK_SPACE :
                pass
            elif event.key == SDLK_m :
                game_framework.push_state(map_select_state)
        elif event.type == SDL_KEYUP :
            if event.key == SDLK_a or event.key == SDLK_d:
                cat.set_dir(0)
        elif event.type == SDL_QUIT :
            game_framework.quit()

def pause() :
    pass

def resume() :
    pass