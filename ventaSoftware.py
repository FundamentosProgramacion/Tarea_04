#Mirna Fernanda Zertuche Calvillo A01373852
#Calcula el costo de compra de paquetes de software y su respectivo descuento si es que lo poseen

def calcularCosto(n):
    if n>= 10 and n<19:
        costo= (n* 1500)*.8
        return costo
    elif n>= 20 and n<49:
        costo = (n * 1500)*.7
        return costo
    elif n>= 50 and n<99:
        costo = (n * 1500)*.6
        return costo
    elif n>= 100:
        costo = (n * 1500)*.5
        return costo



def calcularDescuento(n):
    if n>= 10 and n<19:
        descuento = ((n*1500)*.2)
        return descuento
    elif n>= 20 and n<49:
        descuento = ((n * 1500) *.3)
        return descuento
    elif n>= 50 and n<99:
        descuento = ((n * 1500) *.4)
        return descuento
    elif n>= 100:
        descuento = ((n * 1500) *.5)
        return descuento


def main():
    numeroPaquetes = int(input("¿qué número de paquetes deseea a comprar?: "))
    if numeroPaquetes<=0:
        print("Esta cantidad de paquetes no es válida")

    elif numeroPaquetes>=10:
        descuento = calcularDescuento(numeroPaquetes)
        costoFinal = calcularCosto(numeroPaquetes)
        print("El descuento es: $%.2f"% descuento)
        print("EL costo final es: $%.2f"% costoFinal)
    else:
        costoFinal = numeroPaquetes*1500
        print("EL costo final es: $%.2f"%costoFinal)

main()