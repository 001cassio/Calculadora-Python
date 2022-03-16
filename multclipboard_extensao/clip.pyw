#python 3
#este codigo salva e carrega porcoes de texto no clipboard

import shelve, pyperclip , sys, os

arquivos = shelve.open("salve")

if len(sys.argv) == 3:

    if (sys.argv[1]).lower() == "save":
        
        arquivos[sys.argv[2]] = pyperclip.paste()

    elif(sys.argv[1]).lower() == "delete":

        del arquivos[sys.argv[2]]
        pyperclip.copy(str(list(arquivos.keys())))
        
elif len(sys.argv) == 2:

    if sys.argv[1].lower() =="list":
        
        pyperclip.copy(str(list(arquivos.keys())))
    
    elif sys.argv[1] in arquivos:
     
        pyperclip.copy(arquivos[sys.argv[1]])
    
    elif sys.argv[1] == "delete":

        #ATENCAO PROBLEMA AINDA NAO RESOLVIDO
        del arquivos.keys[:]
        pyperclip.copy(str(list(arquivos.keys())))

arquivos.close()
['texto', 'oii', 'namorada']['texto', 'oii', 'namorada']

