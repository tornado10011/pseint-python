import os
os.system("cls")

print("bienvenido")

articulo=int(input("ingrese el precio del articulo: "))
dinero=int(input("ingrese el dinero con el que va a pagar: "))

if articulo==0 or dinero==0:
    print("datos ingresados incorrectos")

elif dinero<articulo:
    print("\nfalta dinero para completar el articulo")

elif dinero>articulo:
    vuelto=articulo-dinero
    print(f"el vuelto de su articulo comprado es de {vuelto} colones.")


