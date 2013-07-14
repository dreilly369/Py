#
#This class is a set of different sorting algorithms in Python. It currently has:
#
#Merge Sort
#Bubble Sort
#Cocktail Sort
#
#Written by: D. Reilly 2012
#

class MultiSorter():
	#recursively sort individual sub-sets of the packet
	def ms_sort(self,packet):
		if len(packet) > 1:
			#split the pack at about the middle
			n_sz = int(len(packet)/2)
			a_pack = packet[:n_sz]
			b_pack = packet[n_sz:]
			
			#Recursively sort each sub pack
			org_pack_a = self.ms_sort(a_pack)#Yay, Recursion 
			org_pack_b = self.ms_sort(b_pack)#Yay, Recursion
			
			#merge the recursive results back together
			n_pack = self.ms_merge(org_pack_a,org_pack_b)
			return n_pack
			
		else:
			return packet#Packets of size 1 are already sorted
			
	#Merge already sorted packets back together
	def ms_merge(self,pack_a,pack_b):
		goal = []
		while len(pack_a)>0 and len(pack_b)>0:
			if pack_a[0]<= pack_b[0]:#compare strings
				goal.append(pack_a.pop(0))
			else:
				goal.append(pack_b.pop(0))
		
		#we have now sorted all of one packet (or the other)
		#append the remainder of the final packet w/ consideration for order
		if len(pack_a)>0:
			while len(pack_a)>0:
				goal.append(pack_a.pop(0))
		else:
			while len(pack_b)>0:
				goal.append(pack_b.pop(0))

		return goal
		
	#A linear sorting algorithm
	def bubble_sort(self,pop,direction = 'ASC'):
		if direction == 'DESC':
			#Descending Order 
			done = False
			while done == False:
				i=0
				swapped = False
				while i < len(pop)-1:
					j = i+1
					print(pop[i],pop[j])
					if pop[i] < pop[j]:
						#swap the elements
						tmp = pop[i]
						pop[i] = pop[j]
						pop[j] = tmp
						swapped = True
					i += 1
				if swapped == False:
					done = True
		else:
			#Ascending order
			done = False
			while done == False:
				i=0
				swapped = False
				while i < len(pop)-1:
					j = i+1
					if pop[i] > pop[j]:
						#swap the elements
						tmp = pop[i]
						pop[i] = pop[j]
						pop[j] = tmp
						swapped = True
					i += 1
				if swapped == False:
					done = True
	

	#Cocktail sort is a bi-directional bubble sorting algorithm
	def cocktail_sort(self,pop,direction = 'ASC'):
		#Ascending Order
		if direction == 'DESC':
			done = False
			while done == False:
				i=0
				swapped = False
				while i < len(pop)-1:
					j = i+1
					if pop[i] > pop[j]:
						#swap the elements
						tmp = pop[i]
						pop[i] = pop[j]
						pop[j] = tmp
						swapped = True
						
					i += 1
				if swapped == False:
					done = True

				
				#Now go from the back to the front
				if done == False:
					swapped = False
					k = i
					while k > 0:
						l = k-1
						if pop[k] < pop[l]:
							#swap the elements
							tmp = pop[k]
							pop[k] = pop[l]
							pop[l] = tmp
							swapped = True
						k -= 1
					if swapped == False:
						done = True
		
		else:
			#Ascending Order
			done = False
			while done == False:
				i=0
				swapped = False
				while i < len(pop)-1:
					j = i+1
					if pop[i] > pop[j]:
						#swap the elements
						tmp = pop[i]
						pop[i] = pop[j]
						pop[j] = tmp
						swapped = True
						
					i += 1
				if swapped == False:
					done = True
		
				
				#Now go from the back to the front
				if done == False:
					swapped = False
					k = i
					while k > 0:
						l = k-1
						if pop[k] < pop[l]:
							#swap the elements
							tmp = pop[k]
							pop[k] = pop[l]
							pop[l] = tmp
							swapped = True
						k -= 1
					if swapped == False:
						done = True
				
		return pop
		