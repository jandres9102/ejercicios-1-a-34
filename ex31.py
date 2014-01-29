print "Vacations, what you go to do, go to travell #1 or stay at home #2?"

plan = raw_input("> ")

if plan == "1":
    print "Do you go to travell in car or in airplane?"
    print "1. Take the car."
    print "2. Take the airplane."

    transport = raw_input("> ")

    if transport == "1":
        print "you will arrive in 3 hours!"
    elif transport == "2":
        print "you will arrive in 8 hours!"
    else:
        print "i don know when you go to arrive"

elif plan == "2":
    print "You will be very boring"

else:
	print "what you going to do?"
   