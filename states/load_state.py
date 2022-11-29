import states.play_state as play_state
import pickle
from pico2d import *
import game_framework

def enter():
    print('load state')
    pass


def exit():
    pass

def update():
    pass

def draw():
    clear_canvas()
    play_state.map.draw_wide()
    play_state.cat.draw()
    update_canvas()
    pass

def handle_events():
    events = get_events()
    for event in events :
        if event.type == SDL_KEYDOWN :
            if event.key == SDLK_1 :
                with open('save1.pickle', 'rb') as f:
                    state = pickle.load(f)
                    play_state.cat.load(state)
                game_framework.pop_state()
            elif event.key == SDLK_2 :
                with open('save2.pickle', 'rb') as f:
                    state = pickle.load(f)
                    play_state.cat.load(state)
                game_framework.pop_state()
            elif event.key == SDLK_3 :
                with open('save3.pickle', 'rb') as f:
                    state = pickle.load(f)
                    play_state.cat.load(state)
                game_framework.pop_state()
        pass