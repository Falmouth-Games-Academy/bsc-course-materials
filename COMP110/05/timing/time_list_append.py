# Time appending to a list
# Write the results to a CSV file

import time
import random

rep_count = 1000

with open("results.csv", "wt") as f:
	for n in range(100, 100000, 100):
		print(n)

		# Create a list of n elements (not timed)
		my_list = []
		for i in range(n):
			my_list.append(random.randrange(1000))

		# Time appending elements to the list
		start_time = time.perf_counter()
		for repetition in range(rep_count):
			my_list.append(random.randrange(1000))

		end_time = time.perf_counter()
		total_time = end_time - start_time
		f.write("{0},{1}\n".format(n, total_time))
