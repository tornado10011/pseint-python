import os
os.system("cls")

opciones=int(input("si quiere realizar un pago de trabajadores presione 1 \nsi quiere sumar 10 numeros presione 2 \nsi quiere convertir de millas a metros y viceversa presione 3 \n \nindique que desea realizar: "))

if opciones==1:

    horas=int(input("\n""indique sus horas trabajadas: "))
    if horas<=0:
        print("no se puede continuar")
    else:
        trabajo=int(input("\n""coloque 1 si usted es peon, coloque 2 si usted es maestro de obras: "))

    if trabajo==1:
        peon=1500*horas
        os.system("cls")
        print(f"su pago seria de {peon} siendo peon con {horas} horas")
        
    elif trabajo==2:
        maestro=3000*horas
        os.system("cls")
        print(f"su pago seria de {maestro} siendo maestro de obras con {horas} horas")

    print("muchas gracias""\n")

if opciones==2:

    print("suma de 10 numeros""\n")
    suma=0
    for i in range(10):
        numeros=int(input("indique los 10 numeros: "))
        suma=suma+numeros
        os.system("cls")
    if numeros>=0:
        print("\n""numeros validos")
        print(f"la suma de los 10 digitos seria de {suma}")
    else:
        print("numeros invalidos")

    print("muchas gracias""\n")

if opciones==3:
    accion=int(input("\n""presione 1 si quiere covertir de millas a metros \npresione 2 si quiere convertir de metros a millas marinas \nindique su opcion: "))
    
    if accion==1:
        millas=int(input("\n""indique cuales serian sus millas: "))
        if millas<=0:
            print("sus millas son incorrectas")
        else:
            metros=1852*millas
            print(f"sus metros serian de {metros}")
        
    if accion==2:
        metros=int(input("indique cuales serian sus metros: "))
        if metros<=0:
            print("sus millas son incorrectas")
        else:
            millas=metros/1852
            print(f"sus metros serian de {millas}")

    print("muchas gracias""\n")