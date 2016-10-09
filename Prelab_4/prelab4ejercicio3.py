#"Prelab4Ejercicio3.py" Programa realizado por Jesus Kauze (12-10273@usb.ve) y Alejandro Martinez (13-10839@usb.ve)

#Programa que calcula el promedio de edades y de indice de un grupo de N estudiantes

#Variables

suma_indice=0
suma_edad=0
promedio_edad=0
promedio_indice=0

#Creacion de la clase con la cual sera almacenado los datos de los Estudiantes

class Estudiante():
	nombre=""
	indice=0
	edad=0

N = int(input("Introduzca el numero de estudiantes que posee el grupo: "))

#Precondicion(que el numero de estudiantes sea mayor que 1)

assert(N>1)

#arreglo de estudiantes

grupo = [Estudiante() for x in range(N)]

#Bucle para introducir datos del grupo de estudiantes

for x in range(N):
	grupo[x].nombre= input("\nnombre del estudiante " + str(x) + "? ")
	grupo[x].indice= float(input("indice del estudiante " + str(x) + "? "))
	grupo[x].edad= int(input("edad del estudiante " + str(x) + "? "))
	assert(len(grupo[x].nombre)>=1 and grupo[x].edad > 0 and grupo[x].indice>0) #Verificacion de que el nombre tenga al menos 2 caracteres y la edad e indice sean positivo
  
#promedio de las edades

for y in range(N):
	suma_edad += grupo[y].edad
promedio_edad=suma_edad/N

#promedio de los indices

for z in range(N):
	suma_indice += grupo[z].indice
promedio_indice = suma_indice/N

#POSTCONDICION (verificar que la sumatoria de edades y indices es correcta)

assert(promedio_edad == sum(grupo[x].edad for x in range(N))/N and promedio_indice== sum(grupo[x].indice for x in range(N))/N)

#Salida

print("\nEL promedio de las EDADES del grupo es de: " + str(promedio_edad))
print("\nEL promedio de los INDICES del grupo es de: " + str(promedio_indice))
