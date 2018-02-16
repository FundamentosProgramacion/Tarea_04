#Autor: Ricardo Cornejo
#Calcula el total a pagar por el paquete de sorftware incluyendo el decuento si lo hay

def calculaTotal(PaquetesComprados):
    if PaquetesComprados < 10:
        return SinDescuento
    if PaquetesComprados >= 10:
        return (1500*PaquetesComprados)*.80
    elif PaquetesComprados >= 20:
        return (1500*PaquetesComprados)*.70
    elif PaquetesComprados >= 50:
        return (1500*PaquetesComprados)*.60
    elif PaquetesComprados > 100:
        return (1500*PaquetesComprados)*.50
    else:
        return "Error21: Unicamente Teclea numeros positivos"

def main():
    cantidadPaquetes = int(input("Teclea numero de paquetes comprados: "))
    SinDescuento = 1500 * cantidadPaquetes
    total = calculaTotal(cantidadPaquetes)
    print ("\nSubtotal: $%.2f " % (SinDescuento), "\nCantidad descontado: $%.2f " %(total-SinDescuento), "\nTotal a pagar: $%.2f " %(total))

main()