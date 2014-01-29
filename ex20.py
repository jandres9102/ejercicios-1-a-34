from sys import argv

script, transport = argv #on this line its declared the number of arguments to use transport will be the file carro.txt

def print_all(f): #this function  print all the dates of a file 
    print f.read()

def rewind(f):  #this function moving to the start of line
    f.seek(0)

def print_a_line(line_count, f): #this function print only a line
    print line_count, f.readline()

current_file = open(transport)

print "todo el documento\n"
print_all(current_file)

print "ahora regresamos a la primer linea ."
rewind(current_file)

print "finalmente imprimimos 1 linea:"

current_line = 1
print_a_line(current_line, current_file)
