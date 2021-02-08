"""Snake, classic arcade game.

Exercises

1. How do you make the SnakeFast or SnakeSlow classes?
2. How do you make a SnakeSmart, that change the direction when collide with edges?
3. How would you make a new food types? When snake eat them it will more fast or decrease?
4. How do you create a Actor that will be the Head and Food superclass?
"""

from turtle import setup, hideturtle, tracer, listen, onkey, done, update, clear, ontimer
from random import randrange, choice
from freegames import square, vector

# 4. How do you create a Actor that will be the Head and Food superclass?
class Actor:
    def __init__(self, x, y):
        self.position = vector(x, y)

    @property
    def x(self):
        return self.position.x

    @property
    def y(self):
        return self.position.y

class Head(Actor):
    pass

class Food(Actor):
    color = 'Blue'
    cal = 5

#3. How would you make a new food types? When snake eat will more fast or decrease?
class Apple(Food):
    color = 'Green'
    cal = 10

class Mouse(Food):
    color = 'Brown'
    cal = 15

class BadFood(Food):
    color = 'Red'
    cal = -5

class Snake:
    SPEED = 1
    def __init__(self, x=0, y=0):
        self.head = Head(x, y)
        self.body = [vector(10, 0)]
        self.aim = vector(0*self.SPEED, -10*self.SPEED)
        self.direction = "SOUTH"

        self.status = 'LIVE'

    def eat(self, food):
        print('snake is eating', food.cal)
        for x in range(food.cal):
            self.body.append(self.head.position)

        for x in range(food.cal, 0):
            del self.body[0]

    def move(self):
        "Move snake forward one segment."
        self.head = Head(*self.body[-1].copy())
        self.head.position.move(self.aim)

        if self.is_colliding_with_border():
            self.on_collision_with_border()
        elif self.is_eating_himself():
            self.on_eating_himself()
        else:
            self.body.append(self.head.position)
            self.body.pop(0) # cut the tail

    def on_collision_with_border(self):
        self.dead()

    def on_eating_himself(self):
        self.dead()

    def is_eating_himself(self):
        #print(self.head.position, self.body)
        return (self.head.position in self.body)

    def dead(self):
        self.status = 'DEAD'

    def alive(self):
        return self.status != 'DEAD'

    def is_colliding_with_border(self):
       return not(-200 < self.head.x < 190 and -200 < self.head.y < 190)
    
    def left(self):
        if self.direction == "NORTH" :
            self.aim.x = -10*self.SPEED
            self.aim.y = 0*self.SPEED

        elif self.direction == "SOUTH":
            self.aim.x = 10*self.SPEED
            self.aim.y = 0*self.SPEED


        elif self.direction == "WEST" :
            self.aim.x = 0*self.SPEED
            self.aim.y = -10*self.SPEED
            
        elif self.direction == "EAST":
            self.aim.x = 0*self.SPEED
            self.aim.y = 10*self.SPEED

        

    def right(self):
        if self.direction == "NORTH" :
            self.aim.x = 10*self.SPEED
            self.aim.y = 0*self.SPEED

        elif  self.direction == "SOUTH":
            self.aim.x = -10*self.SPEED
            self.aim.y = 0*self.SPEED

        elif self.direction == "WEST" :
            self.aim.x = 0*self.SPEED
            self.aim.y = 10*self.SPEED

        elif self.direction == "EAST":
            self.aim.x = 0*self.SPEED
            self.aim.y = -10*self.SPEED

    
'''    def up (self):
        self.aim.x = 0*self.SPEED
        self.aim.y = 10*self.SPEED
        print('snake is changing ',self.direction)
    
    def dowm (self):
        self.aim.x = 0*self.SPEED
        self.aim.y = -10*self.SPEED
        print('snake is changing ',self.direction) '''
        
# 1. How do you make the SnakeFast or SnakeSlow classes?
class SnakeFast(Snake):
    SPEED = 2

class SnakeSlow(Snake):
    SPEED = 0.5

#2. How do you make a SnakeSmart, that change the direction when collide with edges?
class SnakeSmart(Snake):
    def on_collision_with_border(self):
        self.change(10, 0)

class GameSnake:
    def __init__(self):
        self.food = self.new_food()
        self.snake = Snake()

        onkey(lambda: self.on_rightkeypressed() , 'Right')
        onkey(lambda: self.on_leftkeypressed(), 'Left')
        onkey(lambda: self.on_upkeypressed(), 'Up')
        onkey(lambda: self.on_downkeypressed(), 'Down')

    #EAST
    def on_rightkeypressed(self):
        if self.snake.direction == 'NORTH':
            self.snake.right()
            self.snake.direction = "EAST"
            
        elif self.snake.direction == "SOUTH":
            self.snake.left()
            self.snake.direction = "EAST"
    
        print('snake is changing ',self.snake.direction)
    
    #WEST
    def on_leftkeypressed(self):
        if self.snake.direction == 'NORTH':
            self.snake.left()
            self.snake.direction = "WEST"
            
        elif self.snake.direction == "SOUTH":
            self.snake.right()
            self.snake.direction = "WEST"
        
        print('snake is changing ',self.snake.direction)    
            
    #NORTH
    def on_upkeypressed(self):
        if self.snake.direction == 'WEST':
            self.snake.right()
            self.snake.direction = "NORTH"
            
        elif self.snake.direction == "EAST":
            self.snake.left()
            self.snake.direction = "NORTH"

        print('snake is changing ',self.snake.direction)
    
    #SOUTH
    def  on_downkeypressed (self):
        if self.snake.direction == 'WEST':
            self.snake.left()
            self.snake.direction = "SOUTH"

        elif self.snake.direction == "EAST":
            self.snake.right()
        self.snake.direction = "SOUTH"
        print('snake is changing ',self.snake.direction)
    
    def new_food(self):
        foods = [Food,
                Apple,
                Mouse,
                BadFood,
                ]
        type_food = choice(foods)
        food = type_food(0, 0)
        food.position = vector(randrange(-15, 15) * 10, randrange(-15, 15) * 10)
        return food

    def run(self):
        clear()
        for body in self.snake.body:
            square(body.x, body.y, 9, 'black')
        square(self.food.x, self.food.y, 9, self.food.color)
        update()

        self.snake.move()

        if self.snake.head.position == self.food.position:
            self.snake.eat(self.food)
            self.food = self.new_food()

        if self.snake.alive():
            ontimer(self.run, 100)
        else:
            print('>>> SNAKE IS DEAD <<<')
            square(self.snake.head.x, self.snake.head.y, 9, 'red')
            return

def init():
    setup(420, 420, 370, 0)
    hideturtle()
    tracer(False)
    listen()
    game = GameSnake()
    game.run()
    done()

if __name__ == '__main__':
    init()
