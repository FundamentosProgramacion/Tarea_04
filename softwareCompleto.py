# Autor: Diana Patricia Aguilar Martínez, A01745778
# Descripcion: Este programa calcula el descuento de un software
# A partir de aquí escribe tu programa

def calcularTotal(software):
    total=""

    if software>=0 and software <10:
        total=1500

    elif software >= 10 and software <= 19:
        total= 1500*0.8

    elif  software >=20 and software <=49:
        total= 1500*0.7

    elif software >=50 and software <=99:
        total = 1500* 0.6

    elif software >= 100:
        total= 1500*0.5

    return total


def main():
    pagoTotal = ""
    descuento= ""

    cantidad=int(input("Teclee la cantidad de softwares que compro: "))

    if cantidad < 0 :
        print("Cantidad no válida, estado de error")

    else:
        pagoTotal= calcularTotal(cantidad)
        descuento = 1500 - pagoTotal
        print("Su descuento es de: ", descuento)
        print("Usted debe pagar", pagoTotal, "por", cantidad, "softwares")

main()