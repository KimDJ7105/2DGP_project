from pico2d import *
import game_framework
import map_class

map = None

def enter() :
    global map
    map = map_class.Map()

def exit():
    global map
    del map

def update():
    pass

def draw():
    clear_canvas()
    map.draw()
    update_canvas()
    pass

def handle_events():
    events = get_events()
    for event in events :
        if event.type == SDL_KEYDOWN :
            if event.key == SDLK_SPACE :
                pass
        elif event.type == SDL_QUIT :
            game_framework.quit()

def pause() :
    pass

def resume() :
    pass