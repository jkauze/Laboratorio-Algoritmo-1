#"Prelab4Ejercicio1.py" Programa realizado por Alejandro Martinez (13-10839@usb.ve) y Jesus Kauze (12-10273@usb.ve)

#Avila Burger RETO

#El cliente pide el programa para solamente 5 participantes

#Programa que se encarga de verificar el ganador en una competencia de quien come mas hamburguesas

#Creamos nuestra Clase Competidor

class competidor():
	nombre=""
	hamburguesas=0

#Listamos cada uno de los participantes 

lista=[competidor(),competidor(),competidor(),competidor(),competidor()]

#bucle for que itere en la lista de los participantes, pidiendo nombre y numero de hamburguesas comidas

for estudiante in range(0,5):
	lista[estudiante].nombre=input("\nNombre del concursante: ")
	lista[estudiante].hamburguesas=int(input("Numero de hamburguesas comidas: "))
	assert(len(lista[estudiante].nombre) >= 1) #verifica que el nombre tenga al menos 1 caracter

#PRECONDICION: Verifica que el numero de hamburguesas de cada participante sea un numero positivo

assert(all(lista[i].hamburguesas >= 0 for i in range(0,5)))  

#Ordenamos nuestra lista de mayor a menor, dependiendo del numero de hamburguesas comidas
lista = sorted(lista, key=lambda competidor: competidor.hamburguesas, reverse = True)

#POSTCONDICION: verificamos que de primera posicion este el concursante que posea mayor numero de hamburguesas y asi mismo con la siguiente posicion con respecto a la siguiente

assert(all(lista[x].hamburguesas >= lista[x+1].hamburguesas for x in range(0,4)))

#Salida

print("\nEL GANADOR ES: " + lista[0].nombre + " CON " + str(lista[0].hamburguesas) + "\nLe siguen:")
for i in range(1,5):
	print(lista[i].nombre + " con " + str(lista[i].hamburguesas) + "
