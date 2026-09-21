import os
os.system("cls")

cualquier_persona=5000
hora_extra=1500

print("bienvenido")

horas=int(input("ingrese las horas trabajadas"))

if horas<=40:
    sin_extras=cualquier_persona*horas
    print(f"su paga seria de {sin_extras} ya que no cumple con el minimo de horas para incluir las horas extras")
else:
    extra=horas-40
    salario_extra=extra*(cualquier_persona+hora_extra)
    salario=40*cualquier_persona
    salario_total=salario+salario_extra
    print(f"su paga seria de {salario} y su salario con horas extra seria de {salario_total} ")