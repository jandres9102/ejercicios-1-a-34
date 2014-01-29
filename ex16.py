from sys import argv

script, conveyance = argv

print "Wellcome to design of your %r." % conveyance
print "now we are going to erase all the dates"

print "Opening the file..."
robot = open(conveyance, 'w')

print "Truncating the file.  Goodbye!"
robot.truncate()

print "Now I'm going to ask you for the parts"

line1 = raw_input("color")
line2 = raw_input("type car")

print "I'm going to write these to the design."

robot.write(line1+" car")
robot.write("\n")
robot.write("type"+line2)


print "And finally, we close it."
robot.close()