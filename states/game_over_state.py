from pico2d import *
import states.play_state as play_state
import game_framework
import classes.monster_class as Boss

retry = None
game_over = None

def enter() :
    global retry, game_over
    retry = False
    game_over = load_image('menus/gameover.png')
    if play_state.boss != None :
        del play_state.boss
        play_state.boss = None
    pass

def exit():
    global retry, game_over
    if retry == False :
        play_state.cat.hp = 5
        play_state.map.set_map_type(0)
        play_state.cat.y = 550
    elif retry == True :
        play_state.cat.hp = 5
    del retry
    del game_over
    pass

def update() :
    pass

def draw() :
    clear_canvas()
    play_state.map.draw_wide()
    play_state.cat.draw()
    game_over.draw(400,300)
    update_canvas()


def handle_events():
    events = get_events()
    for event in events :
        if event.type == SDL_KEYDOWN :
            game_framework.pop_state()
        elif event.type == SDL_QUIT :
            game_framework.quit()
    pass