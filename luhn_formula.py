#Class for applying the Luhn(Mod 10) Algorithm to generate or validate a check sum
#Written by: D. Reilly 2012

class LuhnFormula:
		
	def doubleDigitAndSum(self,digit):
		#double a number, 0-9 and if it is >10 sum the resulting 2 digits
		dbl = int(digit)*2

		if dbl > 9:
			str_dbl = str(dbl)
			new_val = int(str_dbl[0])+int(str_dbl[1])
			return new_val
		else:
			return dbl
			
			
		

	def checksumValidator(self,id):
		id_length = len(id)
		checksum = []
		sum = 0
		#Handle ID of even length
		if id_length % 2 == 0:
			i = 0
			while i < id_length:
				#if we are on an odd digit it double and sum
				if(i%2!=0):
					n_val = self.doubleDigitAndSum(id[i])
					print(n_val)
					checksum.append(n_val)
				else:
					checksum.append(int(id[i]))
				i += 1
				
			#print("Checksum: ", ''.join(checksum,',')
		else:
			#Handle ID of odd length
			i = 0
			while i < id_length:
				#if we are on an even digit it double and sum
				if(i%2==0):
					n_val = self.doubleDigitAndSum(id[i])
					checksum.append(n_val)
				else:
					checksum.append(int(id[i]))
				i += 1
			
			
		for i in checksum:
			sum += int(i)
		
		if sum % 10 == 0:
			return 1 
		else:
			return 0
