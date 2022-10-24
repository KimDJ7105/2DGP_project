from pico2d import *
import game_framework
import states.title_state as title_state

open_canvas()

hide_cursor()

game_framework.run(title_state)

close_canvas()