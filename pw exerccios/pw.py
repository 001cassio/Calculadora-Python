#!python3
#pw.py-progama pra senhas doidas

senha ={"cassiooliveira203@gmail.com":99911739}

import sys,pyperclip
if len(sys.argv) < 2:
    print("voce nao colocou a conta")
    sys.exit()

account = sys.argv[1]
if account in senha.keys():
    pyperclip.copy(senha[account])
    print("senha e" + account + "copiado")
else:
    print("nao esta salvo")
    