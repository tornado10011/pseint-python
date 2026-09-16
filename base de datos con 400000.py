import os
os.system("cls")

valorinicial=int(input("indique el valor de su compra: "))

if valorinicial<=0:
    print("usted no indico el valor correctamente")

elif valorinicial>400000:
    print("su compra ha sido aceptada")
    nombre=input("indique su nombre: ")
    print(f"estimado {nombre} su compra a sido acreditada por el valor de {valorinicial}")
else:
    print("su pedido a sido rechazado")

