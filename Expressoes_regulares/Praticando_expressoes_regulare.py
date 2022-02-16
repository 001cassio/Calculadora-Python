import re, pyperclip
texto_base = str(pyperclip.paste())

base_numero = re.compile(r"(\d\d)?(\d){9}|(\d){:5}\S?(\d){4}")
base_email = re.compile(r"(\w)+[@](\w)+[.com]{1}")

resultado = []

for groups  in  base_numero.findall(texto_base):
    resultado.append(groups[0])
for groups in base_email.findall(texto_base):
    resultado.append(groups[0])

print(resultado)


