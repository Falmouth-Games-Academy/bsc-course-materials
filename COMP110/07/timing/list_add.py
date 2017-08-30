import time
import random

for i in xrange(1000):
	print i, ',',
	
	reps = 1000
	lists = []
	for rep in xrange(reps):
		lst = []
		for j in xrange(i):
			lst.append(random.random())
		lists.append(lst)
	
	start_time = time.clock()
	
	for lst in lists:
		lst.append(random.random())
	
	end_time = time.clock()
	
	print end_time - start_time
