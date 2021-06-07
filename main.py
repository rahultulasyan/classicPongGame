# Default module
import turtle
import winsound

# A window creation
w = 800
h = 600
wn = turtle.Screen()
wn.title("Classic Pong", )
wn.bgcolor("lightBlue")
wn.setup(width=w, height=h)
wn.tracer(0)  # Switching off automatic update of the window; because auto update makes it slow

# ScoreBoard
score_a = 0
score_b = 0

# Paddle A
pad_a = turtle.Turtle()
pad_a.speed(0)  # Not the speed of paddle movement on screen, rather it is speed of animation
pad_a.shape("square")  # Default size is 20px by 20px
pad_a.shapesize(stretch_wid=5, stretch_len=1)  # make width 5 times the default, and len 1 times the default
pad_a.color("darkBlue")
pad_a.penup()
pad_a_offset = 50
pad_a_x = -((w // 2) - pad_a_offset)
pad_a.goto(pad_a_x, 0)

# Paddle B
pad_b = turtle.Turtle()
pad_b.speed(0)  # Not the speed of paddle movement on screen, rather it is speed of animation
pad_b.shape("square")  # Default size is 20px by 20px
pad_b.shapesize(stretch_wid=5, stretch_len=1)
pad_b.color("darkBlue")
pad_b.penup()
pad_b_offset = 50
pad_b_x = ((w // 2) - pad_b_offset)
pad_b.goto(pad_b_x, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)  # Not the speed of paddle movement on screen, rather it is speed of animation
ball.shape("circle")  # Default size is 20px by 20px
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.color("darkGreen")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15  # Delta change in ball x-axis (unit px)
ball.dy = 0.15  # Delta change in ball y-axis (unit px)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("Red")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Player A: {score_a}   Player B: {score_b}", align="center", font=("Courier", 24, "bold"))


# Functions
def pad_a_up():
    y = pad_a.ycor()
    y += 30
    pad_a.sety(y)


def pad_a_down():
    y = pad_a.ycor()
    y -= 30
    pad_a.sety(y)


def pad_b_up():
    y = pad_b.ycor()
    y += 30
    pad_b.sety(y)


def pad_b_down():
    y = pad_b.ycor()
    y -= 30
    pad_b.sety(y)


# Keyboard Binding
wn.listen()
wn.onkeypress(pad_a_up, "w")
wn.onkeypress(pad_a_down, "s")
wn.onkeypress(pad_b_up, "Up")  # Up Arrow Key
wn.onkeypress(pad_b_down, "Down")  # Down Arrow Key

# Main Game Loop
while True:

    wn.update()  # Manually updating the window; faster than auto update

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking

    # Top Border
    if ball.ycor() > (h // 2) - 10:
        ball.sety((h // 2) - 10)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # Bottom Border
    if ball.ycor() < -((h // 2) - 10):
        ball.sety(-((h // 2) - 10))
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # Right Border
    if ball.xcor() > (w // 2) - 10:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}   Player B: {score_b}", align="center", font=("Courier", 24, "bold"))
        winsound.PlaySound("bell.wav", winsound.SND_ASYNC)

    # Left Border
    if ball.xcor() < -((w // 2) - 10):
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}   Player B: {score_b}", align="center", font=("Courier", 24, "bold"))
        winsound.PlaySound("bell.wav", winsound.SND_ASYNC)  # play the sound asynchronously

    # Ball Collision with Paddle

    # Collision with Right Paddle
    if (340 < ball.xcor() < 350) and (pad_b.ycor() + 40 > ball.ycor() > pad_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    # Collision with Left Paddle
    if (-340 > ball.xcor() > -350) and (pad_a.ycor() + 40 > ball.ycor() > pad_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
