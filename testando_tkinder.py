from tkinter import *

'''
#este e uma classe que 
class aplicacao(Frame):
    def __init__(self, master = None):
        Frame.__init__(self,master)
        self.msg = Label(self, text ="ola mundo")
        self.msg.pack()
        self.bye = Button(self, text="sair", command= self.quit).pack()
        self.pack()

app = aplicacao()
mainloop()
'''
'''

#este codigo abaixo espande por toda a tela e mapea onde o maouse foi clicado e qual botao foi apertado no teclado
def clica (e):
    txt = "Mouse clicado em\n%d,%d"%(e.x,e.y)
    r.configure(text=txt)
    r.focus()
def tecla(e):
    txt="Keysym=%s\nKeycode=%s\nChar=%s"%(e.keysym,e.keycode,e.char)
    r.configure(text=txt)
r = Label()
r.pack(expand=True, fill="both")
r.master.geometry("200x200")
r.bind("<Button-1>", clica)
r.bind("<Key>", tecla)
r.mainloop()]


'''