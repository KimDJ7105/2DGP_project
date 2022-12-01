import states.play_state as play_state
import pickle
from pico2d import *
import game_framework
from parameter.player_parameter import *

save_data = None
font = None
board = None
image_player = None
slot = None
frame = None

def enter():
    global save_data, font, board, image_player, slot, frame
    save_data = {'atk': play_state.cat.atk, 'item': play_state.cat.item, 'level': play_state.cat.item_level, 'exp' : play_state.cat.exp, 'atk_on' : play_state.cat.atk_on}
    print(save_data)
    font = load_font('menus/ENCR10B.TTF', 45)
    board = load_image('menus/board.png')
    image_player = load_image('player/standard.png')
    slot = 1
    frame = 0


def exit():
    global save_data,font, board,image_player, slot,frame
    del save_data
    del font
    del board
    del image_player
    del slot
    del frame
    pass

def update():
    global frame
    frame = (frame + FRAME_PER_ACTION * ACTION_PER_TIME* game_framework.frame_time) % 7
    pass

def draw():
    clear_canvas()
    play_state.map.draw_wide()
    play_state.cat.draw()
    board.draw(400,300,500,400)
    font.draw(350,340,'SAVE 1', (255,255,255))
    font.draw(350,260,'SAVE 2', (255,255,255))
    font.draw(350,190,'SAVE 3', (255,255,255))
    if slot == 1 :
        image_player.clip_draw(int(frame) * 100,300 * 1,100,100,300,360)
    elif slot == 2 :
        image_player.clip_draw(int(frame) * 100,300 * 1,100,100,300,280)
    elif slot == 3 :
        image_player.clip_draw(int(frame) * 100,300 * 1,100,100,300,210)
    update_canvas()
    pass

def handle_events():
    global slot
    events = get_events()
    for event in events :
        if event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            if slot == 1 :
                with open('save1.pickle', 'wb') as f:
                    pickle.dump(save_data,f)
                game_framework.pop_state()
            elif slot == 2 :
                with open('save2.pickle', 'wb') as f:
                    pickle.dump(save_data,f)
                    game_framework.pop_state()
            elif slot == 3 :
                with open('save3.pickle', 'wb') as f:
                    pickle.dump(save_data,f)
                    game_framework.pop_state()
        elif event.type == SDL_KEYDOWN :
            if event.key == SDLK_UP:
                if slot != 1 :
                    slot -= 1
            elif event.key == SDLK_DOWN :
                if slot != 3 :
                    slot += 1
        pass