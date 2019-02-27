#! /usr/bin/env python2.7

print(" funciones")

print(" para lograr realizar  programas para posteriormente  mandarlos a llamar en un programa  mas grande con nombre ya  dado")
print("al poner  nombre y dos parentesis")

print("el enunciado es def y dos parentesis")

print(" la funcion es el programa como tal, la llamada de funcion es cuando lo ejecutas")


print(" hay  variables globales como locales pero estas variables solo pueden ser una a la vez")

print(" estas variables automaticamente se vuelven locales")

print(" la variable de retorno es para volver inmediatamente a la funcion y usar la  expresion como un valor de retorno")

print(" no devuelve valores de la funcion")
print(" poner el nombre de la variable y antes colocarle global")
print(" es para iniciar una variable previa o para introducir una varible estilo comodin")
print(" la declaracion import random sirve para llamar la biblioteca con nombre random")
print(" para llamar a esta funcion tenemos que poner random.randint(a,b)")

print("tuplas y listas")

print(" los corchetes son usados para modificar y acceder elementos de una lista")

print(" nombre de la lista.insert(posicion, elemento)")

print(" el numero 3 lo multiplica por dos y lo divide entre 11 arrojando un numero entero")

print(" imprime el ultimo valor de la lista")

print(" imprime un rango empezando desde cero hasta el dos ")

print("  da la posicion del valor en la lista")

print(" agrega un valor a la lista")

print(" elimina un elemento de la lista")

print(" por medio del operador suma o a traves del metodo extend (). para replicar el comando se usa copy() para hacer listas")

print(" append() agrega un item al final de la lista, insert () inserta un item en una posicion dada, el primer argumento es el indice del item delante del cual se inserta.")


print(" elimina un elemento de la lista")

print(" se puede concatener a traves del operador suma o a traves del metodo extend (). para replicar el comando se usa copy() para hacer listas")

print(" append() agrega un item al final de la lista, insert () inserta un item en una posicion dada, el primer argumento coorresponde al indice del item delante del cual se inserta.")

print(" se altera una lista, las tuplas no se pueden alterar, una tupla puede ser utilizada como clave en un diccionario, la tupla consume menos espacio")

print("determinar si el numero ingresado es primo")

def testprime(r):
	t= int(2)
	band = "T"

	while((band == "T") and (t < r)):
        	if((t % r) == 0):
               	   band = "F"
        	else:
               	 t = t + 1
	if(band == "T"):
        	print("numero es primo")
	else:
        	print("numero no es primo")

testprime(int(input("introduzca numero")))			

print(" genere numeros primos menores o iguales en los naturales")

def prime(s):
	print( "numero",s)
	testprime(s)  
        
	x = int(2)	
	if s > 0:
	
		for i in range(2,s) :
			creciente = 2
			esprimo = True
			while esprimo and creciente < i:
				if i % creciente == 0:
					esprimo = False
				else:
					creciente += 1
		
			if esprimo:
				print(i,"es primo")
	else:
		print("el numero no es primo")
prime((int(input("numero"))))


print(" numeros gemelos primos")

def twinprime(g, f):
	comprobar = True
	
	a = 0
	if g > 0 and f > 0 and g != f:
		comprobar = False
	if g > f:
		g ^= f
		g ^= f
		g ^= f
	i = g
	while i <= f:
		creciente = 2
		esprimo = True
		while esprimo and creciente < i:
			if i % creciente == 0:
				esprimo = False
			else:
				 creciente += 1
		if esprimo and not a:
			a = i
		elif esprimo and a:
			b = i
			if b-a ==2:
				print(a,"y",b,"son gemelos")
			a = i
		i += 1
	else:
		if g == f:
			print("los numeros son iguales prueba con otros")

twinprime((int(input("numero"))), int(input("numero")))

print("programa regrese una lista con la descompensacion en potencias de primos")

lista=[]
def primo(l):

	for x in range (1,l):
		if (l%x==0 and x!=l and x!=1):
			return False
	return l

def lista_primos(t):
	
	for x in range(2,t):
		if primo(x)!=False:
			lista.append(x)
	return lista

def divisible(lista,m):
	for num in lista:
		if m%num==0:
			factores.append(num)
	return factores

def theoremArihtmetic(lista, num, factores_finales):

	divisibles=[]
	

	while True:
		salida1 = primo(num)
		if salida1!=False:
			factores_finales.append(salida1)
			break

		else:
			lista_primos(num)	
			divisibles=divisible(lista, num) 

			factores_finales.append(divisibles[len(divisibles)-1])
			num=num/divisibles[len(divisibles)-1]
	return factores_finales
		



factores_finales=[1]
lista=[]
factores=[]
num=input("Ingrese un numero: ")
print theoremArihtmetic(lista, num, factores_finales)

print("maximo comun divisor")

def mcm(x, y):

	resto = 0
	while(y > 0):
		resto = y
		y = x % y
		x = resto
	return x

n1 = int(input("numero"))
n2 = int(input("numero"))

print(mcm(n1, n2))

print("minimo comun multiplo")

def MCD(z, p):

	if z > p:
		mayor = z
	else:
		mayor = p
	while(True):
		if((mayor % z == 0) and (mayor % p == 0)):
			minimo = mayor
			break
		mayor += 1
	return minimo

num1 = int(input("numero"))
num2 = int(input("numero"))
print(MCD(num1, num2))
