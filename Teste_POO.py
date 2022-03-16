
from cgitb import text
from tkinter import *
from turtle import onclick


class Calculadora:
    def __init__(self,num1, num2):
        self.num1 = num1
        self.num2 = num2

    def somar(self):
        resultado =self.num1 + self.num2
        print(resultado)

    def subtrair(self):
        resultado = self.num1 - self.num2
        print(resultado)
        
    def dividir(self):
        resultado = self.num1 / self.num2
        print(resultado)
     
    def multiplicar(self):
        resultado = self.num1 * self.num2
        print(resultado)
     
def simbolo(operacao, numero1, numero2):
    calcula = Calculadora(numero1, numero2)
    if operacao == 1:
        calcula.multiplicar()
    elif operacao ==2:
        calcula.somar()
    elif operacao == 3:
        calcula.dividir()
    elif operacao == 4:
        calcula.subtrair()
    else:
        print("digites valores ivalidos")

"""
print("-"*20)
operacao = int(input(print('''Digite o numero conforme a operacao que deseja fazer:
1 - Multiplicação
2 - Soma
3 - Divisao
4 - Subtração
''')))
print("-"*20)
num1 = int(input("Digite o primeiro valor do calculo:  "))
num2 = int(input("Digite o segundo  valor do calculo:  "))


#simbolo(operacao,num1,num2)

   """

class tela:
    def __init__ (self):
        self.app = Tk()
        self.valor = DoubleVar(self.app)
        self.soma = DoubleVar(self.app)
        
        front = Label(textvar = self.soma)
        front.grid()

        visor = Entry(master = self.app,textvar= self.valor)
        visor.grid()
        
        bt1 = Radiobutton(master=self.app, value="1", text="SOMAR")
        bt2 = Radiobutton(master=self.app, value="SUBTRAIR" ,text="SUBTRAIR"  )
        bt3 = Radiobutton(master=self.app, value="DIVIDIR" ,text="DIVIDIR")
        bt4 = Radiobutton(master=self.app, value="ADICIONAR", text="ADICIONAR")

        for i in (bt1,bt2,bt3,bt4): i.grid()

        def adicionando(e):
            self.soma.set(self.soma.get() + self.valor.get())

        botao = Button(master= self.app, text="CALCULAR" )
        botao.grid()
        botao.bind("<Button-1>", adicionando)


visor = tela()
visor.app.mainloop()
