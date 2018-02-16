# Jossian Abimelec García Quijano
#Calcula el total a pagar contando el descuento dependiendo de los paquetes comprados


def Calculardescuento(paquetes):
    if paquetes>0 and paquetes <9:
        descuento=paquetes*1500

    elif paquetes >9 and paquetes <20:
        descuento=(paquetes*1500)-(1500*0.20)

    elif paquetes >=20 and paquetes<50:
        descuento=(paquetes*1500)-(1500*0.30)

    elif paquetes >=50 and paquetes<100:
        descuento=(paquetes*1500)-(1500*0.40)
    elif paquetes>=100:
        descuento=(paquetes*1500)-(1500*0.50)
    else:
        descuento="Error"
    return descuento
def main():



    paquetes=int(input("Teclea el número de paquetes comprados: "))

    descuento=Calculardescuento(paquetes)
    print(descuento)

main()
