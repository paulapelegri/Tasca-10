def llegir_llista():
	#Prec: Llegeix una llista de paraules
	#Post: Retorna la llista llegida.
	b = []
	a = "a"
	while a != ".":
		a = input("Introdueixi la següent paraula: ")
		if a != ".":
			b.append(a)
		else:
			return b
def filtrar_paraules(a, num):
	b = list()
	i = 0
	for e in a:
		if num < len(e):
			b.append(e)
			return b

x = llegir_llista()
a = input("Indicar la longitud de les paraules que vols filtrar: ")
y = filtrar_paraules(x,int(a))
print("Les paraules de igual o més tamany de ", a, " són: ", y)

