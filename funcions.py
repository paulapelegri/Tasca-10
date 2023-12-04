def intercanvi(a,b):
    return b,a
x="a"
y="b"
print("El valor d'x és {} i el d'y és {}".format(x,y))
x,y=intercanvi(x,y)
print("Després de l'intercanvi, el valor d'x és {}".format(x,y))
