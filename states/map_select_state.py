from pico2d import *
import states.play_state as play_state
import game_framework

map_select = None

def enter() :
    global map_select
    map_select = load_image('menus/map_select.png')
    pass

def exit():
    global map_select
    del map_select
    pass

def update() :
    pass

def draw() :
    clear_canvas()
    play_state.map.draw()
    play_state.cat.draw()
    map_select.draw(400,300, 400,300)
    update_canvas()


def handle_events():
    events = get_events()
    for event in events :
        if event.type == SDL_KEYDOWN :
            if event.key == SDLK_1 :
                play_state.map.set_map_type(1)
                game_framework.pop_state()
            elif event.key == SDLK_2 :
                play_state.map.set_map_type(2)
                game_framework.pop_state()
            elif event.key == SDLK_3 :
                play_state.map.set_map_type(3)
                game_framework.pop_state()
            elif event.key == SDLK_0 :
                play_state.map.set_map_type(0)
                game_framework.pop_state()
        elif event.type == SDL_QUIT :
            game_framework.quit()
    pass