# Time creation of a list of random elements
# Write the results to a CSV file

import time
import random

rep_count = 10

with open("results.csv", "wt") as f:
	for n in range(10, 10000, 10):
		print(n)

		start_time = time.perf_counter()
		for repetition in range(rep_count):
			# Create a list of size n
			my_list = []
			for i in range(n):
				my_list.append(random.randrange(1000))

		end_time = time.perf_counter()
		total_time = end_time - start_time
		f.write("{0},{1}\n".format(n, total_time))
