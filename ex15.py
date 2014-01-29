from sys import argv
#this program shows you the conveyance that you prefer if you want run its 
#you have to wrhite python ex15.py carro.txt
script, conveyance = argv

txt = open(conveyance)
print "you choose like conveyance: %r"%conveyance
print txt.read()
print "Type the conveyance again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()