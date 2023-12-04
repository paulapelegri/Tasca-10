
def menu_principal():
    print( """
        Menú principal:
        1. Calculadora enters
        2. Calculadora reals
        3. Canvi de base
        4. Sortir
        
    """)
    
    a  = int(input("Elegeix una opció: "))
    return a
def calculadora_enters():
    op = 1
    while op>0:
        print("""
              Menú enters
              1. Sumar
              2. Restar
              3. Multiplicar
              4. Dividir
              5. Sortir
        """)
        op = int(input("Elegeix una opció: "))
        match op:
            case 1: #Sumar
                x = int(input("Introdueixi el primer número: "))
                y = int(input("Introdueii el segon número: "))
                print("{} + {} = {}". format(x,y, x+y))
            case 2: #Restar 
                x = int(input("Introdueixi el primer número: "))
                y = int(input("Introdueii el segon número: "))
                print("{} - {} = {}". format(x,y, x-y))
            case 3: #Multiplicar
                x = int(input("Introdueixi el primer número: "))
                y = int(input("Introdueii el segon número: "))
                print("{} * {} = {}". format(x,y, x*y))
            case 4: #Dividir
                x = int(input("Introdueixi el primer número: "))
                y = int(input("Introdueii el segon número: "))
                print("{} / {} = {}". format(x,y, x/y))
            case 5: #Sortir
                print("Adeú, ja tornaràs a la calculadora inicial \n\n")
                op=-1

def calculadora_reals():
    q = 2
    while q>0:
        print("""
            Menú reals
            1. Sumar
            2. Restar
            3. Multiplicar
            4. Dividir
            5. Sortir
        """)
        q = int(input("Elegeixi una opció: "))
        match q:
            case 1: #Sumar
                x = float(input("Introdueixi el primer número: "))
                y = float(input("Introdueii el segon número: "))
                print("{} + {} = {}". format(x,y, x+y))
            case 2: #Restar
                x = float(input("Introdueixi el primer número: "))
                y = float(input("Introdueii el segon número: "))
                print("{} - {} = {}". format(x,y, x-y))
            case 3: #Multiplicar
                x = float(input("Introdueixi el primer número: "))
                y = float(input("Introdueii el segon número: "))
                print("{} * {} = {}". format(x,y, x*y))
            case 4: #Dividir
                x = float(input("Introdueixi el primer número: "))
                y = float(input("Introdueii el segon número: "))
                print("{} / {} = {}". format(x,y, x/y))
            case 5: #Sortir
                print("Adeú, ja tornaràs a la calculadora inicial \n\n")
                q=-1

#Funcions de canvi de base

#de decimal a binari, octal i hexadecimal
def dectobin(numero):
    #precondicio: numero sigu un enter
    #postcondicio: retorna el valor de l'enter en binari
    return bin(numero)
def dectooct(numero):
    #precondicio: numero sigu un enter
    #postcondicio: retorna el valor de l'enter en ostal
    return oct(numero)
def dectohex(numero):
    #precondicio: numero sigu un enter
    #postcondicio: retorna el valor de l'enter en hexadecimal
    return hex(numero)

#de binari a octal, decimal, hexadecimal
def bintooct(numero):
    #precondicio: numero sigu una cadena de caràcters i en binari
    #postcondicio: retorna el numero en octal
    a=int(numero,2)
    return dectooct(a)
def bintodec(numero):
    #precondicio: numero sigu una cadena de caràcters i en binari
    #postcondicio: retorna el numero en decimal
    a=int(numero,2)
    return a
def bintohex(numero):
    #precondicio: numero sigu una cadena de caràcters i en binari
    #postcondicio: retorna el numero hexadecimal
    a=int(numero,2)
    return dectohex(a)

#de octal a binario, decimal, hexadecimal
def octtobin(numero):
    #precondicio: numero sigu una cadena de caràcters i en octal
    #postcondicio: retorna el numero en binari
    a=int(numero,8)
    return dectobin(a)
def octtodec(numero):
    #precondicio: numero sigu una cadena de caràcters i en octal
    #postcondicio: retorna el numero en decimal
    a=int(numero,8)
    return a
def octohex(numero):
    #precondicio: numero sigu una cadena de caràcters i en octal
    #postcondicio: retorna el numero en hexadecimal
    a=int(numero,8)
    return dectohex(a)

#de hexadecimal a binari, octal, decimal
def hextonum(hex): #passa qualsevol hexadecimal a un nombre
    #hex es una cadena de caracters
    #retorna un nombre entre 0 i 15
    pnum = {
        "f": 15,
        "e": 14,
        "d": 13,
        "c": 12,
        "b": 11,
        "a": 10
    }
    if hex in pnum:
        return pnum[hex]
    else:
        return int(hex)
    
def hextodec2(hex):
    hex = hex.lower() 
    hex = hex[::-1]
    decimal = 0
    posicio = 0
    for digit in hex:
        valor = hextonum(digit)
        elevat = 16 ** posicio 
        pnum = elevat * valor
        decimal += pnum
        posicio += 1
    return decimal 
def hextobin(numero):
    a=int(numero,16)
    return dectobin(a)
def hextooct(numero):
    a=int(numero,16)
    return dectooct(a)
def hextodec(numero):
    a=hextodec2(numero)
    return a
def canvis_base():
    q = 1
    while q>0:
        print("""
            Menú canvis de base
            1. Donat un binari ho passem a tota la resta
            2. Donat un octal el passem a tota la resta
            3. Donat un decimal ho passem a tota la resta
            4. Donat un hexadecimal ho passem a tota la resta
            5. Sortir
        """)
        q = int(input("Elegeixi una opció: "))
        match q:
            case 1: #Binari to
                b = input("Introdueixi el número binari: ")
                o = bintooct(b)
                d = bintodec(b)
                h = bintohex(b)
                print("El número binari {} és: \n oct -> {} \n dec -> {} \n hex -> {}".format(b,o,d,h))
                #\n = salto de línea(como un puto y aparte)
            case 2: #octal to
                o = input("Introdueixi el número octal: ")
                b = octtobin(o)
                d = octtodec(o)
                h = octohex(o)
                print("El número octal {} és: \n bin -> {} \n dec -> {} \n hex -> {}".format(o,b,d,h))
            case 3: #Decimal to
                d = int(input("Introdueixi el número decimal: "))
                b = dectobin(d)
                o = dectooct(d)
                h = dectohex(d)
                print("El número decimal {} és: \n bin -> {} \n oct -> {} \n hex -> {}".format(d,b,o,h))
            case 4: #hexadecimal to
                h = input("Introdueixi el número hexadecimal: ")
                b = hextobin(h)
                o = hextooct(h)
                d = hextodec(h)
                print("El número hexadecimal {} és: \n bin -> {} \n ost -> {} \n dec -> {}".format(h,b,o,d))
            case 5: #Sortir
                print("Adeú, ja tornaràs a la calculadora inicial \n\n")
                q=-1
#Programa principal
a = 1
while a>0:
    a = menu_principal()
    match a:
        case 1:
            calculadora_enters()
        case 2:
            calculadora_reals()
        case 3:
            canvis_base()
        case 4:
            a = -1
        case other:
            print("Opció no vàlida torni al menú principal: \n")
