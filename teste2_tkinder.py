from tkinter import *

def ola(): print("ola mundo")
def opcoes(): print("olaaa")

app = Tk()

menu_superior = Menu(app)

menu_inferior = Menu(menu_superior, tearoff=0)

menu_pop = Menu(menu_superior, tearoff=0)

menu_pop.add_command(label="deu ceerrot", command=ola)



menu_superior.add_cascade(label="Inicio", menu = menu_pop)
menu_superior.add_cascade(label="Opcoes",  menu = menu_inferior)

menu_inferior.add_command(label="deu certo", command= ola)

tela = Frame(app, width= 400, height= 300)

tela.pack()
app.configure(menu = menu_superior)



app.mainloop()