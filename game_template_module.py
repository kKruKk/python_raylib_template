
import pyray as rl 
import loop_module

class Game:
    def __init__(self,loop : loop_module.Loop_Data):
        self.loop = loop
        
    def input(self):
        pass 

    def update(self,t : float, dt : float ):
        pass

    def render(self):
        rl.begin_drawing()
        rl.clear_background(rl.RAYWHITE)
        
        
        text = str(self.loop.fps)
        rl.draw_text(text,10,10,30,rl.GREEN)
        rl.end_drawing()
