##############################################
## This is the interface for the Word file  ##
## parser. It treats all non-alpha numeric  ##
## characters and converts them to whites-  ##
## space. Then it tokenizes into words      ##
## based on whitespace, into a dictionary.  ##
##                                          ##
## Written by: D. Reilly 2013               ##
##############################################

import sys
import imp
import time

def run():
	#Get the Filename from stdin
	file = raw_input('Enter File to parse: ')
	handle = None

	#Time the function
	start = time.clock()

	#Try to open the given file
	try:
		handle = open(file,'r')
	except IOError:
		print("%r Could not be opened!" % file)
		exit(0)
	
	#Try to read the file into a buffer
	contents = None
	try:
		contents = handle.read()
	except IOError as e:
		print("%r Could not be read!" % file)
		print ("\n" . format(e.errno, e.strerror))
		exit(0)
	finally:
		print "Contents Loaded."
		
	#Clean up after ourselves
	handle.close()
	
	if len(contents) is 0:
		print "Nothing to see here. Move along."
		exit(0)
		
	contents = cleanString(contents) # Clean up for tokenizer
	contentDict = loadDict(contents) # tokenize into words and load into Dictionary
	print "Dictionary Created. Analyzing Structure.\n"
	
	for word in contentDict:
		print word+" ",contentDict[word]
		
	done = (time.clock() - start)*1000
	print "\nFinished Process in %d ms\n" % done
	exit(0)
	
	
#convert offending chars to whitespace
def cleanString(string):
	whitespaces = ['!','@','#','$','%','^','&','(',')','[',']',':',';','-','_','.','/','\\',',','?','+','=','\"']
	
	#replace the above characters with a whitespace char
	for offender in whitespaces:
		string = string.replace(offender,' ')
		
	return string
	
	
#convert into "word" tokens and load into LL-RB-BST
def loadDict(string):
	words = string.split(' ') #tokenize on whitespace chars
	dict = {}
	
	for word in words:
		word = word.lstrip()
		word = word.rstrip()
		
		if len(word) >= 1:
			word = word.capitalize() # Normalize all words to proper names for comparison
			if word in dict:
				dict[word] += 1
			else:
				dict[word] = 1;
				
	return dict

	
if __name__=="__main__":
	run()