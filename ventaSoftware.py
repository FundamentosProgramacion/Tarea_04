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

def calcularCostoDescuento(numeroPaquetes):
    if numeroPaquetes<=0:
        return "Esta cantidad de paquetes no es válida"

    elif numeroPaquetes>=10:
        descuentoF = calcularDescuento(numeroPaquetes)
        costoFinalF = calcularCosto(numeroPaquetes)
        return ("El descuento es:$%i\n El costo total es:$%i"%(descuentoF,costoFinalF))
    else:
        costoFinal = numeroPaquetes*1500
        return "El costo final es:$%i"%(costoFinal)

def main():
    numeroPaquetes = int(input("¿qué número de paquetes deseea a comprar?: "))
    paquetesCalculos= calcularCostoDescuento(numeroPaquetes)
    print (paquetesCalculos)

main()