#Valores inciales
N = int(input('\n\n\nEste algoritmo calcula la suma de los factoriales desde 0 hasta N.\n\nA continuacion introduzca el numero: '))
suma, fact, k = 0,1,0

#Pre
assert(N >= 0 and 0<=k<=N)

#Algo
while k<=N:
	if k>0:
		fact *= k
	suma += fact
	k += 1

#Funcion que definio el profesor que aparece creada por otro en: http://stackoverflow.com/questions/595374/whats-the-python-function-like-sum-but-for-multiplication-product
def prod( iterable ): 
	p= 1 
	for n in iterable: 
		p *= n 
	return p 

#Post
assert(suma == sum(prod(range(1,i+1)) for i in range(0,N+1)))

#Salida
print("La suma de los factoriales es:", suma)