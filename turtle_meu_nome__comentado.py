import turtle

tartaruga = turtle.Turtle()
#este comando faz virar a direita
tartaruga.rt(90)
#este comando determina a velocidade que se desenha
tartaruga.speed(8)
#este comando nao deixa a caneta riscar
tartaruga.pu()

#estes trecho e uma tupla que contem a familia o tamanho e o tipo da fonte
fonte1 = ("Comic Sans", 40, "normal")
#este comando escreve na tela o primeiro argumento, se o segundo for true ou false ele
#percorre as pavaras e o ultimo e a variavel com o tipo da letra
tartaruga.write("Vandercassio",False, "center", fonte1)

#este comando salta para baixo para escrever mais
tartaruga.fd(40)
#esta tupla tem a mesma funcao da tupla acima
fonte2 = ("Comic Sans", 20, "normal")
#esta funcao tem o mesmo valor da funcao acima

tartaruga.write("de", False, "center", fonte2)
#salta para baixo
tartaruga.fd(40)

fonte3 = ("Comic Sans", 30, "bold")
tartaruga.write("Oliveira", True, "center", fonte3)
#este comando retorna o cursor para o centro

tartaruga.home()
#este comando volta a riscar com o cursor
tartaruga.pd()
#este comando diz a cor que a caneta vai riscar
tartaruga.pencolor("LightSkyBlue")
#este comando diz o grossura que a caneta vai riscar
tartaruga.pensize(10)

#este comando avanca pra frente
tartaruga.fd(200)
#vira a esquerda 90 graus
tartaruga.lt(90)
#risca pra frente
tartaruga.fd(80)
#vira a esquerda 90 graus
tartaruga.lt(90)
#risca pra frente
tartaruga.fd(400)
#vira a esquerda 90 graus
tartaruga.lt(90)

tartaruga.fd(80)

tartaruga.lt(90)
tartaruga.fd(200)
#este comando nao deixa a caneta riscar
tartaruga.pu()

tartaruga.home()
#este comando move o cursor no eixo y 
tartaruga.sety(-250)
tartaruga.pd()
tartaruga.pensize(3)
tartaruga.pencolor("blue")
#este comando faz um circulo
tartaruga.circle(250)

#este comado cptura a tela, recomendo usar no final pois perde um pouco
#das funcoes 
tartaruga = turtle.Screen()
#este comanddo muda a cor de fundo, de primeira so consegui usar depois de usar
#0 screen o que limita as funcoes
tartaruga.bgcolor("DeepSkyBlue")

#este comando faz com que o programa execute e fique aguardando o usuario
tartaruga.mainloop()
