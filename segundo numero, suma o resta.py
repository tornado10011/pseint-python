import os
os.system("cls")
suma=0

num1=int(input("digite el primer numero: "))
num2=int(input("digite el segundo numero: "))

if num2>100:
    suma=num1+num2
    print(f"la suma seria de {suma}")
elif num2<50:
    resta=num1-num2
    print(f"la resta seria de {resta}")