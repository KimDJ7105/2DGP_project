from pico2d import *
import states.play_state as play_state
import game_framework
import classes.monster_class as Boss

retry = None

def enter() :
    global retry
    retry = False
    pass

def exit():
    if retry == False :
        play_state.cat.hp = 5
        play_state.map.set_map_type(0)
    elif retry == True :
        play_state.cat.hp = 5
    pass

def update() :
    pass

def draw() :
    clear_canvas()
    play_state.map.draw_wide()
    play_state.cat.draw()
    update_canvas()


def handle_events():
    events = get_events()
    for event in events :
        if event.type == SDL_KEYDOWN :
            game_framework.pop_state()
        elif event.type == SDL_QUIT :
            game_framework.quit()
    pass