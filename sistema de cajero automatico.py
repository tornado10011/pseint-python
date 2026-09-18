import os

contador=3

pin=5144
os.system("cls")
tarjeta=int(input("presione 1 si quiere ingresar tarjeta \npresione 2 si no \n\ndigite que desea hacer:"))

if tarjeta<=0 or tarjeta>2:
    print("usted no indico que desea realizar correctamente")

if tarjeta==1:
    pinn=int(input("digite el pin de su tarjeta: "))

    if pinn==pin:
        print("bienvenido")
    else:
        for i in range(contador):
            pinn=int(input("digite nuevamente el pin de su tarjeta: ""\n"))

            if pinn==pin:
                print("bienvenido")
            else:
                contador=contador-1
                print(f"le quedan {contador} intentos\n")
                