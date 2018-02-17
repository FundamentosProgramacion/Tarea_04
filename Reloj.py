#Autor: Eduardo Roberto Müller Romero
# Este programa convierte horas en formato de 24 hrs a formato de 12hrs

def cambiarFormato(hrs):
	AmPm = ""
	horas = int()
	if 0 <= hrs <= 12:
		AmPm = "AM"
		return hrs, AmPm
	else:
		AmPm = "PM"
		horas = hrs  - 12
		return horas, AmPm

def main():
	horas = int(input("Escribe la hora actual(sólo el número de horas ej. 00hrs o 01hrs): "))
	if horas >= 24:
		print("Error de Capa 8", "\nInsertaste un valor inválido \n:(")
		pass
	minutos = int(input("Escribe la hora actual(sólo el número de minutos ej. 00): "))
	if minutos > 60:
		print("Error de Capa 8", "\nInsertaste un valor inválido \n:(")
	segundos = int(input("Escribe la hora actual(sólo el número de segundos ej. 00): "))
	if segundos > 60:
		print("Error de Capa 8", "\nInsertaste un valor inválido \n:(")
	horas12, AmPm = cambiarFormato(horas)
	print("Son las: %dd:%dd:%dd" % (horas12, minutos, segundos), AmPm)

main()