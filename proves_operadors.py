
"""
#a = [3, (1,3), [4,5,6], 7, "hola",'0',0,1]
#elif:

a='e'
if a == 'b':
    print("a és b")
elif a=='c':
    print("a és c")
elif a=='d':
    print("a és d")
elif a=='e':
    print("a és e")
else:
    print("a no val res")
#match/case:
a='e'
match a:
    case 'b':
        print("a és b")
    case 'c':
        print("a és c")
    case'd':
        print("a és d")
    case'e':
        print("a és e")
    case other:
        print("a no val res")

a = [3, (1,3), [4,5,6], 7, "hola",'0',0,1]
if 'a' in a:
    print("a és dins la llista {}".format(a))
elif 'holas' in a:
    print("hola és dins la llista {}".format(a))
elif "0b" in a:
    print("Aixo s'executa si és ceta la condició")
elif 'b' in a:
    print("b és dins {}".format(a))
else:
    print("dins a hi ha {}".format(a))




a = [2, 3, 4]
b = [2, 5, 6, 10]
c=[]
for i in range(len(a)):
    c.append(a[i]*b[i])
print("La multiplicació de la llista {} per la llista {} és {}".format(a, b, c))




a=int(input("Introdueixi el primer valor: "))
b=int(input("Intrpdueixi el segon valor: "))
if a ==b:
    print("El nombre {} i {} són iguals".format(a,b))
else:
    print("El nombre {} i {} no són iguals".format(a,b))



if a % 2==0:
    print("El nombre {} és parell".format(a))
else:
    print("El nombre {} no es parell".format(a))
c=a/b
print("Loperació de {} i {} és {}".format(a,b,c))
"""


#bucle
for i in range(1,11):
    print(i)
#con while
i = 0
while i<10:
    print(i)
    if i==5:
        break;     #se rompe el bucle
    i+=1