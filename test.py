from pico2d import *

open_canvas()

background = load_image('town.png')
player = load_image('player_resource/Player_Standing.png')
land = load_image('grass.png')

def print_map(  type ) :
    global land
    global background
    if type == 0 :
        background = load_image('town.png')
        land = load_image('grass.png')
    background.draw(400,300,800,600)
    land.draw(400,30)

def set_player(type) :
    global player
    if type == 0 :
        player = load_image('player_resource/Player_Standing.png')
    elif type == 1 :
        player = load_image('player_resource/wark.png')
    elif type == 2 :
        player = load_image('player_resource/jump.png')

frame = 0;

for x in range(40,600 + 1, 10) :
    clear_canvas()
    print_map(0)
    set_player(1)
    player.clip_draw(0 + (frame * 100),0,100,100,x,90)
    update_canvas()
    frame = (frame + 1) % 4
    if frame == 3 :
        for y in range(90,120+1, 10) :
            set_player(2)
            player.draw(x,y)
            delay(0.1)
    delay(0.05)
    get_events()



close_canvas()