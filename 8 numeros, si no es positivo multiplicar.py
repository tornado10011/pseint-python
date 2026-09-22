import os
os.system("cls")
suma=0

print("bienvenido\n")

for i in range(8):
    num=int(input("ingrese el numero: "))
    suma=suma+num
if suma>0:
    print("los numeros brindados son positivos")
else:
    multi=suma*num
    print(f"los numeros no son positivos \n\nse procedera a multiplicarlos. \nla multiplicacion seria de {multi}")