#!python3
#copiar.py-copia e usa

import pyperclip
text = pyperclip.paste()

lines = text.split("\n")
for i in range(len(lines)):
    lines[i] ="*" + lines[i]

text = "\n".join(lines)

pyperclip.copy(text)
print(text)