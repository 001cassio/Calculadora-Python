from tkinter import *
from turtle import right

def abrir(): print("abrir")
def salvar(): print("salvar")
def ajuda(): print("ajuda")

top = Tk()
#este menu esta na configuracao de menu e localizado no topo da pagnina
principal = Menu(top)
#ao que parece se cria um menu e o chama e faz ele fazer referencia a quem o chamou, e adinciona comando ao menu atraves do ADD 
opcoes = Menu(principal)

#este dois comando aparecem como opcoes e executam outra funcao
opcoes.add_command(label = "Abrir", command= abrir)
opcoes.add_command(label = "Salvar", command= salvar)

#foi adicinado ao menu principa essas duas opces, uma chama outru menu e outra apenas um funcao
principal.add_cascade(label= "Opcoes", menu=opcoes)
principal.add_command(label= "Ajuda", command= ajuda)


#1 primeiro se instacia e chama a janela com um menu
top.configure(menu= principal)
top.mainloop()

