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
    is_running : bool = True 
    is_updating: bool = False
    is_drawing : bool = False

    current_scene : Game 

    def change_max_fps(self,max_fps : float):
        self.max_fps = max_fps 
        self.dt = 1.0 / self.max_fps

import pyray as rl

def run(loop : Loop_Data,game : Game):
    loop.current_scene = game
    while loop.is_running:

        # Timing
        loop.new_time =  rl.get_time()
        loop.frame_time = loop.new_time - loop.current_time  
        loop.current_time = loop.new_time 

        loop.accumulator += loop.frame_time 
        loop.accumulator_each_second += loop.frame_time

        
        # Update 
        while loop.accumulator >= loop.dt:
            if loop.accumulator > loop.dt * 10:
                loop.accumulator = loop.dt * 10

            loop.is_running = not rl.window_should_close()
            if not loop.is_running: 
                break

            if not loop.is_drawing:
                rl.poll_input_events()
            
            loop.is_drawing = False

            loop.current_scene.input()  
            loop.current_scene.update(loop.t,loop.dt)

            loop.accumulator -= loop.dt
            loop.is_updating = True
        
        # Rendering 
        if loop.is_updating:
            rl.begin_drawing()
            loop.current_scene.render()
            rl.end_drawing()
            loop.is_updating = False
            loop.is_drawing = True
            loop.fps_counter += 1
        
        # Do things each second
        if loop.accumulator_each_second >= 1.0:
            loop.accumulator_each_second -= 1.0
            loop.fps = loop.fps_counter
            loop.fps_counter = 0