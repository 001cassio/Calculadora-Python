import time, datetime

'''

print(str(time.localtime().tm_year))
print(str(time.localtime().tm_yday))
print(str(time.localtime().tm_hour))
print(str(time.localtime().tm_gmtoff))
print(str(time.localtime().tm_zone))
print(str(time.localtime().tm_isdst))
'''
dia = int(input("digite o dia"))
mes = int(input("digite o mes"))
ano = int(input("digite o ano"))
data_pesquisa = datetime.datetime(ano,mes,dia)
dia2 = data_pesquisa.date()
print(dia2)


print(data_pesquisa.today())
print(data_pesquisa.time())
print(data_pesquisa.date())

'''
if data_pesquisa > data_pesquisa.today():
    time.sleep(5)
    resultado = data_pesquisa - data_pesquisa.today()
    print("faltam %d para a data especificada, e %d meses" %(resultado., resultado.date))

else:
    print("menor")

'''

