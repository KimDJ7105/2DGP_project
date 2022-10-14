from pico2d import *
from random import randint
import game_framework


image_grass = None
image_background = None
image_player = None
image_type = randint(0,4)
frame = 0

def enter():
    global image_grass, image_background, image_player
    image_player = load_image('player_resource/2DGP.png')
    match image_type :
        case 0 :
            image_grass = load_image('map/grass.png')
            image_background = load_image('map/town.png')
        case 1 :
            image_grass = load_image('map/grass.png')
            image_background = load_image('map/desert.png')
        case 2 :
            image_grass = load_image('map/grass.png')
            image_background = load_image('map/snowland.png')
        case 3 :
            image_grass = load_image('map/grass.png')
            image_background = load_image('map/volcano.png')


def exit():
    global image_type, image_player, image_background, image_grass
    del image_type
    del image_player
    del image_background
    del image_grass

def update():
    global frame
    frame = (frame + 1) % 7
    pass


def draw():
    clear_canvas()
    image_background.draw(400,300,800,600)
    image_grass.draw(400,30)
    image_player.clip_draw(frame * 100,300 * 1,100,100,100,90)
    update_canvas()
    delay(0.1)

def handle_events():
    events = get_events()
    for event in events :
        if event.type == SDL_KEYDOWN :
            if event.key == SDLK_SPACE :
                pass
                # game_framework.change_state('')
        elif event.type == SDL_QUIT :
            game_framework.quit()