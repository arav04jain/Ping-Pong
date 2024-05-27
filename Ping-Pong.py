# imports
import turtle
import time
import random as r
# import playsound

# screen
scr = turtle.Screen()
scr.bgcolor("black")
scr.screensize(600, 600)
scr.listen()
scr.tracer(0)

# score board
sb = turtle.Turtle()
sb.goto(0, 250)
sb.pencolor("white")
sb.hideturtle()
s = 0


# peddal setup
p = turtle.Turtle()
p.shape("square")
p.shapesize(stretch_len=5, stretch_wid=1)
p.color("green")
p.penup()
p.goto(0, -225)


# ball setup
b = turtle.Turtle()
b.shape("circle")
b.color("yellow")
b.penup()
b.goto(0, 225)
b.setheading(270)

# peddal move


def tleft():
    p.setheading(180)


def tright():
    p.setheading(0)


# forever loop
n = 0
scr.onkey(tleft, "Left")
scr.onkey(tright, "Right")
while n == 0:
    time.sleep(.001)
    p.forward((s/5)+3)
    if p.xcor() >= 300:
        p.goto(300, -225)
    if p.xcor() <= -300:
        p.goto(-300, -225)
    if b.ycor() >= 300:
        b.setheading(b.heading()-270)
    if b.xcor() >= 300:
        b.setheading(b.heading()-270)
    if b.xcor() <= -300:
        b.setheading(b.heading()-270)
    if b.distance(p) < 50:

        s += 1
        b.setheading(r.randrange(45, 135))
        b.forward(s+5)

        time.sleep(.01)

        # playsound.playsound("C:\\Users\\DELL\\OneDrive\\Desktop\\ARAV JAIN\\pong_sound.wav")

    if b.ycor() <= -300:
        n = 1
    sb.clear()
    sb.write(s, move=False, align="center", font=("Arial", 20, "normal"))

    b.forward(3+(s/5))
    scr.update()


scr.exitonclick()
