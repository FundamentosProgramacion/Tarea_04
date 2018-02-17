# Autor:. Andrés Reyes Rangel
# Descripción: Calcular el área de un triangulo


def calcularArea(base, base2, altura, altura2):
    mayor = ()
    area1 = base * altura
    area2 = base2 * altura2

    if area1 == area2:
        mayor = "Las áreas son iguales"
    elif area1 > area2:
        mayor = "El primer rectangulo es el mayor"
    else:
        mayor = "El segundo es el mayor"
    print("")
    print(mayor)
    return area1, area2


def calcularPerimetro(base, base2, altura, altura2):
    perimetro1 = (base * 2) + (altura * 2)
    perimetro2 = (base2 * 2) + (altura2 * 2)

    return perimetro1, perimetro2


def main():
    base = int(input("Ingresa la base de tu primer rectángulo: "))
    altura = int(input("Ingresa la altura de tu segundo rectángulo: "))
    base2 = int(input("Ingresa la base de tu primer rectángulo: "))
    altura2 = int(input("Ingresa la altura de tu segundo rectángulo: "))

    area = calcularArea(base, base2, altura, altura2)
    perimetro = calcularPerimetro(base, base2, altura, altura2)

    print("El área del primer rectángulo es de %i y el área del segundo es de %i " % area)
    print("El perímetro del primer rectángulo es de %i y el perímetro del segundo es de %i" % perimetro)

main()
