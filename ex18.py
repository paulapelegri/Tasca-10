def invertir(a):
	#Prec: invertir una cadena de lletres.
	#Post: Retorna la cadena invertida.
	b = list(a)
	c = b[::-1]
	r = "".join(c)
	return r
# Programa principal
s="Això és una cadena que s'ha de girar"
print("La cadena: ", s, " girada és: ",invertir(s))
		
