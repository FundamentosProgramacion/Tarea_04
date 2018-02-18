#encoding UTF-8
# Genaro Ortiz Durán, A01375315
#Descripción: Hacer un programa que lea la cantidad de paquetes comprados, hacer un descuento si lo hay y hacer el total de la compra.

# Calcula el total de la compra multiplicando el número de paquetes por el precio. Si se compran más de 9 paquetes se aplica un descuento a partir de los rangos establecidos.
def calcularDescuento(paquete):
    precio=0
    if paquete>0 and paquete<10:
        precio=paquete*1500
    elif paquete>=10 and paquete<19:
        precio=(paquete * .80) * 1500
    elif paquete>=20 and paquete<49:
        precio=(paquete*.70)*1500
    elif paquete>=50 and paquete<99:
        precio=(paquete * .60) * 1500
    elif paquete>99:
        precio = (paquete * .50) * 1500

    return precio





def main():
    paquete=int(input("¿Cuántos paquetes quieres:"))
    if paquete<0:
        print("ERROR")
    elif paquete==0:
        print("No se ha comprado ningún paquete")
    else:
        print("El total es:", calcularDescuento(paquete))

main()