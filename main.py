import pyray as rl 
import time as time

import loop_module
import square_module as game

def main():
    rl.set_random_seed(int(time.perf_counter()))

    title = "python raylib"
    screen_width = 800
    screen_height = 600

    rl.init_window(screen_width,screen_height,title)
    #rl.set_target_fps(60)

    loop = loop_module.Loop_Data()
    loop_module.run(loop,game.Game(loop))

    rl.close_window()    

main()