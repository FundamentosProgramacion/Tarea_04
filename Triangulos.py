#Autor: Eduardo Roberto Müller Romero
# Este programa recibe los lados de un triangulo si existe, indica si es equilatero, isosceles o rectángulo
import math
def definirTriangulo(a, b, c):
	triangulo = ""
	if a + b <= c and b - c >= a:
		return "Estos lados no corresponden al triangulo"
	else:
		if a == b:
			if b == c:
				triangulo = "equilátero"
			elif a > c or c > a:
				triangulo = "isóceles"
		elif a > b:
			if a == c:
				triangulo = "isóceles"
			elif a > c and c != b:
				triangulo = "rectángulo"
			elif c > a:
				triangulo  = "rectángulo"
		elif b > a:
			if b == c:
				triangulo = "isóceles"
			elif b > c and c != a:
				triangulo = "rectángulo"
		return triangulo


def main():
	lado1 = int(input("Longitud del lado1: "))
	lado2 = int(input("Longitud del lado2: "))
	lado3 = int(input("Longitud del lado3: "))
	esUnTriangulo_ = definirTriangulo(lado1, lado2, lado3)
	if esUnTriangulo_ == "Estos lados no corresponden al triangulo":
		print(esUnTriangulo_)
	else:
		print("Es un triángulo", esUnTriangulo_)

main()