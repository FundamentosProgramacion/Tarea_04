#encoding: UTF-8
#Jean Paul Esquivel Lobato
#Calcular el area y perimetro de dos rectangulos


def calcularAreaA(ladoA, ladoB):
    return ladoA*ladoB

def calcularPerimetroA(ladoA, ladoB):
    return 2*ladoA + 2*ladoB

def calcularAreaB(ladoC, ladoD):
    return ladoC*ladoD

def calcularPerimetroB(ladoC, ladoD):
    return 2*ladoC + 2*ladoD


def calcularRectangulos(areaA, areaB):
    if areaA > areaB:
        mayor = "El primer rectangulo tiene mayor área"
    elif areaB > areaA:
        mayor = "El segundo rectangulo tiene mayor área"
    else:
        mayor = "Tus rectángulos tienen la misma área"

    return mayor

def main():
    ladoA = float(input("Teclea el lado a: "))
    ladoB = float(input("Teclea el lado b: "))
    ladoC = float(input("Teclea el lado c: "))
    ladoD = float(input("Teclea el lado d: "))

    areaA = calcularAreaA(ladoA,ladoB)
    perimetroA = calcularPerimetroA(ladoA,ladoB)
    areaB = calcularAreaB(ladoC,ladoD)
    perimetroB = calcularPerimetroA(ladoC, ladoD)

    rectangulos = calcularRectangulos(areaA, areaB)

    print("El área del primer rectángulo es de: ", areaA)
    print("El perímetro del primer rectángulo es de: ", perimetroA)
    print("El área del segundo rectángulo es de: ", areaB)
    print("El perímetro del segundo rectángulo es de: ", perimetroB)
    print("Por lo tanto: ", rectangulos)

main()