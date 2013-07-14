#This is the interface for the Luhn Formula (Mod 10 algorithm)
#It takes an arbitrary ID and uses the LuhnFormula Class to validate or reject it.

#Written by: D. Reilly 2012

from luhn_formula import LuhnFormula
import sys
import imp

def run():
	mod = imp.find_module('luhn_formula')
	res = imp.load_module('luhn_formula.LuhnFormula',mod[0],mod[1],mod[2])
	lf = LuhnFormula()
	
	id = raw_input('Enter ID to validate: ')
	
	print('Checking %s' % id)
	if lf.checksumValidator(id) == 1:
		print('%s is valid' % id)
	else:
		print('%s is NOT valid' % id)
		
	exit(0)
	
if __name__=="__main__":
	run()