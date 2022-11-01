from pico2d import *
import game_framework
import states.title_state as title_state
import states.play_state as play_state

open_canvas()

hide_cursor()

game_framework.run(play_state)

close_canvas()