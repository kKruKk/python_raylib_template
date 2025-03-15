from abc import ABC, abstractmethod

class Game(ABC):
    @abstractmethod
    def input(self):
        pass  
    def update(self,t,dt):
        pass
    def render(self):
        pass

class Loop_Data:
    current_time : float = 0
    new_time : float = 0
    frame_time : float = 0
    accumulator : float = 0
    accumulator_each_second : float = 0

    max_fps : float = 120
    dt : float = 1/max_fps
    t : float = 0

    fps_counter : int = 0
    fps : int = 0
    update_counter: int = 0
    is_running : bool = True 
    is_drawing : bool = False

import pyray as rl

def run(loop : Loop_Data,game : Game):
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

            game.input()  
            game.update(loop.t,loop.dt)

            if loop.update_counter > 10:
                loop.accumulator = 0
                break
        
        # Rendering 
        if loop.update_counter > 0:
            game.render()
            loop.is_drawing = True
            loop.fps_counter += 1
        
        # Do things each second
        if loop.accumulator_each_second >= 1.0:
            loop.accumulator_each_second -= 1.0
            loop.fps = loop.fps_counter
            loop.fps_counter = 0