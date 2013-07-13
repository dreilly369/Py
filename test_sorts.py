import sys
import time
import random
from multisorter import MultiSorter

#for testing the multi sorter class
def run():
	print("Recursive Merge sort")
	str_len = -1
	sample_size = -1
	run_wild = False
	while str_len == -1:
		str_len = raw_input("Enter string size (0 for random up to 10 letters):")#length of the string making up one member of the population	
	while sample_size == -1:
		sample_size = raw_input("Enter sample dataset size (0 for big random population):")#number of members of the population
		if sample_size == '0':
			sample_size = int(random.random()*1000)+10000
			print(sample_size)
			raw_input('>')
	
	pop = generate_samples(str_len,sample_size)#generate a population of strings
	print("Done Generating Samples")
	
	ms_pop = run_merge_sort(pop)
	print("Done Sorting Samples")
	
	show = raw_input("Show sorted population? 0/1:")
	if int(show)>0:
		print(ms_pop)
		
	#Now compare it to bubble sorting the same population
	print("Running Bubble sort on same unsorted set")
	bbl_pop = run_bubble_sort(pop)
	print("Done Sorting Samples")
	
	show = raw_input("Show sorted population? 0/1:")
	if int(show)>0:
		print(bbl_pop)
	exit(0)
	
#This function generates sz random strings of length ln.
#it doesn't account for Capitolization at this time.
#used for testing the sorting functions in the MultiSorter class
def generate_samples(ln,sz):
	alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	i = 0
	sample = []
	#loop to create variable number of strings
	while i<int(sz):
		j = 0
		str = []
		if int(ln)<1:
			nln = int(random.random()*7)+3
		else:
			nln = int(ln)
		
		while j<nln:
			index = random.random()*(len(alphabet)-1)#Set the random range to the length of the alphaet being used
			#Create random string
			str.append(alphabet[int(index)])#Add char to list
			j = j+1
		i = i+1
		str = ''.join(str)#Join list into string
		sample.append(str)
		#print(str)
	
	return sample	
			
			
def sort_timer(func):
    def wrapper(*arg):
        t1 = time.time()
        res = func(*arg)
        t2 = time.time()
        print '%s took %0.3f ms' % (func.func_name, (t2-t1)*1000.0)
        return res
    return wrapper

@sort_timer
def run_merge_sort(pop):
	sorter = MultiSorter()
	ms_pop = sorter.ms_sort(pop)
	return pop

@sort_timer
def run_bubble_sort(pop):
	sorter = MultiSorter()
	bbl_pop = sorter.bubble_sort(pop,'ASC')
	return pop


if __name__=="__main__":
	run()