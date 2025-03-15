import pyray as rl 
import time as time

import loop_data_module
import game_module


def main():
    rl.set_random_seed(int(time.perf_counter()))

    title = "python raylib"
    screen_width = 800
    screen_height = 600

    rl.init_window(screen_width,screen_height,title)
    #rl.set_target_fps(60)

    loop = loop_data_module.Loop_Data()
    game = game_module.Game(loop)   

    # Main loop
    while loop.is_running:

        # Timing
        loop.new_time =  rl.get_time()
        loop.frame_time = loop.new_time - loop.current_time  
        loop.current_time = loop.new_time 

        loop.accumulator += loop.frame_time 
        loop.accumulator_each_second += loop.frame_time

        
        # Update 
        loop.update_counter = 0
        while loop.accumulator >= loop.dt:
            loop.accumulator -= loop.dt
            loop.update_counter += 1

            loop.is_running = not rl.window_should_close()
            if not loop.is_running: 
                break

            if not loop.is_drawing:
                rl.poll_input_events()
            
            loop.is_drawing = False

            game_module.input(game)  
            game_module.update(game,loop.t,loop.dt)

            if loop.update_counter > 10:
                loop.accumulator = 0
                break
        
        # Rendering 
        if loop.update_counter > 0:
            game_module.render(game)
            loop.is_drawing = True
            loop.fps_counter += 1
        
        # Do things each second
        if loop.accumulator_each_second >= 1.0:
            loop.accumulator_each_second -= 1.0
            loop.fps = loop.fps_counter
            loop.fps_counter = 0
        
    rl.close_window()    

main()