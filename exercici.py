
def canvi(l,m,n):
    print("1) {}{}\n {}".format(l,m,n))
    l="Auéu, "
    m="Joan"
    n="Que vagi bé"
    print("2) {}{} \n {}".format(l,m,n))
a="Hola, "
b="Ramis."
c="Com estàs?"
print("El valor de la variable abans de canviar és: {}{} \n {}".format(a, b, c))
canvi(a,b,c)
print("El valor de la variable després de canviar és: {}{} \n {}".format(a, b, c))





"""
def canvi(l): #definim canvi com una variable
    x=int(input("Introdueixi la posició a modificar: ")) #Quan surti a la terminal s'ha d'escriure un numero per "int"
    l[x]=input("Introdueixi eñ valor a inserir: ") #cambia un nombre de la llista en la posicio que l'has dit abans
#Programa principal
a=[3, 4, 5, 6, 7, 8, 'a', (1, 2), [3, 4], 10] #s'ha llista creada es el valor a
print("El valor de la llista abans de canviar és: {}".format(a)) #ens escriu a la consola la llista sense modificar
canvi(a) #crides la funció
print("El valor de la llista després de canviar és: {}".format(a)) #es mostra a la terminal lo que has modificat a la llista
"""