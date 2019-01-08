from mpmath import *
import numpy as np
import matplotlib.pyplot as plt

r = np.linspace(-10, 10, 100)
i = np.linspace(-10, 10, 100)
p = [mp.mpc(b, a) for a in i for b in r]

q = [zeta(wee) for wee in p]

input_real = [re(i) for i in p]
input_imag = [im(i) for i in p]
output_real = [re(i) for i in q]
output_imag = [im(i) for i in q]

plt.plot(input_real, input_imag)
plt.show()
plt.plot(output_real, output_imag)
plt.show()
