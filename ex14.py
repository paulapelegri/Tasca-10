def gran_de_tres(a,b,c):
    if a>b>c:
        return a
    elif a>b==c:
        return a
    elif a>c>b:
        return a
    elif a==b>c:
        return a
    elif b>a>c:
        return b 
    elif a==b==c:
        return b 
    elif b>c>a:
        return b
    elif b>a==c:
        return b
    elif c>a>b:
        return c
    elif c>b>a:
        return c
    elif c>a==b:
        return c 
    
#Programa principal
a=int(input("introdueixi un número: "))
b=int (input("Introdueixi el segon número: "))
c=int(input("Introdueixi el tercer número: "))
d= gran_de_tres (a,b,c)
print("El número més gran és: {}".format(d))







