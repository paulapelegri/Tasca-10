"""
a=[2, 3, 4]
print(a)

for j in (a):
    b=j*j*j
print(b)

for j in range(len(a)):
    a [j]=a[j]*a[j]*a[j]
print (a)

for j, e in enumerate(a):
    a[j]=e*e*e
print (a)
"""
""""
#dia 14/11/23 --> tuples
l=(1, 4, 2, (1, 3, 3), 3, 4, 2, 1)
def tercera_ocurrencia(l,e):
    a = l.count(e)
    if a==0:
        print("No hi ha ocurrenciès d'aquest element")
    elif a==1:
        print("La primera ocurrència de l'element està en la posició {}".format(l.index(e)))
    elif a==2:
        print("Hi ha més d'una ocurrència de {}".format(e))
        p = l.index(e)
        so = l.index(e,(p+1))
        print(so)
    elif a>2:
        print("Hi ha més de dues ocurrències de {}".format(e))
        p = l.index(e)
        so = l.index(e,(p+1))
        to = l.index(e,(so+1))
        print(to)
    else:
        print("Valor no vàlid")


#Programa principal
l=(1, 4, 2, (1, 3, 3), 3, 4, 2, 1)
x = int(input("Elegeixi l'element que vol cercar la 3ra ocurrencia: "))
tercera_ocurrencia(l,x)
"""

#Conjunt/set


#Diccionari
dic = {'nom': 'Joan', 'cognom': 'Ramis', 'edat': 30, 'telèfon': '971360133'}
for element in dic:
    print("La clau {} té el valor {}".format(element,dic[element]))