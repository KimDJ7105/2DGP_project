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
    global frame
    if type == 0 :
        player = load_image('player_resource/Player_Standing.png')
        player.draw(x,y)
    elif type == 1 :
        player = load_image('player_resource/wark.png')
        player.clip_draw(frame * 100 , 0 ,100, 100,x,y)
    elif type == 2 :
        player = load_image('player_resource/jump.png')
        player.draw(x,y)

def Handle_events() :
    global x
    global y
    global running
    global dir
    global pl_draw
    events = get_events()
    for event in events :
        if event.type == SDL_QUIT :
            running = False
        elif event.type == SDL_KEYDOWN :
            if event.key == SDLK_ESCAPE :
                running = False
            elif event.key == SDLK_d :
                dir = 1
                pl_draw = 1
            elif event.key == SDLK_a :
                dir = -1
                pl_draw = 1
            elif event.key == SDLK_w :
                y = 140
                pl_draw = 2
        elif event.type == SDL_KEYUP :
            if event.key == SDLK_d :
                dir = 0
                pl_draw = 0
            elif event.key == SDLK_a :
                dir = 0
                pl_draw = 0
            elif event.key == SDLK_w :
                y = 90
                pl_draw = 0


frame = 0;
x = 800 // 2
y = 90
dir = 0
running = True
pl_draw = 0
map_draw = 0

while running :
    clear_canvas()
    print_map(map_draw)
    set_player(pl_draw)
    update_canvas()

    Handle_events()
    frame = (frame + 1) % 4
    if x < 800 and dir == 1 :
        x += dir * 5
    if x > 0 and dir == -1 :
        x += dir * 5
    delay(0.01)


close_canvas()