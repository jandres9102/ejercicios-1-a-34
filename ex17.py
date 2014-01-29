from sys import argv
from os.path import exists
#old file is carro.txt new_field is camioneta.txt
script, old_file, new_file = argv

print "Copying from %s to %s" % (old_file, new_file)

# we could do these two on one line too, how?

indata = open(old_file).read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(new_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(new_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
