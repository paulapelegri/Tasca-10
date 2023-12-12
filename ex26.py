def filtrar_paraules(a, num):
    b = list()
    i = 0
    for e in a:
        if num < len(e):
            b.append(e)
    return b

x = ["hola caracola", "de eso nada monada", "mecachis", "relampago", "de oca en oca y tiro porque me toca", "zzzz"]
a = input("Indicar la longitud de les paraules que vols filtrar: ")
y = filtrar_paraules(x,int(a))
print("Les paraules de igual o més tamany de ", a, " són: ", y)
