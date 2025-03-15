import pyray as rl 
import time as time

import game_module

def main():
    rl.set_random_seed(int(time.perf_counter()))

    title = "python raylib"
    screen_width = 800
    screen_height = 600

    rl.init_window(screen_width,screen_height,title)
    #rl.set_target_fps(60)

    time_start : float = 0
    time_end : float = 0
    dt : float  = 0
    time_acc : float = 0
    time_acc_second : float = 0

    max_fps : float = 120
    max_frame_time : float = 1/max_fps

    fps_counter = 0
    fps = 0
    update_counter = 0
    is_running : bool = True 
    is_drawing : bool = False


    game = game_module.Game(screen_width,screen_height,1000)   

    # Main loop
    while is_running:

        # Timing
        time_end =  rl.get_time()
        dt = time_end - time_start 
        time_start = time_end 

        time_acc += dt 
        time_acc_second += dt

        
        # Update 
        update_counter = 0
        while time_acc > max_frame_time:
            time_acc -= max_frame_time
            update_counter += 1

            is_running = not rl.window_should_close()
            if not is_running: 
                break

            if not is_drawing:
                rl.poll_input_events()
            
            is_drawing = False
            game_module.input(game)  


            game_module.update(game,max_frame_time)

            if update_counter > 10:
                time_acc = 0
                break
        
        # Rendering 
        if update_counter > 0:
            game_module.render(game,max_frame_time,fps)
            is_drawing = True
            fps_counter += 1
        
        # Do things each second
        if time_acc_second > 1:
            time_acc_second -= 1
            fps = fps_counter
            fps_counter = 0
        
    rl.close_window()    

main()