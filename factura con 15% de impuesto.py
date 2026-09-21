import os 
os.system("cls")

print("bienvenido\n")


precio=int(input("ingrese el precio del articulo: "))

if precio<=0:
    print("usted ingreso el precio incorrectamente")

else:
    impuesto=precio*0.15
    precio_final=precio+impuesto
    print(f"\nel precio final seria de {precio_final}")