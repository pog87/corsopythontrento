import sys

print("Benvenuto!")

a=sys.argv[1]
b=sys.argv[2]

a=int(a)
b=int(b)

print ("L'ipotenusa del triangolo di cateti lunghi %d e %d" % (a,b))
print ("rullo di tamburi...")

c=(a**2 + b**2)**.5

print(c)