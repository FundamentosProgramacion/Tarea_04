#encoding: UTF-8
#Autor: Genaro Ortiz Durán
#Descripción: Hacer que un programa que lea los lados del triángulo y escriba el tipo de triángulo.



def main():
    a=float(input("Escribe el lado a:"))
    b=float(input("Escribe el lado b:"))
    c=float(input("Escribe el lado c:"))

    if a==b and b==c: # La condición se cumple si los lados son iguales.
        print("Triángulo equilátero")

    elif a==b or a==c or b==c: # Si dos lados son iguales se cumple la condición.
        print("El triángulo es isósceles")

    elif a!=b and a!=c and b!=c: #Se cumple la condición si uno de los lados es diferente.
        print("El triángulo es Rectángulo")
    else:
        print("Estos lados no corresponden a un triángulo")










main()