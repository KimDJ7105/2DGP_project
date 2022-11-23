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
    pass

def exit():
    global retry, game_over
    if retry == False :
        play_state.cat.hp = 5
        play_state.map.set_map_type(0)
        play_state.cat.y = 1000
        play_state.cat.hp_potion = 5
        for monster in play_state.boss :
            del monster
        play_state.boss.clear()
    elif retry == True :
        play_state.cat.hp = 5
        play_state.cat.hp_potion = 5
        play_state.cat.y = 1000
    del retry
    del game_over
    pass

def update() :
    pass

def draw() :
    clear_canvas()
    play_state.map.draw_wide()
    for monster in play_state.boss :
        monster.cur_state.draw(monster, play_state.map.map_x)
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