a= "There are %d types of people." % 10#this variable  use %d for indicate that the value is an integer. place one
binary = "binary"#it declares a variable of type string
do_not = "don't" #it declares a variable of type string
b = "Those who know %s and those who %s." % (binary, do_not) #it declares a variable of type string but use %s  to indicate  that these places are of type string. place two

print a# print the variable a
print b# print the variable b

print "I said: %r." % a # print a string but put a string(in this case the variable a) inside a string. place three
print "I also said: '%s'." % b # print a string but put a string(in this case the variable b) inside a string. place four

hilarious = True #it declares a variable of type boolean
joke_evaluation = "Isn't that joke so funny?! %r" #it declares a variable of type string but put %r to replace any variable. place five

print joke_evaluation % hilarious #print the follow variable but also put hilarious like the variable that replace %r

w = "This is the left side of..." #it declares a variable of type string
e = "a string with a right side."#it declares a variable of type string

print w + e # this line concatenates the variables w an e for this reason this prin is long