from mimetypes import init
import os, re

#este codigo todo cagado percorre o local que ele esta atras de arquivos txt existntes, e dentro dos txt ele busca um numero ne telefone, ainda falta muito pra ficar bom, mas ja e uma base
# feito e melhor que prefeito

local = os.path.abspath(".")
print(local)
arquivos = os.listdir(local)

def pasta_nova(pasta):
    for i in pasta:
        if ".txt" in i and os.path.exists(i):   
            lendo_pasta = open(i)
            lido = lendo_pasta.read()
            print(lido)
            procura(lido)

def procura(valor):
    numero = re.compile(r"\d\d\d\d\d\d\d\d")
    resultado = numero.search(str(valor))
    print(valor)
    print(resultado)
    print("acabou")        



for i in arquivos:
    if os.path.isfile(i) and ".txt" in i:
        lendo = open(i)
        lendo.readlines()
        procura(lendo)
    
    elif os.path.isdir("."):
        pasta = list(os.listdir(i))
        pasta_nova(pasta)
    
        
        


        
