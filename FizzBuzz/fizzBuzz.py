for i in range(1,101):
	if (i % 3 is 0 and i % 5 is 0):
		print("FizzBuzz")
	elif (i % 3 is 0 and i % 5 is not 0):
		print("Fizz")
	elif (i % 3 is not 0 and i % 5 is 0):
		print("Buzz")
	else:
		print i