#Autor: Nataly Paulina Lopez Salazar
#Calcular el descuento por cada sotware vendido.

def calcularPrecio(numSof):# Calcula el total con el descuento a pagar.

    if numSof<10:
        t = numSof*1500
        return t
    elif numSof>10 and numSof<=19:
        d = numSof*1500*.80
        return d
    elif numSof>=20 and numSof<=49:
        d = numSof*1500*.70
        return d
    elif numSof>=50 and numSof<=99:
        d = numSof*1500*.60
        return d
    elif numSof>=100:
        d =numSof*1500*.50
        return d

def main():
    numSof = int(input("Teclea el numero de paquetes:"))

    descuento = calcularPrecio(numSof)

    print("Total a pagar:$",descuento)

main()

