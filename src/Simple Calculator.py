#!/usr/bin/python
while input != 6:
	print "(1) Addition\n(2) Subtraction\n(3) Multiplication\n(4) Division\n(5) Quit\n"
	input=int(raw_input('Input:'))
	if input == 1:
		print "Adding Numbers:"
		first  = int(raw_input('Enter First Number: '))
		second = int(raw_input('Enter Second Number: '))
		addEquals = first + second
		print str(first) + " + " + str(second) + " = " + str(addEquals)

	elif input == 2:
		print "Subtracting Numbers:"
		first  = int(raw_input('Enter First Number: '))
		second = int(raw_input('Enter Second Number: '))
		subEquals = first - second
		print str(first) + " - " + str(second) + " = " + str(subEquals)

	elif input == 3:
		print "Multiplying Numbers:"
		first  = int(raw_input('Enter First Number: '))
		second = int(raw_input('Enter Second Number: '))
		mulEquals = first * second
		print str(first) + " * " + str(second) + " = " + str(mulEquals)

	elif input == 4:
		print "Dividing Numbers:"
		first  = int(raw_input('Enter Dividened: '))
		second = int(raw_input('Enter Divisor: '))
		divEquals = first / second
		print str(first) + " / " + str(second) + " = " + str(divEquals)

	elif input == 5:
		print "Exiting program!"
		quit()

	else:
		print "Not a proper option"
