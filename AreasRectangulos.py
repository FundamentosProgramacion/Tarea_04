# Autor: Carlos Martínez Rodríguez
# Descripción: Programa que calcula el área y perímetro de dos rectángulos y determina cual es más grande.

# Función que calcula el área del rectángulo
def areaRectangulo(base, altura):
    return base * altura

# Función que calcula el perímetro del rectángulo
def perimetroRectangulo(base, altrua):
    return (2 * base) + (2 * altrua)

# Función que determina que rectángulo es mayor o si son iguales
def compararRectangulos(area1, area2):
    if (area1 > area2):
        return "El rectángulo 1 es mayor al rectángulo 2"
    elif (area1 < area2):
        return "El rectángulo 2 es mayor al rectángulo 1"
    else:
        return "Los rectángulos son iguales"

def main():
    # Entradas
    baseRect1 = int(input("Base Rectángulo 1: "))
    alturaRect1 = int(input("Altura Rectángulo 1: "))
    baseRect2 = int(input("Base Rectángulo 2: "))
    alturaRect2 = int(input("Altura Rectángulo 2: "))

    # Calcular área y perímetro de ambos rectángulos
    areaRect1 = areaRectangulo(baseRect1, alturaRect1)
    areaRect2 = areaRectangulo(baseRect2, alturaRect2)
    perimetroRect1 = perimetroRectangulo(baseRect1, alturaRect1)
    perimetroRect2 = perimetroRectangulo(baseRect2, alturaRect2)

    # Salidas
    print("\nRectángulo 1 - área: %.0i perímertro: %.0i" % (areaRect1, perimetroRect1))
    print("Rectángulo 2 - área: %.0i perímertro: %.0i \n" % (areaRect2, perimetroRect2))
    print(compararRectangulos(areaRect1, areaRect2))

main()