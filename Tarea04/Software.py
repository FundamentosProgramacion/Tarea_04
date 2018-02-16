#Carlos Ochoa
#Define el costo de un software

def main():
    cantidad=int(input("Cuantos software compro: "))

    if cantidad>=10 and cantidad<20:
        costo=cantidad*1500
        costo=costo - costo*.20

        print ("Costo a pagar es: ", costo)

    elif cantidad>=20 and cantidad<50:
        costo=cantidad*1500
        costo=costo-costo*.30

        print ("Costo a pagar es: ", costo)

    elif cantidad>=50 and cantidad<100:
        costo=cantidad*1500
        costo=costo-costo*.40

        print ("Costo a pagar es: ", costo)

    elif cantidad>=100:
        costo=cantidad*1500
        costo=costo-costo*.50

        print ("Costo a pagar es: ", costo)

    else:
        costo=cantidad*1500

        print ("Costo a pagar es: ", costo)

main()
