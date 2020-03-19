#!/usr/bin/python

while input != "3":
	print "\nChoose an option\n(1) Find Sumt\n(2) Quit"

	input = raw_input()

	if input == "1":
		print "\nEnter two numbers"
		num1 = int(raw_input('First: '))
		num2 = int(raw_input('Second: '))
		sum = num1 + num2
		print "\nSum is " + str(sum)
	elif input == "2":
		print "Exiting program!"
		quit()
	else:
		print "Invalid input. Please try again."
		input = raw_input()
