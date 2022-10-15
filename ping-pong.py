import turtle

wind = turtle.Screen()
wind.title("ping pong py mo7amed ayad")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)
#when i tracer(0) this give me best control so that there is no update 


#madrad_1
madrab1 = turtle.Turtle()
madrab1.speed(0)#these is the max speed
madrab1.shape("square") #these is the its shape
madrab1.color("blue")
madrab1.shapesize(stretch_wid=5, stretch_len=1)
madrab1.penup()
madrab1.goto(-360,0)

#madrab2

madrab2= turtle.Turtle()
madrab2.speed(0)#these is the max speed
madrab2.shape("square") #these is the its shape
madrab2.color("red")
madrab2.shapesize(stretch_wid=5, stretch_len=1)
madrab2.penup()
madrab2.goto(360,0)

#ball

ball = turtle.Turtle()
ball.speed(0)#these is the max speed
ball.shape("circle") #these is the its shape
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.5
ball.dy = 0.5


#score
score_1 = 0
score_2 = 0
score = turtle.Turtle()
score.shape("circle") #these is the its shape
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("player 1 : 0 player 2 : 0", align="center",font=("Open Sans",24,"normal" ))



def madrab1_up():
    y = madrab1.ycor()
    y += 20
    madrab1.sety(y)

def madrab1_down():
    y = madrab1.ycor()
    y -= 20
    madrab1.sety(y)


def madrab2_up():
    y = madrab2.ycor()
    y += 20
    madrab2.sety(y)

def madrab2_down():
    y = madrab2.ycor()
    y -= 20
    madrab2.sety(y)


wind.listen()
wind.onkeypress(madrab1_up,"")
wind.onkeypress(madrab1_down,"s")
wind.onkeypress(madrab2_up,"Up")
wind.onkeypress(madrab2_down,"Down")


while True:
    wind.update() #updateing the scren eny time
    ball.setx(ball.xcor() + ball.dx)
    #I take the ball's current location and give it 2.5 What is the speed you set
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *=-1

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor()>390:
        ball.goto(0 , 0)
        ball.dx *= -1
        score_1 += 1
        score.clear()
        score.write("player 1 : {} player 2 : {}".format(score_1,score_2), align="center", font=("Open Sans", 24, "normal"))

    if ball.xcor() <-390:
        ball.goto(0 , 0)
        ball.dx *= -1
        score_2 += 1
        score.clear()
        score.write("player 1 : {} player 2 : {}".format(score_1,score_2), align="center", font=("Open Sans", 24, "normal"))

    if (ball .xcor() > 350  and ball.xcor() < 360) and (ball.ycor() < madrab2.ycor() + 40 and ball.ycor() > madrab2.ycor()-40):
        ball.setx(350)
        ball.dx *= -1

    if (ball .xcor() < -350  and ball.xcor() > -360) and (ball.ycor() < madrab1.ycor() + 40 and ball.ycor() > madrab1.ycor()-40):
        ball.setx(-350)
        ball.dx *= -1



