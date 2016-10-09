#Programa Que almacena 10 enteros y los suma

#Variables

lista=[] #Lista vacia donde se guardaran los valores
Sumatoria=0 #variable donde se guardara la sumatoria de lista

#Bucle for para introducir los digitos

for i in range(1,11):
	lista.append(int(input("Introduzca el valor numero " +str(i) + " : ")))

#Precondicion (verificamos que sea tipo entero el valor introducido)

assert(all(x for x in lista if type(x)==int and x!=0))

#Bucle para la sumatoria

for i in lista:
	Sumatoria += i

#Postcondicion (verificamos que la suma sea la sumatoria correcta)

assert(Sumatoria== sum(x for x in lista))
print("la Sumatoria de los valores " + str(lista) + "es: " + str(Sumatoria))
