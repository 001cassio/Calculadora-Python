from tkinter import *
from tkinter import font
from turtle import bgcolor


class aplicativo:
    def __init__(self):
        self.app = Tk()
        variavel = StringVar(self.app)
        cor1 ="#C4EEF2"
        cor2 ="#025951"
        cor3= "#7AB8BF"

        #estas duas partes serve para criar como se fosse uma div, primeria parte da tela e a segunda para os botoes, primero se cria este elemento pai e depois atribui os elementos filhos
        tela = Frame(self.app, width= 336, height=80, background="#04BFAD")
        tela.grid(row=0,column=0,)

        corpo= Frame(self.app, width=336, height=400, background=cor2)
        corpo.grid(column= 0, row=1)
        #VARIAVEL GLOBAL VAI RECEBER TODOS OS VALORES
        self.valores = ""
        #FUNCAO PARA MOSTRAR OS EVNTOS NA TELA
        def recebe_valor(event):
            self.valores = self.valores + str(event)
            variavel.set(self.valores)

        #esta funcao faz o calculo das operacoes e tambem trata erros de digitacao chamando outra funcao
        def calcula():
            try:
                resultado = eval(self.valores)
                variavel.set(resultado)
                self.valores = str(resultado)
            except:
                erro()

        #este serve para mostrar o erro ao usuario, limpando os valores recentes e mostrando a mensegem de erro ao usuario
        def erro():
            variavel.set("SINTAXE INVALIDA")
            self.valores =""

        #esta funcao apaga os valores na tela e tambem limpa as variaveis
        def apaga():
            self.valores =""
            variavel.set("")

        #este serve para criar uma janela dentro da parte da tela do app, para aprensentar os numeros
        visao = Label(master= tela, textvariable=variavel, width=23, height=3, anchor="e", justify=RIGHT, relief=FLAT, font=("ivy 18"), padx=7, bg=cor1)
        visao.place(x=0,y=0)



        #criando botoes, e referenciando as chamadas de funcoes com os valores dos botoes para que o evento seja mostrado na tela

        botao7 = Button(master= corpo,command=lambda:recebe_valor(7), text= 7,height=4,width=8,font=8,bg=cor3); botao7.place(x=0,y=71)

        botao4 = Button(master= corpo,text= 4,command=lambda:recebe_valor(4),height=4,width=8,font=8,bg=cor3); botao4.place(x=0,y=158)
        botao1 = Button(master= corpo,text= 1,command=lambda:recebe_valor(1),height=4,width=8,font=8,bg=cor3); botao1.place(x=0,y=245)
        botao0 = Button(master= corpo,text= 0,command=lambda:recebe_valor(0),height=4,width=22,bg=cor3); botao0.place(x=0,y=333)

        botao_C = Button(master= corpo,text= "C", command=apaga ,height=4,width=22,bg=cor3); botao_C.place(x=0,y=0)
        botao8 = Button(master= corpo,text= 8,command=lambda:recebe_valor(8),height=4,width=8,font=8,bg=cor3); botao8.place(x=84,y=71)
        botao5 = Button(master= corpo,text= 5,command=lambda:recebe_valor(5),height=4,width=8,font=8,bg=cor3); botao5.place(x=84,y=158)
        botao2 = Button(master= corpo,text= 2,command=lambda:recebe_valor(2),height=4,width=8,font=8,bg=cor3); botao2.place(x=84,y=245)
 
        botao_porcent = Button(master= corpo,text= "%",command=lambda:recebe_valor("%"),height=3,width=8,font=8,bg=cor3); botao_porcent.place(x=168,y=0)
        botao9 = Button(master= corpo,text= 9,command=lambda:recebe_valor(9),height=4,width=8,font=8,bg=cor3); botao9.place(x=168,y=71)
        botao6 = Button(master= corpo,text= 6,command=lambda:recebe_valor(6),height=4,width=8,font=8,bg=cor3); botao6.place(x=168,y=158)
        botao3 = Button(master= corpo,text= 3,command=lambda:recebe_valor("3"),height=4,width=8,font=8,bg=cor3); botao3.place(x=168,y=245)
        botao_ponto = Button(master= corpo,command=lambda:recebe_valor("."),text= ".",height=3,width=8,font=8,bg=cor3); botao_ponto.place(x=168,y=333)
    
        botao_div = Button(master= corpo,command=lambda:recebe_valor("/"),text= "/",height=3,width=8,font=7,bg=cor3); botao_div.place(x=252,y=0)
        botao_mais = Button(master= corpo,command=lambda:recebe_valor("+"),text= "+",height=4,width=8,font=8,bg=cor3); botao_mais.place(x=252,y=71)
        botao_menos = Button(master= corpo,command=lambda:recebe_valor("-"),text= "-",height=4,width=8,font=8,bg=cor3); botao_menos.place(x=252,y=158)
        botao_mult = Button(master= corpo,command=lambda:recebe_valor("*"),text= "x",height=4,width=8,font=8,bg=cor3); botao_mult.place(x=252,y=245)
        botao_igual = Button(master= corpo,command= calcula ,text= "=",height=3,width=8,font=8,bg=cor3); botao_igual.place(x=252,y=333)
        
        self.app.title("CALCULADORA PYTHON")
        self.app.geometry('336x480')
        self.app.resizable(height=0, width=0)
        self.app.mainloop()
        



app = aplicativo()


# made by: Vandercassio 