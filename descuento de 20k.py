import os 
os.system("cls")

compra=int(input("digite el precio de la compra a realizar: "))
    
if compra>20000:
    descuento=compra*0.35
    print(f"""\nsu descuento es de {descuento}
su pago final es de: {compra-descuento}""")

else:
    descuento=0
    print("su compra no llega al precio para el descuento")