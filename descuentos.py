# Autor:. Andrés Reyes Rangel
# Descripción: Calcular el área de un triangulo

def calcularDescuento(paquetes, unidades):
    precio = paquetes*1500
    if 10 <= unidades <= 19:
        descuento = precio-(precio*0.20)
        print("El descuento es del 20%")
    elif 20 <=unidades <= 49:
        descuento = precio-(precio*0.30)
        print("El descuento es del 30%")
    elif 50 <= unidades <= 99:
        descuento = precio - (precio * 0.40)
        print("El descuento es del 40%")
    elif 100 <= unidades:
        descuento = precio - (precio * 0.50)
        print("El descuento es del 50%")
    return descuento

def main():
    paquetes = int(input("¿Cuántos paquetes se vendieron? \n"))
    unidades = int(input("¿Cuántas unidades? \n"))

    descuento = calcularDescuento(paquetes, unidades)
    print("El precio es de:", descuento)
main()