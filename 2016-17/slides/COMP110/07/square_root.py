square_root = {}
for i in xrange(30):
    square_root[i*i] = i

for key, value in square_root.iteritems():
    print "The square root of", key, "is", value
