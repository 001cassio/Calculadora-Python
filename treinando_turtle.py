import turtle

t = turtle.Turtle()
#obtem a tela para definir uma cor de fundo
s = turtle.Screen()
s.bgcolor("black")

t.pencolor("red")
color=["blue","red","pink","purple","yellow","DeepSkyBlue","Goldenrod"]
t.speed(0)
#este codigo va gerer uma especie de flor com cores difrentes e conforme passa o fundo tambem altera sua cor
for x in range(len(color)):
    for i in range(len(color)):
        t.begin_fill()
        t.fillcolor(color[i])
        t.circle(150 ,100)
        t.lt(90)
        t.circle(150,100)
        t.rt(90)
        t.end_fill()
    s.bgcolor(color[x])
t.clear()
s.clear()


turtle.mainloop()
