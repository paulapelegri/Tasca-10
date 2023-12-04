
#a = [3,4,'a',[3,2],(1,2,3),"Hola"]
#print(len(a))
#a=range (5,9)
a = 1
while a>0:
    print( """
    Menú
    1. Mirar si un número és senar o parell
    2. Sortir
    """)
    a = int(input("Seleccini una opcció: "))
    match a:
        case 1:
            x = int(input("Escriu un nombre: "))
            if x % 2 == 0:
                print("És parell")
            else:
                print("No és parell")
        case 2:
            a = 0
            
