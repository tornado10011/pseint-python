import os 
os.system("cls")

accion=int(input("""digite 1 si quiere convertir de millas marinas a metros
presione 2 si quiere convertir de metros a millas \n\ndigite que desea realizar:"""))

if accion==1:
    millas=int(input("indique cual serian sus millas: "))
    metros=1852*millas
    print(f"sus metros serian de {metros}")

elif accion==2:
    metros=int(input("indique sus metros: "))
    millas=metros/1852
    print(f"sus millas serian de {millas}")

else:
    print("no indico que desea realizar correctamente")