import datetime
from tkinter import *
data_pesquisa = {}
data_h
def dias_atuais():
    dia = int(input("Digite o Dia: ")) 
    mes = int(input("Digite o Mes: ")) 
    ano = int(input("Digite o Ano: ")) 

    global(data_pesquisa) = datetime.datetime(ano,mes,dia)
    global(data_hoje) = data_pesquisa.today()

def calcula_timer():

    resultado = dias_atuais.data_pesquisa.date() - dias_atuais.data_hoje.date()

    if resultado.days:
        print("Faltam %s dias para a data especificada" %(resultado.days))
    else:     
        print("Faltam %s dias para a data especificada" %(resultado.days*(-1)))


janela = Tk()
hoje = datetime.datetime().today()
hoje2 = Label(janela, text= hoje).grid(column=0 , row= 0)








janela.mainloop()
