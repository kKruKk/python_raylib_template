
import pyray as rl 
import loop_module

import game_template_module as scene

class Game:
    def __init__(self,loop : loop_module.Loop_Data):
        self.loop = loop
        self.screen_width : int = rl.get_screen_width()
        self.screen_height : int = rl.get_screen_height()

        self.player : Entity = Entity(64,64,100,100,200)
        self.squares : list[Entity] = []

        for i in range(500):
            self.squares.append(
                Entity(
                    8,8,
                       rl.get_random_value(50,self.screen_width - 50),
                       rl.get_random_value(50,self.screen_height - 50),
                       rl.get_random_value(10,100)
                       )
                       )
            
            self.squares[i].color = rl.Color(rl.get_random_value(64,255),rl.get_random_value(64,255),rl.get_random_value(64,255),255)


    def input(self):
        self.player.direction = [0.0,0.0]

        if rl.is_key_down(rl.KEY_E):
            self.player.direction[1] = -1
        if rl.is_key_down(rl.KEY_D):
            self.player.direction[1] = 1
        if rl.is_key_down(rl.KEY_W):
            self.player.direction[0] = -1
        if rl.is_key_down(rl.KEY_S):
            self.player.direction[0] = 1  

    def update(self,t : float, dt : float ):
        Entity.update_position(self.player,dt)
        Entity.border_teleport(self.player,self.screen_width,self.screen_height)

        for item in self.squares:
            item.direction[0] += float(rl.get_random_value(-100,100)) 
            item.direction[1] += float(rl.get_random_value(-100,100))

            Entity.update_position(item,dt)
            Entity.border_teleport(item,self.screen_width,self.screen_height)

        # change scane
        # if self.player.x > 400:
        #     self.loop.current_scene = scene.Game(self.loop)

    def render(self):
        
        rl.clear_background(rl.ORANGE)
        
        for i in self.squares:
            Entity.draw(i)

        Entity.draw(self.player)
        
        text = str(self.loop.fps)
        rl.draw_text(text,10,10,30,rl.GREEN)

       




class Entity:
    def __init__(self,width = 32,height = 32,x : float = 0,y : float = 0,speed = 10):
        self.width : int = width
        self.height : int = height
        self.x : float = x
        self.y : float = y
        self.speed : float = speed
        self.direction : list[float] = [0.0,0.0]
        self.color = rl.Color(64,255,128,255)

    def draw(self):
        rl.draw_rectangle(int(self.x),int(self.y),self.width,self.height,self.color)

    def update_position(self,dt : float):
        v = rl.vector2_normalize(self.direction)
       
        self.x += v.x * self.speed * dt
        self.y += v.y * self.speed * dt

    def border_teleport(self,screen_width : int,screen_height : int):

        if self.x < 0.0:
            self.x = float(screen_width - self.width) 

        if self.x + self.width > screen_width:
            self.x = 1.0 

        if self.y < 0.0:
            self.y = float(screen_height - self.height)

        if self.y + self.height > screen_height:
            self.y = 0.0    