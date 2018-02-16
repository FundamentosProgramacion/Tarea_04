#Carlos Ochoa
#Define que area es mayor

#Calcula el perimetro del primer rectangulo
def perimetroRec1(base1,altura1):
    perimetro1 = 2*base1 + 2*altura1

    return perimetro1

#Calcula el area del primer rectangulo
def areaRec1(base1,altura1):
    area1 = base1 * altura1

    return area1

#Calcula el perimetro del segundo rectangulo
def perimetroRec2(base2,altura2):
    perimetro2 = 2*base2+ 2*altura2

    return perimetro2

#Calcula el area del segundo triangulo
def areaRec2(base2,altura2):
    area2 = base2 * altura2

    return area2


def main():
    baseRectangulo1=int(input("Escribe la base del primer rectangulo: "))
    alturaRectangulo1=int(input("Escribe la altura del primer rectangulo: "))
    baseRectangulo2=int(input("Escribe la base del segundo rectangulo: "))
    alturaRectangulo2=int(input("Escribe la altura del segundo rectangulo: "))
    perimetro1=perimetroRec1(baseRectangulo1, alturaRectangulo1)
    area1=areaRec1(baseRectangulo1,alturaRectangulo1)
    perimetro2=perimetroRec2(baseRectangulo2,alturaRectangulo2)
    area2=areaRec2(baseRectangulo2,alturaRectangulo2)

    if area1>area2:
        print("El area uno es mayor")

    elif area1==area2:
        print("Las areas son iguales")

    else:
        print("El area dos es mayor")



main()
