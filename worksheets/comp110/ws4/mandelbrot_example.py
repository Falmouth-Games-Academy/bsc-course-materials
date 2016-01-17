

x0 = 0.5
y0 = 0.5

zx = x0
zy = y0

print r"x_0 &= %r \\" % x0
print r"y_0 &= %r \\" % y0

for i in xrange(200):
	mag = zx*zx + zy*zy
	print r"(x_{%i})^2 + (y_{%i})^2 &= %r %s 4 \\" % (i, i, mag, r"<" if mag<4 else r"\geq")
	if mag >= 4:
		break

	nx = zx*zx - zy*zy + x0
	ny = 2*zx*zy + y0
	
	print r"x_{%i} &= (x_{%i})^2 - (y_{%i})^2 + x_0 \\" % (i+1, i, i)
	print r"&= (%r)^2 - (%r)^2 + %r" % (zx, zy, x0)
	print r"= %r \\" % nx
	
	print r"y_{%i} &= 2 \times x_{%i} \times y_{%i} + y_0 \\" % (i+1, i, i)
	print r"&= 2 \times %r \times %r + %r" % (zx, zy, y0)
	print r"= %r \\" % ny
	
	zx = nx
	zy = ny

