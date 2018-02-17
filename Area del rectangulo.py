#Autor: Eduardo Roberto Müller Romero
#Este programa recibe las dimensiones de dos rectángulos, calcula área y perímetro de ambos, y decide cual es el más grande

def perimetroyArea(x, y): #Calcular Perímetro y Área
	perimetro = 2 * x  + 2 * y
	area = x * y
	return perimetro, area

def compararArea(a, b): #Decide cuál es mayor o si son iguales también regresa un resultado
	el_mayores = ""
	if a > b:
		el_mayores = "La del rectángulo 1"
	elif a < b:
		el_mayores = "La del rectángulo 2"
	elif a == b:
		el_mayores = "Ninguna, las áreas son iguales"
	return el_mayores

def main():
	x1 = int(input("Largo del rectángulo 1: "))
	y1 = int(input("Ancho del rectángulo 1: "))
	x2 = int(input("Largo del rectángulo 2: "))
	y2 = int(input("Ancho del rectángulo 2: "))
	perimetro1, area1 = perimetroyArea(x1, y1)
	perimetro2, area2 = perimetroyArea(x2, y2)
	area_mayor = compararArea(area1, area2)
	print("El área mayor es: ", area_mayor)

main()