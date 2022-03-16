#python3
#este codigo pega uma frase em um arquivo de texto e mofifica os seus verbos, substantivos adjetivos que estao destacados com seu respectivo nome
#o usaario inseri o novo valor rm seguida o codigo mostra o valor e depois o armazena em um outro arquivo de texto

arquivo = open("arquivo")
lendo = arquivo.read()
lendo = lendo.replace(".","")
lido = lendo.split()

for i in lido:

    if i.lower() =="adjective":
        novo = input("Digite qual adjetivo deseja colocar aqui ")
        posicao = lido.index(i)
        lido[posicao] = novo

    elif i.lower() == "noun":

        novo = input("Digite qual substantivo deseja colocar aqui ")
        posicao = lido.index(i)
        lido[posicao] = novo
    
    elif i.lower() == "adverb":

        novo = input("Digite qual adverbio deseja colocar aqui ")
        posicao = lido.index(i)
        lido[posicao] = novo

    elif i.lower() == "verb":

        novo = input("Digite qual verbo deseja colocar aqui ")
        posicao = lido.index(i)
        lido[posicao] = novo
    else:
        continue
print(lido)

modificado = open("modificadoarquivo","a")
modificado.write(str(lido))

modificado.close()
arquivo.close()

