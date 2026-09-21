import os
os.system("cls")
suma=0

print("bienvenido a la suma de 10 numeros")

for i in range(10):
    num=int(input("digite el numero: "))
    suma=suma+num
print(f"\nla suma es el total de {suma}")