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
	best = []
	best_value = 0
	
	for subset in powerset(items):
		weight = sum(item.weight for item in subset)
		value = sum(item.value for item in subset)
		if weight <= max_weight and value > best_value:
			best = subset
			best_value = value
	
	return best


def greedy(items, max_weight):
	sorted_items = sorted(items, key=lambda item: float(item.value) / float(item.weight), reverse=True)
	result = []
	weight = 0
	for item in sorted_items:
		if item.weight + weight <= max_weight:
			result.append(item)
			weight += item.weight
	return result


def divide_and_conquer(items, max_weight, k = None):
	if k is None:
		k = len(items)-1
	if k < 0:
		return []
	
	solution = divide_and_conquer(items, max_weight, k-1)
	if items[k].weight <= max_weight:
		solution_with_k = divide_and_conquer(items, max_weight - items[k].weight, k-1) + [items[k]]
		if sum(item.value for item in solution_with_k) > sum(item.value for item in solution):
			solution = solution_with_k
	
	return solution


memo = {}


def dynamic_programming(items, max_weight, k = None):
	global memo
	
	if k is None:
		k = len(items)-1
		memo = {}
	
	if k < 0:
		return []
	
	try:
		return memo[max_weight, k]
	except KeyError:
		pass
	
	solution = dynamic_programming(items, max_weight, k-1)
	if items[k].weight <= max_weight:
		solution_with_k = dynamic_programming(items, max_weight - items[k].weight, k-1) + [items[k]]
		if sum(item.value for item in solution_with_k) > sum(item.value for item in solution):
			solution = solution_with_k
	
	memo[max_weight, k] = solution
	return solution


def random_item():
	weight = random.randrange(1, 40)
	value = int(weight * random.uniform(1,5))
	return Item(value, weight)

def main():
	#items = [Item(180, 20), Item(190, 20), Item(300, 30)]
	items = [random_item() for i in xrange(80)]
	max_weight = 40
	
	#start_time = time.clock()
	#print brute_force(items, max_weight)
	#print "Brute force time:", time.clock() - start_time, "seconds"
	
	start_time = time.clock()
	print greedy(items, max_weight)
	print "Greedy time:", time.clock() - start_time, "seconds"

	start_time = time.clock()
	print divide_and_conquer(items, max_weight)
	print "Divide and conquer time:", time.clock() - start_time, "seconds"

	start_time = time.clock()
	print dynamic_programming(items, max_weight)
	print "Dynamic programming time:", time.clock() - start_time, "seconds"


if __name__ == '__main__':
	main()
