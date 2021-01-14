"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.
"""

from turtle import setup, hideturtle, tracer, listen, onkey, done, update, clear, ontimer
from random import randrange, choice
from freegames import square, vector

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
    def __init__(self, x=0, y=0):
        self.head = Head(x, y)
        self.body = [vector(10, 0)]
        self.aim = vector(0, -10)

    def eat(self, food):
        print('snake is eating', food.cal)
        for x in range(food.cal):
            self.body.append(self.head)

    def change(self, x, y):
        "Change snake direction."
        print('snake is changing')
        self.aim.x = x
        self.aim.y = y

    def move(self):
        "Move snake forward one segment."
        self.head = self.body[-1].copy()
        self.head.move(self.aim)

        self.body.append(self.head)
        self.body.pop(0)

class GameSnake:
    def __init__(self):
        self.food = self.new_food()
        self.snake = Snake()

        onkey(lambda: self.snake.change(10, 0), 'Right')
        onkey(lambda: self.snake.change(-10, 0), 'Left')
        onkey(lambda: self.snake.change(0, 10), 'Up')
        onkey(lambda: self.snake.change(0, -10), 'Down')

    def new_food(self):
        food = choice((Food(x=0, y=0), Apple(x=0, y=0), Mouse(x=0, y=0)))
        food.position = vector(randrange(-15, 15) * 10, randrange(-15, 15) * 10)
        return food

    def on_collision_with_border(self):
       return not(-200 < self.snake.head.x < 190 and -200 < self.snake.head.y < 190)

    def run(self):
        clear()
        for body in self.snake.body:
            square(body.x, body.y, 9, 'black')
        square(self.food.x, self.food.y, 9, self.food.color)
        update()

        self.snake.move()

        if self.snake.head == self.food.position:
            self.snake.eat(self.food)
            self.food = self.new_food()

        if self.on_collision_with_border():
            print('collide with border. game over.')
            square(self.snake.head.x, self.snake.head.y, 9, 'red')
            update()
            return
        else:
            ontimer(self.run, 100)

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
