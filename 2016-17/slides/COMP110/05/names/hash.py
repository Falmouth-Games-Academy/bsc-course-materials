hashes = {}

for name in open('names.txt', 'rt'):
	name = name.strip()
	surname, firstname = name.strip().upper().split(', ')
	
	letters = [ord(c) - ord('A') + 1 for c in surname + firstname]
	print name, letters
	hash = sum(letters)
	
	record = (name, letters)
	
	if hash in hashes:
		hashes[hash].append(record)
	else:
		hashes[hash] = [record]

f = open('../hashtable.tex', 'wt')
for hash in sorted(hashes.keys()):
	hs = hashes[hash]
	names = [n for (n,l) in hs]
	letters = [repr(l) for (n,l) in hs]
	
	f.write('%i' % hash)
	for name in names:
		f.write(r" & %s \\" % name)
	f.write(r"\hline")

