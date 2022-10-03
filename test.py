from pico2d import *

open_canvas()

background = load_image('town.png')
player = load_image('player_resource/2DGP.png')
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
    global idle_frame
    global run_frame
    if type == 0 : #idle
        if last_dir == 1 or last_dir == 0:
            player.clip_draw(idle_frame * 100,100 * 3,100,100,x,y)
            idle_frame = (idle_frame + 1) % 4
        elif last_dir == -1 :
            player.clip_draw(idle_frame * 100,100 * 2,100,100,x,y)
            idle_frame = (idle_frame + 1) % 4
    elif type == 1 : #run
        if dir == 1 :
            player.clip_draw(run_frame * 100,100 * 1,100,100,x,y)
            run_frame = (run_frame + 1) % 7
        elif dir == -1 :
            player.clip_draw(run_frame * 100,100 * 0,100,100,x,y)
            run_frame = (run_frame + 1) % 7
    elif type == 2 : #jump
        if dir == 1 or dir == 0:
            player.clip_draw(5 * 100, 100* 3,100,100,x,y)
        elif dir == -1:
            player.clip_draw(5 * 100, 100* 2,100,100,x,y)

def Handle_events() :
    global x
    global y
    global running
    global dir
    global pl_draw
    global last_dir
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
                last_dir = 1
                pl_draw = 0
            elif event.key == SDLK_a :
                dir = 0
                last_dir = -1
                pl_draw = 0
            elif event.key == SDLK_w :
                y = 90
                pl_draw = 0


idle_frame = 0
run_frame = 0
x = 800 // 2
y = 90
dir = 0
last_dir = 0
running = True
pl_draw = 0
map_draw = 0

while running :
    clear_canvas()
    print_map(map_draw)
    set_player(pl_draw)
    update_canvas()

    Handle_events()
    if x < 800 and dir == 1 :
        x += dir * 7
    if x > 0 and dir == -1 :
        x += dir * 7
    delay(0.03)


close_canvas()