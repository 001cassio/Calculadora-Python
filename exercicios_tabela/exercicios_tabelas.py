import pyperclip
lista_len = {}
tabela ={}

lista = pyperclip.paste()
lista2 = lista.split()
print(lista2)
print(len(lista2))

for i in range(len(lista2)):
    tabela[len(lista2[i])] = lista2[i]
tabela2 = sorted(tabela)
print(tabela2)
if round(len(lista) / len(lista2)) % 2 ==0:
    while True:
        i = 0
        x = -1
        tabela_pre = (tabela2[i], tabela2[x])
        i += 1
        x -=1
        if i > (len(tabela2)):
            break
else:
    while True:
        i = 0
        x = -1
        tabela_pre = (tabela2[i], tabela2[x])
        i += 1
        x -=1
        if i > (len(tabela2)):
            break
