"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

"""
from turtle import *
from random import randrange
from freegames import square, vector

class Head:
    def __init__(self,x=10,y=0):
        self.x = x
        self.y = y
        self.vector = vector(self.x, self.y)
        

class Food:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        self.vector = vector(x,y)
        
class Snake:
    
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        self.head = Head()
        self.body = []
        
        self.aim = self.Aim()
    class Aim:
        def __init__(self):
            self.x = 0
            self.y = -10
            self.vector = vector(self.x,self.y)
        

    def change(self,x, y):
        "Change snake direction."
        self.aim.x = x
        self.aim.y = y
    def move(self):
        "Move snake forward one segment." #Mova a cobra um segmento para frente
        self.head.vector = self.aim.vector
        self.head = self.head.vector[-1]

          
class GameSnake:

    def __init__(self):
        self.food = Food()
        self.snake = Snake()

    def inside(self,head):
        "Return True if head inside boundaries."
        return -200 < self.snake.head.x < 190 and -200 < self.snake.head.y < 190
    
    def on_collision_with_border(self):
        if(self.inside):
            pass    
        else:
            square(self.snake.head.x, self.snake.head.y, 9, 'red')# desenha um dradrado vermelho
            update()
            return    
    self.snake.append(head)

    if self.snake.head == food.vector:
        print('Snake:', len(snake))
        self.food.x = randrange(-15, 15) * 10 #novo X da comida no intervalo determinado
        self.food.y = randrange(-15, 15) * 10 #novo Y da comida no intervalo determinado
    else:
        self.snake.pop(0)

    clear()
    for body in self.snake.vector:
        square(self.snake.body.x, self.snake.body.y, 9, 'black')
        

class setup:
        
    setup(420, 420, 370, 0)
    hideturtle()
    tracer(False)
    listen()
    game = GameSnake()
    onkey(lambda: game.snake.change(10, 0), 'Right')
    onkey(lambda: game.snake.change(-10, 0), 'Left')
    onkey(lambda: game.snake.change(0, 10), 'Up')
    onkey(lambda: game.snake.change(0, -10), 'Down')
    game.snake.move()
    done()