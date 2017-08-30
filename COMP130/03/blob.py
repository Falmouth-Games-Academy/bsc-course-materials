import codecs

last_indent = 0

fin = codecs.open('inheritance.txt', 'rt', 'utf-8')
fout = codecs.open('inheritance.tex', 'wt', 'utf-8')

for line in fin:
	indent = 0
	for c in line:
		if c == '\t':
			indent += 1
		else:
			break
	
	line = line.strip()
	
	if indent > last_indent:
		for i in xrange(indent - last_indent):
			fout.write('\t' * (last_indent + i) + r'\begin{itemize}' + '\n')
	elif indent < last_indent:
		for i in xrange(last_indent - indent):
			fout.write('\t' * (last_indent - i - 1) + r'\end{itemize}' + '\n')
	
	if indent == 0:
		fout.write(r'\end{frame}' + '\n\n')
		fout.write(r'\begin{frame}{' + line[2:] + '}' + '\n')
	else:
		fout.write('\t' * indent + r'\pause\item ' + line[2:] + '\n')
	
	last_indent = indent

