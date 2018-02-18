#encoding: UTF-8
#Autor: Genaro Ortiz Durán
#Descripción: Calcular perímetro y área de dos rectángulos.



#Calcula el area multiplicando la base por la altura
def calcularRectangulo(base, altura):
    area=base*altura
    return area

#Calcula el perímetro multiplicando el resultado de la suma de la base más la altura por dos.
def calcularPerimetro(base, altura):
    p=2*(base+altura)

    return p


def main():
    base=float(input("Escribe la base 1:"))
    altura=float(input("Escribe la altura 1:"))
    base1=float(input("Escribe la base 2:"))
    altura1=float(input("Escribe la altura 2:"))

    print("El area del rectangulo 1 es:",calcularRectangulo(base,altura),"u**2")
    print("El area del rectangulo 2 es:",calcularRectangulo(base1, altura1),"u**2")
    print("El perímetro del rectangulo es:",calcularPerimetro(base,altura),"u")
    print("El perímetro del rectangulo es:",calcularPerimetro(base1,altura1),"u")



main()