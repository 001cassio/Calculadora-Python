import turtle

color=["DarkRed","red","yellow","blue","indigo","spring green","orchid"]



oii = turtle.Turtle()


oii.speed(0)



oii.pensize(2)

x = 100
#ola.pencolor("light steel blue")
for y in range(150,550):
    for i in range(6):
        
        oii.pencolor(color[i])
        oii.fd(y)
        oii.lt(229-2)
        y += 20
        
        


turtle.mainloop()
