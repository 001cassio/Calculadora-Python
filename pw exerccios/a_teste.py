import os, pyperclip
valor = pyperclip.paste()

local = os.path.abspath(".")
local2 = os.path.abspath("texto.txt")


print(local)
print(local2)
caminho = os.path.dirname(local)
caminho2 = os.path.basename(local)
print(caminho)
print(caminho2)

arquivo = open(local2,"a")
arquivo.write("ola mundo como vai as coisas")
arquivo.close()


arquivo = open(local2,"w")
arquivo.write(valor)
arquivo.close()

arquivo = open(local2)
print(arquivo.readline())

ola = arquivo

print(ola)