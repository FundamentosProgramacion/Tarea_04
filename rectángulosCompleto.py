# Autor: Diana Patricia Aguilar Martínez, A01745778
# Descripcion: Este programa lee los lados de dos rectangulos y calcula el area, perimetro y dice cual es mas grande o si son iguales
# A partir de aquí escribe tu programa

def calcularPerimetro(base, altura):
    perimetro= (2*base) +  (2*altura)
    return perimetro


def calcularArea(base, altura):
    area= base * altura

    return area


def main():
    base1= int(input("inserte la base del primer rectangulo: "))
    altura1= int(input("inserte la altura del primer rectangulo: "))

    base2 = int(input("inserte la base del segundo rectangulo: "))
    altura2 = int(input("inserte la altura del segundo rectangulo: "))

    perimetro1= calcularPerimetro(base1, altura1)
    perimetro2= calcularPerimetro(base2, altura2)

    area1= calcularArea(base1, altura1)
    area2= calcularArea(base2,altura2)

    print ("el perimetro del primer rectangulo es: ", perimetro1)
    print ("el perimetro del segundo rectangulo es: ", perimetro2)

    print ("el área del primer rectangulo es: " , area1)
    print ("el área del segundo rectangulo es: ", area2)

    if area1 > area2:
        print ("el rectangulo mayor es el primero")

    elif area2 > area1:
        print("el rectangulo mayor es el segundo")

    else:
        print("los rectangulos son iguales")

    

main()