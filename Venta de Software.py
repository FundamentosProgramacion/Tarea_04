#Autor: Eduardo Roberto Müller Romero
# Una compañía aplica cierto descuento al comprar n cantidad de paquetes de software, el programa calcula descuento y total

def calcularPago(x):
	'''
	La función recibe un valor y basándose en el, decide si se aplica un descuento, que descuento se aplica y además
	calcula el total.
	'''
	total = int()
	descuento = ""
	subtotal = x * 1500
	if x < 10:
		descuento = "Ninguno"
		total = subtotal
	elif x >= 10 and x <= 19:
		total = subtotal - (subtotal * .2)
		descuento = "20%"
	elif x >= 20 and x <= 49:
		total = subtotal - (subtotal * .3)
		descuento = "30%"
	elif x >=40 and x <= 99:
		total = subtotal - (subtotal * .4)
		descuento = "40%"
	elif x > 99:
		total = subtotal * .5
		descuento = "50%"
	return descuento, total

def main():
	software_vendido = int(input("Cantidad de paquetes adquiridos: "))
	if software_vendido < 0:
		print("Error de Capa 8", "\nInsertaste un valor inválido \n:(")
	descuento, total = calcularPago(software_vendido) #La función regresará el total y el descuento que se aplicó
	print("Compraste", software_vendido, "paquetes de software.", "\nSe aplicó un descuento del:", descuento,
		  "\nEl total a pagar sería de: $%.02f" % total)


main()