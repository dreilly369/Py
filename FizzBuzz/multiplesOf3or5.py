the_sum = 0;
for i in range(1,1000):
	if i % 3 == 0 or i % 5 == 0:
		the_sum += i
		
print("The sum is: %d" % the_sum)