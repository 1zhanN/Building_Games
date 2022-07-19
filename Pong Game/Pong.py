import turtle

win = turtle.Screen()                   # importing gui module
win.title("PONG")            # creating a window
win.bgcolor("black")
win.setup(width=800, height=600)        # size of the window
win.tracer(0)                           # stops the window from updating (efficiency)

# score
score_a = 0
score_b = 0

# paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(0)                       # speed of animation (max)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid= 5, stretch_len= 1)
paddle_a.penup()
paddle_a.goto(-350, 0)


# paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)                       # speed of animation (max)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid= 5, stretch_len= 1)
paddle_b.penup()
paddle_b.goto(350, 0)


# Ball

ball = turtle.Turtle()
ball.speed(0)                           # speed of animation (max)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)

ball.dx = 0.23                          # ball movement by 2 pixels
ball.dy = 0.23

# pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player One: 0 Player Two: 0", align="center", font=("Courier", 24, "normal"))

# function

def paddle_a_up():
    y = paddle_a.ycor()             # returns the 'y' coordinate
    y += 20                         # adds 20 pixels to the current y pos
    paddle_a.sety(y)                # set the new value to the 'y' coordinate


# function

def paddle_a_down():
    y = paddle_a.ycor()             # returns the 'y' coordinate
    y -= 20                         # subtract 20 pixels to the current y pos
    paddle_a.sety(y)                # set the new value to the 'y' coordinate

# function

def paddle_b_up():
    y = paddle_b.ycor()             # returns the 'y' coordinate
    y += 20                         # adds 20 pixels to the current y pos
    paddle_b.sety(y)                # set the new value to the 'y' coordinate


# function

def paddle_b_down():
    y = paddle_b.ycor()             # returns the 'y' coordinate
    y -= 20                         # subtract 20 pixels to the current y pos
    paddle_b.sety(y)                # set the new value to the 'y' coordinate

# keyboard binding

win.listen()                                # listens for keyboard inputs
win.onkeypress(paddle_a_up, "w")            # call the function on pressing desired keys
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

# main game loop
while True:
    win.update()                            # updates the screen


    # moving the ball

    ball.setx(ball.xcor() + ball.dx)        # ( current ball coordinate + 0.2)
    ball.sety(ball.ycor() + ball.dy)
    # border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1                       # reverse direction on axis
        score_a += 1
        pen.clear()
        pen.write("Player One: {} Player Two: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player One: {} Player Two: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

# paddle collision
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
