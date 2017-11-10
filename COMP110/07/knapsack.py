import itertools
import time
import random


class Item:
	def __init__(self, value, weight):
		self.value = value
		self.weight = weight
	
	def __repr__(self):
		return "Item(value=%r, weight=%r)" % (self.value, self.weight)


# Based on https://docs.python.org/2.7/library/itertools.html#recipes
# Powerset = set of all subsets
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return list(itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1)))


def brute_force(items, max_weight):
	# TODO
	return []


def greedy(items, max_weight):
	# TODO
	return []


def divide_and_conquer(items, max_weight, k = None):
	# TODO
	return []


def dynamic_programming(items, max_weight, k = None):
	# TODO
	return []


def random_item():
	""" Create a random item, for testing purposes """
	weight = random.randrange(1, 40)
	value = int(weight * random.uniform(1,5))
	return Item(value, weight)


def main():
	items = [Item(180, 20), Item(190, 20), Item(300, 30)]
	# items = [random_item() for i in xrange(10)]
	max_weight = 40
	
	start_time = time.clock()
	print brute_force(items, max_weight)
	print "Brute force time: %.6f seconds" % (time.clock() - start_time)
	
	start_time = time.clock()
	print greedy(items, max_weight)
	print "Greedy time: %.6f seconds" % (time.clock() - start_time)

	start_time = time.clock()
	print divide_and_conquer(items, max_weight)
	print "Divide and conquer time: %.6f seconds" % (time.clock() - start_time)

	start_time = time.clock()
	print dynamic_programming(items, max_weight)
	print "Dynamic programming time: %.6f seconds" % (time.clock() - start_time)


if __name__ == '__main__':
	main()
