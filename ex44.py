suma=0
a = input("Introdueix un número: ")
print("{} té {} dígits".format(a,len(a)))
for i,e in enumerate(a):
	if i%2==0:
    		print("El número {} és un parell del {}".format(i,e))
