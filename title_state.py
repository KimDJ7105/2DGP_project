from pico2d import *
from random import randint
import game_framework
import play_state
import map_class


map = None
image_player = None
frame = None

def enter():
    global image_player, map
    global frame
    frame = 0
    image_player = load_image('player/2DGP.png')
    map = map_class.Map()
    map.set_map_type(randint(0,4))
    map.set_image()


def exit():
    global image_player, frame
    global map
    del frame
    del image_player
    del map

def update():
    global frame
    frame = (frame + 1) % 7
    pass


def draw():
    clear_canvas()
    map.draw()
    image_player.clip_draw(frame * 100,300 * 1,100,100,100,90)
    update_canvas()
    delay(0.1)

def handle_events():
    events = get_events()
    for event in events :
        if event.type == SDL_KEYDOWN :
            if event.key == SDLK_SPACE :
                game_framework.change_state(play_state)
        elif event.type == SDL_QUIT :
            game_framework.quit()