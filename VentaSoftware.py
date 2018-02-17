# Autor: Carlos Martínez Rodríguez
# Descripción: Calcular el precio de venta de una compañía de software

# Función que calcula el descuento que se debe aplicar dependiendo de la cantidad de paquetes que se venden
def calcularDescuento(paquetes):
    precioBase = 1500
    if (paquetes > 10 % paquetes < 19):
        return (paquetes * precioBase) * .20
    elif (paquetes > 20 & paquetes < 49):
        return (paquetes * precioBase) * .30
    elif (paquetes > 50 & paquetes < 99):
        return (paquetes * precioBase) * .40
    elif (paquetes > 100):
        return (paquetes * precioBase) * .50

# Función que calcula el total aplicando el descuento a los paquetes vendidos
def calcularTotal(paquetes):
    precioBase = 1500
    return (paquetes * precioBase) - calcularDescuento(paquetes)

# Función Main
def main():
    # Entradas
    numPaquetes = int(input("Número de paquetes: "))

    # Si el usuario no introduce un número positivo el programa devuelve un error, de lo contrario se ejecuta y calcula
    # el descuento y total
    if (numPaquetes >= 0):
        # Calcular descuento y tootal de la venta
        descuento = calcularDescuento(numPaquetes)
        total = calcularTotal(numPaquetes)

        # Salidas
        print("\nTotal Descuento: %.2f" % descuento)
        print("Total:           %.2f" % total)
    else:
        print("ERROR: No puedes escribir números negativos")

main()