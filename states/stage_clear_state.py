from pico2d import *
import states.play_state as play_state
import game_framework
import states.game_world as game_world
from parameter.player_parameter import *


font1 = None
font2 = None
board = None
pi = None
frame = None

def enter() :
    global font1, font2, board, pi, frame
    font1 = load_font('menus/ENCR10B.TTF', 45)
    font2 = load_font('menus/ENCR10B.TTF', 25)
    board = load_image('menus/board.png')
    pi = load_image('player/standard.png')
    frame = 0
    pass

def exit():
    global font1, font2, board, pi, frame
    play_state.cat.hp = 5
    play_state.map.set_map_type(0)
    play_state.cat.y = 1000
    play_state.cat.hp_potion = 5
    game_world.clear_monsters()
    del font1
    del font2
    del board
    del pi
    del frame
    pass

def update() :
    global frame
    frame = (frame + FRAME_PER_ACTION * ACTION_PER_TIME* game_framework.frame_time) % 7
    pass

def draw() :
    clear_canvas()
    play_state.map.draw_wide()
    play_state.cat.draw()
    board.draw(400,300,500,400)
    font1.draw(280,320,'Stage Clear!',(255,255,255))
    font2.draw(300,250,'Return To Town',(255,255,255))
    pi.clip_draw(int(frame) * 100,300 * 1,100,100,280,270)
    update_canvas()


def handle_events():
    events = get_events()
    for event in events :
        if event.type == SDL_KEYDOWN :
            game_framework.pop_state()
        elif event.type == SDL_QUIT :
            game_framework.quit()
    pass