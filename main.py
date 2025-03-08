import pyray as rl 
import time as time

rl.set_random_seed(int(time.perf_counter()))

class Entity:
    def __init__(self,width,height,x,y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.speed = 10
        self.direction = [0.0,0.0]
        self.color = rl.Color(64,255,128,255)

    def draw(self):
        rl.draw_rectangle(self.x,self.y,self.width,self.height,self.color)

    def update_position(self):
        normalized = rl.vector2_normalize(self.direction)
        v = rl.vector2_scale(normalized,self.speed)
        self.x = int(float(self.x) + v.x)
        self.y = int(float(self.y) + v.y)

    def border_teleport(self,x,y):
        if self.x < 0:
            self.x = x 
        if self.x > x:
            self.x = 0 
        if self.y < 0:
            self.y = y 
        if self.y > y:
            self.y = 0             

player = Entity(64,64,100,100)

squares = []
for i in range(1000):
    squares.append(Entity(8,8,rl.get_random_value(50,750),rl.get_random_value(50,550)))
    squares[i].color = rl.Color(rl.get_random_value(64,255),rl.get_random_value(64,255),rl.get_random_value(64,255),255)
    squares[i].speed = 4

rl.init_window(800,600,"python raylib")
rl.set_target_fps(60)

while not rl.window_should_close():

    #input
    player.direction = [0,0]
    if rl.is_key_down(rl.KEY_E):
        player.direction[1] = -1
    if rl.is_key_down(rl.KEY_D):
        player.direction[1] = 1
    if rl.is_key_down(rl.KEY_W):
        player.direction[0] = -1
    if rl.is_key_down(rl.KEY_S):
        player.direction[0] = 1        

    #update
    Entity.update_position(player)

    for item in squares:
        item.direction[0] += (rl.get_random_value(0,100) - 50) 
        item.direction[1] += (rl.get_random_value(0,100) - 50)
        Entity.update_position(item)
        Entity.border_teleport(item,rl.get_screen_width(),rl.get_screen_height())



    #drawing
    rl.begin_drawing()
    rl.clear_background(rl.ORANGE)
    
    for i in squares:
        Entity.draw(i)

    Entity.draw(player)
    rl.draw_fps(10,10)

    rl.end_drawing()

rl.close_window()    