#Autor: Ricardo Cornejo
#Calcula area y perimetro de dos triangulos y calcula cual de los dos es mayor.

def calculaArea(b1,a1):
    area1 = b1*a1
    return area1

def calcularPerimetro(b2,a2):
    Perimetro2 = (b2*2) + (a2*2)
    return Perimetro2

def main():
    base = int(input("Teclea base del primer rectangulo: "))
    altura = int(input("Teclea altura del primer perimetro: "))
    base2 = int(input("Teclea base del segundo rectangulo: "))
    altura2 = int(input("Teclea altura del segundo rectangulo: "))
    areaFinal = calculaArea(base, altura)
    areaFinal2 = calculaArea(base2, altura2)
    perimetroFinal = calcularPerimetro (base, altura)
    perimetroFinal2 = calcularPerimetro (base2, altura2)
    print ("\nArea del primer rectangulo: " +str(areaFinal),"\nArea del segundo rectangulo: " +str(areaFinal2), "\nPerimetro del primer rectngulo: " +str(perimetroFinal), "\nPerimetro del segundo triangulo: " +str(perimetroFinal2))

    if areaFinal == areaFinal2:
        print ("\nLos rectangulos son iguales. ")
    elif areaFinal > areaFinal2:
        print ("\nEl primer rectangulo es mayor. ")
    else:
        print ("\nEl segundo rectangulo es mayor. ")

main()
