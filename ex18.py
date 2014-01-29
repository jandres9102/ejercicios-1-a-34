# this one is like your scripts with argv
def colores(*args):
    col1, col2, col3 = args
    print "color1: %r,\n color2: %r,\n color3: %r" % (col1, col2,col3)

# ok, that *args is actually pointless, we can just do this
def dos_primeros_colores(col1, col2):
    print "color1: %r, color2: %r" % (col1, col2)

# this just takes one argument
def ultimo_color(col3):
    print "arg1: %r" % col3

# this one takes no arguments
def print_none():
    print "I got nothin'."


colores("amarillo","azul","rojo")
dos_primeros_colores("blanco","verde")
ultimo_color("naranja")
print_none()