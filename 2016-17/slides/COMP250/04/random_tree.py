import random

labels = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

next_index = 1

def random_tree(indent, max_depth):
	global labels
	num_children = random.randrange(4)
	if max_depth <= 0:
		num_children = 0
	label = random.choice(labels)
	labels.remove(label)
	print '%s[.%s' % (indent, label)
	for i in xrange(num_children):
		random_tree(indent + '\t', max_depth-1)
	print '%s]' % indent

random_tree('', 4)
