def llegir_llista():
	#Prec: Llegeix una llista d’strings
	#Post: Retorna la llista llegida.
	b = []
	a = "a"
	while a != ".":
		a = input("Introdueixi una paraula, per acabar posi . :  ")
		if a != ".":
			b.append(a)
		else:
			return b
def longitud(a):
	return len(a)
# Ús de la funció
x = llegir_llista()
print("La longitud de la cadena donada és: ", longitud(x))
