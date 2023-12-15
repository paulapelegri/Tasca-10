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
def paraula_mes_gran(a):
	sorted(a,key=lambda a:len(a))
	return a[len(a)-1]

# Programa principal
x = llegir_llista()
print("La paraula més llarga és: ", paraula_mes_gran(x))

