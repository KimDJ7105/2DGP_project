from pico2d import *
import states.play_state as play_state
import game_framework
import states.game_world as game_world
from parameter.player_parameter import *

retry = None
game_over = None
font = None
frame = None
image_player = None

def enter() :
    global retry, game_over,font, image_player, frame
    retry = True
    frame = 0
    game_over = load_image('menus/gameover.png')
    font = load_font('menus/ENCR10B.TTF',20)
    image_player = load_image('player/standard.png')
    game_world.clear_monsters()
    pass

def exit():
    global retry, game_over, image_player, frame, font
    if retry == False :
        play_state.cat.hp = 5
        play_state.map.set_map_type(0)
        play_state.cat.y = 1000
        play_state.cat.hp_potion = 5
    elif retry == True :
        play_state.cat.hp = 5
        play_state.cat.hp_potion = 5
        play_state.cat.y = 1000
    del retry
    del game_over
    del font
    del frame
    del image_player
    pass

def update() :
    global frame
    frame = (frame + FRAME_PER_ACTION * ACTION_PER_TIME* game_framework.frame_time) % 7
    pass

def draw() :
    clear_canvas()
    play_state.map.draw_wide()
    play_state.cat.draw()
    game_over.draw(400,300)
    font.draw(300,200,'Retry',(255,255,255))
    font.draw(450,200,'Go to Town', (255,255,255))
    if retry ==  False :
        image_player.clip_draw(int(frame) * 100,300 * 1,100,100,400,220)
    else :
        image_player.clip_draw(int(frame) * 100,300 * 1,100,100,260,220)
    update_canvas()


def handle_events():
    global retry
    events = get_events()
    for event in events :
        if event.type == SDL_KEYDOWN :
            if event.key == SDLK_LEFT :
                if retry == False :
                    retry = True
            elif event.key == SDLK_RIGHT :
                if retry == True :
                    retry = False
            else :
                game_framework.pop_state()
        elif event.type == SDL_QUIT :
            game_framework.quit()
    pass