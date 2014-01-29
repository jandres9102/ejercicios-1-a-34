def  suma(a, b):
    print "suma entre %d + %d" % (a, b)
    return a + b

def resta(a, b):
    print "resta entre %d - %d" % (a, b)
    return a - b

def multiplica(a, b):
    print "multiplicacion entre %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "Divicion entre %d / %d" % (a, b)
    return a / b
def nom():
    print "digite su nombre:\n"
    n=raw_input()
    return n

print "prueba de las anteriores funciones"
nombre=nom()
edad = suma(10, 5)
estatura = resta(78, 4)
grosor = multiplica(90, 2)
iq = divide(100, 2)
print nombre
print " su edad: %d, estatura: %d grosor: %d, IQ: %d" % ( edad, estatura, grosor, iq)

total=suma(edad,resta(estatura,multiplica(iq,divide(iq,estatura))))
print "toal ", total, "facil"