a = 0
b = 0

for i in xrange(10):
	if i < 3 or i > 7:
		a += i
	else:
		b += i

print a
print b
