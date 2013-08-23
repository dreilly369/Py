def buildFibSeq(limit):
	seq = [1,1,2] # A hack taking advantage of domain knowledge ;)
	i = seq[-1]
	print i
	while i < limit:
		j = seq[-2]
		next = j + i
		seq.append(next)
		i = seq[-1]
	return seq
	

def sumEvenDigits(seq):
	print seq
	sum = 0
	for n in seq:
		if n % 2 is 0:
			sum += n
	
	return sum

def main():
	fibseq = buildFibSeq(4000000)
	sum = sumEvenDigits(fibseq)
	print("Sum: %d" % sum)
	
if __name__ == "__main__":
	main()