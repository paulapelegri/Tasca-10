def paraula_mes_gran(a):
	sorted(a,key=lambda a:len(a))
	return a[len(a)-1]

# Programa principal
x = ["hola", "Adeu", "fins demá!", "tinc son", "Alfons XIII va ser declarat major d'edat quant tenia setze anys"]
print("La paraula més llarga és: ", paraula_mes_gran(x))
