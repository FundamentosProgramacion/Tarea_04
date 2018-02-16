    #Jossian Abimelec García Quijano
    #Lee las dimensiones de dos rectángulos y calcula su perímetro así como su área


def Calcularperimetro(base, altura):
    perimetro=2*base+2*altura
    return perimetro

def Calculararea(base, altura):
    area=base*altura
    return area

def main():
    base=int(input("Cuál es la base del primer rectángulo"))
    altura = int(input("Cuál es la altura del primer rectángulo"))
    base1 = int(input("Cuál es la base del segundo rectángulo"))
    altura1 = int(input("Cuál es la altura del segundo rectángulo"))

    perimetro=Calcularperimetro(base, altura)
    area = Calculararea(base, altura)
    perimetro1=Calcularperimetro(base1, altura1)
    area1 = Calculararea(base1, altura1)
    print ("el perimetro del primer rectángulo es: ",perimetro,"\nel area del primer rectángulo es: ",area,"\nel perimetro del segundo rectángulo es: ",perimetro1,"\nel area del segundo rectángulo es: ",area1)
    if area> area1:
        print("El área del primer rectángulo es mayor")
    elif area<area1:
        print("El área del segundo rectángulo es mayor")
    else:
        print("Las áreas son iguales")
main()