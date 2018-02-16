#encoding: UTF-8
#Jean Paul Esquivel Lobato
#Calcular la compra de una venta


def calcularCompra(paquete):
    if paquete < 10:
        paga = paquete*1500
    elif paquete >= 10 and paquete <= 19:
        pagaSin = (paquete*1500)
        paga = pagaSin - (pagaSin*.20)
    elif paquete >= 20 and paquete <= 49:
        pagaSin = (paquete * 1500)
        paga = pagaSin - (pagaSin * .30)
    elif paquete >= 50 and paquete <= 99:
        pagaSin = (paquete * 1500)
        paga = pagaSin - (pagaSin * .40)
    elif paquete >= 100:
        pagaSin = (paquete * 1500)
        paga = pagaSin - (pagaSin * .50)
    else:
        paga = "Error, teclea un valor correcto."

    return paga

def main():
    paquete = int(input("¿Cuántos paquetes compraste? : "))
    compra = calcularCompra(paquete)

    print("Tu monto a pagar por tu compra fue: ", "$", compra)

main()