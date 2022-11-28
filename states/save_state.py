import states.play_state as play_state
import pickle
from pico2d import *
import game_framework

save_data = None
save_data2 = None

def enter():
    global save_data, save_data2
    save_data = {'atk': play_state.cat.atk, 'item': play_state.cat.item, 'level': play_state.cat.item_level, 'exp' : play_state.cat.exp, 'atk_on' : play_state.cat.atk_on}
    save_data2 = play_state.cat
    print(save_data)


def exit():
    global save_data
    del save_data
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
                with open('save1.pickle', 'wb') as f:
                    pickle.dump(save_data2,f)
                game_framework.pop_state()
            elif event.key == SDLK_2 :
                with open('save2.pickle', 'wb') as f:
                    pickle.dump(save_data,f)
                    game_framework.pop_state()
            elif event.key == SDLK_3 :
                with open('save3.pickle', 'wb') as f:
                    pickle.dump(save_data,f)
                    game_framework.pop_state()
        pass