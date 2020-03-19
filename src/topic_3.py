#!/usr/bin/python

def addition (mylist):
	sum = 0
	for i in range(len(mylist)):
		sum = sum + mylist[i]
	print "Sum is: " + str(sum)

while input != "3":
	print "\nChoose an option\n(1) Addition\n(2) Quit"

	input = raw_input()

	if input == "1":
		print "\nEnter three numbers"
		num1 = int(raw_input('First: '))
		num2 = int(raw_input('Second: '))
		num3 = int(raw_input('Third: '))
		mylist = [num1, num2, num3]
		addition(mylist)
	elif input == "2":
		print "Exiting program!"
		quit()
	else:
		print "Invalid input. Please try again."

