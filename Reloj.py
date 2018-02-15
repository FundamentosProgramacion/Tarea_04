#Autor Karla Fabiola Ramirez Martinez
#Descripcion: Convierte las horas en formato de 24hrs a 12


#Funcion que cambia la hora en formato de 14 horas a 12.
def calcularHora(h,m,s):
#Calcula cuando la hora es menor a 12 , no hay ningun cambio en ese caso
    if h<12:
        h="%.2i" %h
        h=str(h)
        s=":%.2i"%s
        hora=(h+":%.2i"%m+s)
        return hora
#Cuando h es = a 12( espero que este bien y no se refiera a que 12 y 24 ambas daran 0) acabo de darme cuenta que esta puedo juntarla con la de arriba pero la dejare asi
    elif h==12:
        h = str(h)
        s = ":%.2i" % s
        hora = (h + ":%.2i" % m + s)
        return hora
#Calcula cuando la hora es mayor a 12 y menor a 24
    elif h>12 and h<24:
        h=h-12
        h = str(h)
        s = ":%.2i" % s
        hora = (h + ":%.2i" % m + s)
        return hora
#La unica variable restante seria 24 ,
    else:
        h=0
        h = str(h)
        s = ":%.2i" % s
        hora = (h + ":%.2i" % m + s)
        return hora



#Funcion principal que recibe hora,minutos,segundos
def main():
    print("Dime la hora en formato de 24 horas")
    horas=int(input("Hora: "))
    minutos=int(input("Minutos: "))
    segundos=int(input("Segundos: "))
    formato12=calcularHora(horas,minutos,segundos)
    print(formato12," hrs")










main()