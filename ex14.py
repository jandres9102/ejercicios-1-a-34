from sys import argv

user_name, lives = argv
user_name=raw_input("what is your user name?")
lives=raw_input ("how many lives do you like to have?")
print "Welcome to Zork %s remember that you have %s lives"%(user_name,lives)
print"so now please write the name of your enemy",
enemy=raw_input()
print"""very good, so %s you have %s lives and your enemy will be %s
. now is time for play"""%(user_name,lives,enemy)
