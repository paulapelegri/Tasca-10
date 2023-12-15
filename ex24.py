def llegir_llista():
	#Prec: Llegeix una llista de números
	#Post: Retorna la llista llegida.
	b = []
	a = "a"
	while a != ".":
		a = input("Introdueixi el següent número: ")
		if a != ".":
			b.append(int(a))
		else:
			return b
def gran_llista(a):
    a.sort()
    return a[-1:]

# Programa principal
a = llegir_llista()
c = gran_llista(a)
print("El més gran de la llista {} és {}".format(a, c))
