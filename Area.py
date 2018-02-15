#Autor Karla Fabiola Ramirez Martinez
#Descripcion: Calcula el area y perimetro de dos rectangulos

#funcion de area
def calcularArea(b,a):
    area=b*a
    return area

#Funcion de perimetro
def calcularPerimetro(b,a):
    perimetro=2*b+a*2
    return perimetro

#Funcion que calcula la mayor area
def calcularMayor(a1,a2):
    respuesta=""
    if a1==a2:
        respuesta="Son iguales"
        return respuesta
    elif a1>a2:
        respuesta="El area del primer rectangulo es mayor"
        return respuesta
    else:
        respuesta= "El area del segundo rectangulo es mayor"
        return  respuesta

#Funcion principal
def main():
    #Se pediran los lados de ambos rectangulos
    #rectangulo1
    print ("Dime los lados del primer rectangulo")
    base1=int(input("Dime la base : "))
    altura1=int(input("Dime la altura : "))

    #rectangulo2
    print ("Dime los lados del segundo rectangulo")
    base2=int(input("Dime la base: "))
    altura2=int(input("Dime la altura: "))
#Aqui es donde se ponen los valores para las funciones
    rectangulo1area=calcularArea(base1,altura1)
    rectangulo2area=calcularArea(base2,altura2)
    rectangulo1perimetro=calcularPerimetro(base1,altura1)
    rectangulo2perimetro=calcularPerimetro(base2,altura2)
    mayorrectangulo=calcularMayor(rectangulo1area,rectangulo2area)

    print("Area y perimetro del primer rectangulo")
    print("El area  es: ",rectangulo1area)
    print("El perimetro es: ",rectangulo1perimetro)
    print ("Area y perimetro del segundo rectangulo")
    print("El area  es: ",rectangulo2area)
    print("El perimetro es: ",rectangulo2perimetro)
    print(mayorrectangulo)





















main()