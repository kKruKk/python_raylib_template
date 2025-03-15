
import pyray as rl 

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


class Game:
    def __init__(self,screen_width : int,screen_height : int):
        self.screen_width : int = screen_width
        self.screen_height : int = screen_height

        self.player : Entity = Entity(64,64,100,100,200)
        self.squares : list[Entity] = []

        for i in range(1000):
            self.squares.append(
                Entity(
                    8,8,
                       rl.get_random_value(50,self.screen_width - 50),
                       rl.get_random_value(50,self.screen_height - 50),
                       rl.get_random_value(10,100)
                       )
                       )
            
            self.squares[i].color = rl.Color(rl.get_random_value(64,255),rl.get_random_value(64,255),rl.get_random_value(64,255),255)

game = Game(rl.get_screen_width(),rl.get_screen_height())    

def input():
    game.player.direction = [0.0,0.0]

    if rl.is_key_down(rl.KEY_E):
        game.player.direction[1] = -1
    if rl.is_key_down(rl.KEY_D):
        game.player.direction[1] = 1
    if rl.is_key_down(rl.KEY_W):
        game.player.direction[0] = -1
    if rl.is_key_down(rl.KEY_S):
        game.player.direction[0] = 1  

def update(dt : float ):
    Entity.update_position(game.player,dt)
    Entity.border_teleport(game.player,game.screen_width,game.screen_height)

    for item in game.squares:
        item.direction[0] += float(rl.get_random_value(-100,100)) 
        item.direction[1] += float(rl.get_random_value(-100,100))

        Entity.update_position(item,dt)
        Entity.border_teleport(item,game.screen_width,game.screen_height)


def render(dt : float, fps : int ):
    rl.begin_drawing()
    rl.clear_background(rl.ORANGE)
    
    for i in game.squares:
        Entity.draw(i)

    Entity.draw(game.player)
    text = str(fps)
    
    rl.draw_text(text,10,10,30,rl.GREEN)

    rl.end_drawing()