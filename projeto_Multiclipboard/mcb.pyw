#python 3
#este codigo salva e carrega porcoes de texto no clipboard

import shelve, pyperclip,sys

arquivoshelb = shelve.open("mcb")

#este trecho verifica se o cmd vai receber tres arumentos, o de chamamento, o save e o nome da chave, se sim ele 
# armazena o valor que esta no copiar/colar numa dic com a chave que e o segundo argumento que foi chamado
if len(sys.argv) == 3 and (sys.argv[1]).lower() == "save":

    arquivoshelb[sys.argv[2]] = pyperclip.paste()

#se foi chamado apenas com dois valores ele verifica, se for list, vai copiar todas as chaves de valores para o copiar/colar
#se nao ele vai verificar se o argumento e uma chave e retornar o valor armazenado nela para o copiar e colar

elif len(sys.argv) ==2:
    if sys.argv[1] =="list":
        pyperclip.copy(str(list(arquivoshelb.keys())))
    elif sys.argv[1] in arquivoshelb:
        pyperclip.copy(arquivoshelb[sys.argv[1]])

#fecha o arquivo
arquivoshelb.close()

#pode ser  muito ultilizado em tarefas macantes que envolvem preenchimento repetitivo de textos

