#Autor: Nataly Paulina Lopez Salazar
#Con los valores de los lados del rectangulo se calculan areas y perimetros y decir cual area es mayor.

def calcularPerimetro(b,a):         #Calcula el perimetro de los dos triangulos.
    peri = 2*b + 2*b
    return peri

def calcularArea(b,a):          #Calcula el area de los rectangulos
    area = (b*a)/2
    return area


def calcurlarMayor(area1,area2):                #Menciona cual area es mayor de las dos.
    if area1<area2:
        print("El rectangulo 2 tiene mayor area")
    elif area1>area2:
        print("El rectangulo 1 tiene mayor area")
    else:
        print("Las areas son iguales")


def main():
    print("Rectangulo 1")
    ladoA = int(input("Dame el valor de la base:"))
    ladoH = int(input("Damel el valor de la altura:"))

    perimetro = calcularPerimetro(ladoA,ladoH)
    area1 = calcularArea(ladoA,ladoH)

    print("Perimetro:",perimetro)
    print("Area:",area1)


    print("Recangulo 2")
    base = int(input("Teclea el valor de la base:"))
    altura = int(input("Teclea el valor de la altura"))

    perimetro= calcularPerimetro(base,altura)
    area2= calcularArea(base,altura)

    print("Perimetro:", perimetro)
    print("Area:", area2)

    mayor = calcurlarMayor(area1,area2)

main()