def gran_llista(a):
	a.sort()
	return a[-1:]

# Programa principal
a = [7, 40, 34, 14, 4, 9, 7, 43]
c = gran_llista(a)
print(c[0])
