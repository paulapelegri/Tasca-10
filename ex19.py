def invertir(a):
    b = list(a)
    c = b[::-1]
    r = "".join(c)
    return r

def es_palindrom(a):
    c = invertir(a)
    x = 0
    for i in range(len(a)):
        if a[i]!=c[i]:
            x+=1
        if x==0:
            return True
        else:
            return False
        
# Programa Principal
x = input("Introdueix una paraula per a veure si és palíndrom o no: ")
if es_palindrom(x):
	print("La paraula ", x, " a l'inrevés ", invertir(x), " és un palíndrom.")
else:
	print("La paraula ", x, " a l'inrevés ", invertir(x), " no és un palíndrom.")
