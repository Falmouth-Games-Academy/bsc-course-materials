__author__ = 'Ed'

import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

import matplotlib
matplotlib.rcParams.update({'font.size': 22})

x = np.linspace(1, 100)
y_const = x*0 + 5
plt.ylim(0, 10)
plt.plot(x, y_const)
plt.xlabel('Students')
plt.ylabel('Time (hours)')
plt.savefig('plot_constant.pdf', bbox_inches='tight')

plt.clf()
y_linear = x
plt.plot(x, y_linear)
plt.xlabel('Students')
plt.ylabel('Time (hours)')
plt.savefig('plot_linear.pdf', bbox_inches='tight')

plt.clf()
y_quad = 0.5 * x * (x-1) * (10.0 / 60.0)
plt.plot(x, y_quad)
plt.xlabel('Students')
plt.ylabel('Time (hours)')
plt.savefig('plot_quadratic.pdf', bbox_inches='tight')

plt.clf()
plt.ylim(0, 200)
plt.plot(x, y_const)
plt.plot(x, y_linear)
plt.plot(x, y_quad)
plt.xlabel('Students')
plt.ylabel('Time (hours)')
plt.savefig('plot_all.pdf', bbox_inches='tight')

plt.clf()
plt.tick_params(axis='y', which='both', left='off', right='off', labelleft='off')
plt.tick_params(axis='x', which='both', bottom='off', top='off', labelbottom='off')
plt.plot(x, y_linear)
plt.xlabel('Elements')
plt.ylabel('Time')
plt.savefig('plot2_linear.pdf', bbox_inches='tight')

plt.clf()
plt.tick_params(axis='y', which='both', left='off', right='off', labelleft='off')
plt.tick_params(axis='x', which='both', bottom='off', top='off', labelbottom='off')
plt.plot(x, y_const)
plt.xlabel('Elements')
plt.ylabel('Time')
plt.savefig('plot2_constant.pdf', bbox_inches='tight')

plt.clf()
y_log = np.log(x)
plt.tick_params(axis='y', which='both', left='off', right='off', labelleft='off')
plt.tick_params(axis='x', which='both', bottom='off', top='off', labelbottom='off')
plt.plot(x, y_log)
plt.xlabel('Elements')
plt.ylabel('Time')
plt.savefig('plot2_log.pdf', bbox_inches='tight')

plt.clf()
y_log = np.log(x)
plt.tick_params(axis='y', which='both', left='off', right='off', labelleft='off')
plt.tick_params(axis='x', which='both', bottom='off', top='off', labelbottom='off')
plt.plot(x, y_linear)
plt.plot(x, y_log * 5)
plt.xlabel('Elements')
plt.ylabel('Time')
plt.savefig('plot2_linear_log.pdf', bbox_inches='tight')

plt.clf()
y_nlogn = x * np.log(x)
plt.tick_params(axis='y', which='both', left='off', right='off', labelleft='off')
plt.tick_params(axis='x', which='both', bottom='off', top='off', labelbottom='off')
plt.plot(x, y_nlogn)
plt.xlabel('Elements')
plt.ylabel('Time')
plt.savefig('plot2_nlogn.pdf', bbox_inches='tight')


"""plt.subplot(2,4,1)
plt.ylim(0, 1.2)
plt.plot(x, x*0+1)
plt.title("Constant")

plt.subplot(2,4,2)
plt.plot(x, np.log(x))
plt.title("Logarithmic")

plt.subplot(2,4,3)
plt.plot(x, x**0.5)
plt.title("Fractional power")

plt.subplot(2,4,4)
plt.plot(x, x)
plt.title("Linear")

plt.subplot(2,4,5)
plt.plot(x, x**2)
plt.title("Quadratic")

plt.subplot(2,4,6)
plt.plot(x, x**4)
plt.title("Polynomial")

plt.subplot(2,4,7)
plt.plot(x, 2**x)
plt.title("Exponential")

plt.subplot(2,4,8)
n = range(100+1)
plt.plot(n, [np.math.factorial(i) for i in n])
plt.title("Factorial")

plt.show()
"""
