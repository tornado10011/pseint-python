import os
os.system("cls")

cuenta=0
total=0


veces=int(input("ingrese la cantidad de veces que desea sumar: "))

for i in range(veces):
    cuenta=cuenta+1
    print("\n"f"esta es la {cuenta} vez")
    num1=int(input("\ningrese el primer digito: "))
    num2=int(input("ingrese el segundo digito: "))
    suma=num1+num2
    total=suma+total
    print(f"la suma es: {suma}")
   

print(f"la suma en total es: {total}")
