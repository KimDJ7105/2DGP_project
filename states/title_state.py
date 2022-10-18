from pico2d import *
from random import randint
import game_framework
import states.play_state as play_state
import classes.map_class as map_class


map = None
image_player = None
frame = None
title = None

def enter():
    global image_player, map
    global frame, title
    frame = 0
    image_player = load_image('player/standard.png')
    title = load_image('menus/title.png')
    map = map_class.Map()
    map.set_map_type(randint(0,4))
    map.set_image()


def exit():
    global image_player, frame
    global map, title
    del title
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
    title.draw(400,300,500,300)
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