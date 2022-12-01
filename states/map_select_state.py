from pico2d import *
import states.play_state as play_state
import game_framework
import states.game_world as game_world
from parameter.player_parameter import *

board = None
font1 = None
font2 = None

image_player = None
frame = None

select = None

def enter() :
    global board, font1, font2, image_player, frame,select
    board = load_image('menus/board.png')
    font1 = load_font('menus/ENCR10B.TTF', 45)
    font2 = load_font('menus/ENCR10B.TTF', 20)
    image_player = load_image('player/standard.png')
    frame = 0
    select = 0
    pass

def exit():
    global board, font1, font2, image_player, frame,select
    del board
    del font1
    del font2
    del image_player
    del frame
    del select
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
    font1.draw(350,340,'Snowland', (0,0,0))
    font1.draw(350,260,'Desert', (0,0,0))
    font1.draw(350,190,'Volcano', (0,0,0))
    font2.draw(100,400,'Stay Town', (0,0,0))
    if select == 1 :
        image_player.clip_draw(int(frame) * 100,300 * 1,100,100,300,360)
    elif select == 2 :
        image_player.clip_draw(int(frame) * 100,300 * 1,100,100,300,280)
    elif select == 3 :
        image_player.clip_draw(int(frame) * 100,300 * 1,100,100,300,210)
    elif select == 0 :
        image_player.clip_draw(int(frame) * 100,300 * 1,100,100,80,420)
    update_canvas()


def handle_events():
    global select
    play_state.cat.x = 1000
    events = get_events()
    for event in events :
        if event.type == SDL_KEYDOWN :
            if event.key == SDLK_SPACE :
                play_state.map.set_map_type(select)
                play_state.timer = get_time()
                if select != 0 :
                    game_world.spawn = True
                else :
                    game_world.spawn = False
                game_framework.pop_state()
        elif event.key == SDLK_UP:
            if select != 0 :
                select -= 1
        elif event.key == SDLK_DOWN :
            if select != 3 :
                select += 1
        elif event.type == SDL_QUIT :
            game_framework.quit()
    pass
