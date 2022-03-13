import turtle
import time
# creating the turtles of the game 
sc = turtle.Screen()
sc.title("msh 3arf")
sc.setup(height = 600 , width = 800)
sc.tracer(0)
sc.bgcolor("black")


stuffr1c1 = turtle.Turtle()
stuffr1c1.color("red")
stuffr1c1.shape("square")
stuffr1c1.shapesize(stretch_wid =5)
stuffr1c1.shapesize(stretch_len =2)
stuffr1c1.penup()
stuffr1c1.goto(-350,-250)



stuffr2c1 = turtle.Turtle()
stuffr2c1.color("red")
stuffr2c1.shape("square")
stuffr2c1.shapesize(stretch_wid =5)
stuffr2c1.shapesize(stretch_len = 2)
stuffr2c1.penup()
stuffr2c1.goto(-250,-250)


stuffr3c1 = turtle.Turtle()
stuffr3c1.color("red")
stuffr3c1.shape("square")
stuffr3c1.shapesize(stretch_wid =5)
stuffr3c1.shapesize(stretch_len = 2)
stuffr3c1.penup()
stuffr3c1.goto(-150,-250)


stuffr1c2 = turtle.Turtle()
stuffr1c2.color("red")
stuffr1c2.shape("square")
stuffr1c2.shapesize(stretch_wid =5)
stuffr1c2.shapesize(stretch_len =2)
stuffr1c2.penup()
stuffr1c2.goto(-350,-125)



stuffr2c2 = turtle.Turtle()
stuffr2c2.color("red")
stuffr2c2.shape("square")
stuffr2c2.shapesize(stretch_wid =5)
stuffr2c2.shapesize(stretch_len = 2)
stuffr2c2.penup()
stuffr2c2.goto(-250,-125)


stuffr3c2 = turtle.Turtle()
stuffr3c2.color("red")
stuffr3c2.shape("square")
stuffr3c2.shapesize(stretch_wid =5)
stuffr3c2.shapesize(stretch_len = 2)
stuffr3c2.penup()
stuffr3c2.goto(-150,-125)

stuffr1c3 = turtle.Turtle()
stuffr1c3.color("red")
stuffr1c3.shape("square")
stuffr1c3.shapesize(stretch_wid =5)
stuffr1c3.shapesize(stretch_len =2)
stuffr1c3.penup()
stuffr1c3.goto(-350,0)


stuffr2c3 = turtle.Turtle()
stuffr2c3.color("red")
stuffr2c3.shape("square")
stuffr2c3.shapesize(stretch_wid =5)
stuffr2c3.shapesize(stretch_len = 2)
stuffr2c3.penup()
stuffr2c3.goto(-250,0)


stuffr3c3 = turtle.Turtle()
stuffr3c3.color("red")
stuffr3c3.shape("square")
stuffr3c3.shapesize(stretch_wid =5)
stuffr3c3.shapesize(stretch_len = 2)
stuffr3c3.penup()
stuffr3c3.goto(-150,0)


stuffr1c4 = turtle.Turtle()
stuffr1c4.color("red")
stuffr1c4.shape("square")
stuffr1c4.shapesize(stretch_wid =5)
stuffr1c4.shapesize(stretch_len =2)
stuffr1c4.penup()
stuffr1c4.goto(-350,125)


stuffr2c4 = turtle.Turtle()
stuffr2c4.color("red")
stuffr2c4.shape("square")
stuffr2c4.shapesize(stretch_wid =5)
stuffr2c4.shapesize(stretch_len = 2)
stuffr2c4.penup()
stuffr2c4.goto(-250,125)

stuffr3c4 = turtle.Turtle()
stuffr3c4.color("red")
stuffr3c4.shape("square")
stuffr3c4.shapesize(stretch_wid =5)
stuffr3c4.shapesize(stretch_len = 2)
stuffr3c4.penup()
stuffr3c4.goto(-150,125)


stuffr1c5 = turtle.Turtle()
stuffr1c5.color("red")
stuffr1c5.shape("square")
stuffr1c5.shapesize(stretch_wid =5)
stuffr1c5.shapesize(stretch_len =2)
stuffr1c5.penup()
stuffr1c5.goto(-350,250)

stuffr2c5 = turtle.Turtle()
stuffr2c5.color("red")
stuffr2c5.shape("square")
stuffr2c5.shapesize(stretch_wid =5)
stuffr2c5.shapesize(stretch_len = 2)
stuffr2c5.penup()
stuffr2c5.goto(-250,250)

stuffr3c5 = turtle.Turtle()
stuffr3c5.color("red")
stuffr3c5.shape("square")
stuffr3c5.shapesize(stretch_wid =5)
stuffr3c5.shapesize(stretch_len = 2)
stuffr3c5.penup()
stuffr3c5.goto(-150,250)


#Racket
racket = turtle.Turtle()
racket.color("blue")
racket.shape("square")
racket.shapesize(stretch_wid = 5)
racket.shapesize(stretch_len = 1)
racket.penup()
racket.goto(360,0)

#Ball
sc.tracer(0)
ball = turtle.Turtle()
ball.color("white")
ball.shape("circle")
ball.penup()
ball.goto(340,0)
ball.dx = 0.5
ball.dy = 0.5

#Score
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("white")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("Life: 3",
             align="center", font=("Arial", 24, "bold"))

def hit_stuff(block):   # the rebound of the ball and braking the turtles
    global score
    if ball.xcor() < block.xcor()+40 and ball.xcor() > block.xcor()-40 and ball.ycor() < block.ycor()+40 and ball.ycor() > block.ycor()-40:
        ball.dx*=-1
        block.ht()
        block.goto(1000,1000)
        score += 1
       
        
def shoot_ball():
    time.sleep(1)
    ball.setx(340)
    ball.sety(racket.ycor())
         

def is_winner():
    global score
    if score == 15:
        sketch.clear()
        sketch.penup()
        sketch.ht()
        sketch.goto(0, 0)
        sketch.write('''Well Played...
  You Won!''',
             align="center", font=("Arial", 40, "bold"))
        return True
        
def moving_up():
    y = racket.ycor()
    y+=20
    racket.sety(y)
    
def moving_down () :
    y = racket.ycor()
    y-=20
    racket.sety(y)

sc.listen()
sc.onkeypress( moving_up , "Up" )
sc.onkeypress( moving_down , "Down" )

lives = 3
score = 0

while True:
    sc.update()
    if is_winner():
        break
        
    ball.sety(ball.ycor()+ball.dy)
    ball.setx(ball.xcor()+ball.dx)
    
    if racket.ycor() < -250:
        racket.sety(-250)
    if racket.ycor() > 250:
        racket.sety(250)
    if (ball.ycor()>290):
        ball.sety (290)
        ball.dy*=-1
    if( ball.ycor()<-290):
        ball.sety (-290)
        ball.dy*=-1
    if (ball.xcor()>390):
        shoot_ball()
        lives -= 1
        sketch.clear()
        sketch.write("Life: {}".format(lives),
             align="center", font=("Arial", 24, "bold"))
        if lives == 0:
            sketch.clear()
            sketch.penup()
            sketch.hideturtle()
            sketch.goto(0, 0)
            sketch.write('''Game Over...
  You Lost!''',
             align="center", font=("Arial", 40, "bold"))
            break
    if (ball.xcor()<-390):
        ball.dx*=-1
    if (ball.xcor()>350 )and(ball.xcor() <(370)and (ball.ycor()<racket.ycor()+40) and (ball.ycor()>racket.ycor()-40)): 
        ball.dx *= -1

        
    hit_stuff(stuffr1c1)
    hit_stuff(stuffr1c2)
    hit_stuff(stuffr1c3)
    hit_stuff(stuffr1c4)
    hit_stuff(stuffr1c5)
    hit_stuff(stuffr2c1)
    hit_stuff(stuffr2c2)
    hit_stuff(stuffr2c3)
    hit_stuff(stuffr2c4)
    hit_stuff(stuffr2c5)
    hit_stuff(stuffr3c1)
    hit_stuff(stuffr3c2)
    hit_stuff(stuffr3c3)
    hit_stuff(stuffr3c4)
    hit_stuff(stuffr3c5)
