def menu_principal():
    print( """
        Menu principal:
        1. Calculadora enters
        2. Calculadora reals
        3. Sortir
        """
            )
    x  = int(input("Elegeix una opció: "))
    if x>0 and x<4:
        return x
    else:
        return 0

#Programa principal
a = menu_principal()
print(a)
