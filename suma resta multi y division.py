import os 
os.system("cls")

print("Bienvenido a la calculadora")

num1=int(input("digite el primer numero:"))
num2=int(input("digite el segundo numero:"))

suma=num1+num2
multiplicacion=num1*num2
resta=num1-num2

resta_alrevez=num2-num2

print(f"""\nla suma: {suma}
la resta: {resta} 
la resta alrevez: {resta_alrevez}
la multiplicacion: {multiplicacion}""")

if num1==0 or num2==0:
    print("no se puede dividir entre 0")

else:
    division=num1/num2
    division_alrevez=num2/num1
    restante_num1= num1%num2
    restante_num2= num2%num1

    print(f"""\nla division es: {division}
la division alrevez es: {division_alrevez}
el restante del numero1: {restante_num1}
el restante del numero 2: {restante_num2}""")