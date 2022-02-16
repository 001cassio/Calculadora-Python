#!python3
#este codigo propoe os resultados dos desafiios do curso de python3

#este codigo retorna os valores do tamanho de cada palavra na string
'''

lista =("vandercassio de oliveira rodrigues cassiooliveira203@gmail.com")

print( list(map( lambda x: len(x),lista.split())))

'''
#este codigo retorna apenas as palvavras inciadas em 'h' seja maiusculo ou minusculo
"""
palavras = ("hellho oma ddfrt Hinrefa dfadsgf ght hdfbg hgraeg")

print(list(filter(lambda x: x[0].lower() == "h", palavras.split())))


"""

ola = ('a','b','c')
oii = ('A','B','C')

print(list(zip(lambda ola,oii: ola,"-",oii)))
