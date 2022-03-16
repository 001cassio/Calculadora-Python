import turtle


t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor("black")


t.pencolor("yellow")
t.speed(0)

for i in range(150):
    t.circle(10)
    t.fd(30)
    t.rt(101)
    t.circle(90)
    if i == 25:
        t.pencolor("green")
    if i == 50:
        t.pencolor("blue")
    if i == 100:
        t.pencolor("magenta")
        

turtle.mainloop()