import random

words = [w.strip() for w in open("words.txt", "rt")]
words = words[words.index("---")+1 : ]
words = [w.upper() for w in words if w.isalpha()]

n = 5
words = [w for w in words if len(w) == n]

def similarity(a,b):
	n = 0
	for i in xrange(len(a)):
		if a[i] == b[i]:
			n += 1
	return n

secret = random.choice(words)
print secret

for s in xrange(n+1):
	print s, sum(1 for w in words if similarity(w, secret) == s)

# desired_similarity = [0,0,0,0,1,1,1,1,1,1,2,2,2,2,3,3,4]

# for s in desired_similarity:
	# a = None
	# tries = 100
	# while a != s and tries > 0:
		# option = random.choice(words)
		# a = similarity(secret, option)
		# tries -= 1
	# print secret, option, a
