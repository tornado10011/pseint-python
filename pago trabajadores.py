import os
os.system("cls")

print("bienvenido a calculadora de pago")

horas=int(input("indique sus horas trabajadas: "))

trabajo=int(input("\n""coloque 1 si usted es peon, coloque 2 si usted es maestro de obras: "))

if trabajo==1:
    peon=1500*horas
    print(f"su pago siendo peon seria de {peon}")

elif trabajo==2:
    maestro=3000*horas
    print(f"su pago siendo maestro de obras seria en total de: {maestro}")

else:
    print("su paga no se a realizado porque no a indicado el numero correctamente")

