import numpy as np
import matplotlib.pyplot as plt
import math

def taylor_sin(x, a, n_terms):
    result = 0
    for n in range(n_terms):
        if n % 4 == 0:
            coeff = np.sin(a) #0
        elif n % 4 == 1:
            coeff = np.cos(a) #1
        elif n % 4 == 2:
            coeff = -np.sin(a) #0
        else:
            coeff = -np.cos(a) #-1
        
        result += coeff * (x - a)**n / math.factorial(n)
    
    return result

a = 0
x_test = 2
n_terms = 15

sin_2_taylor = taylor_sin(x_test, a, n_terms)
sin_2_exact = np.sin(x_test)

x_range = np.arange(-10, 10.1, 0.1)

fig, ax = plt.subplots(figsize=(8, 8))

term_counts = [1, 2, 3, 4, 5, 6]

for i, n in enumerate(term_counts):
    y_taylor = np.array([taylor_sin(x, a, n) for x in x_range])
    ax.plot(x_range, y_taylor)

y_exact = np.sin(x_range)
ax.plot(x_range, y_exact)

y_taylor_15 = np.array([taylor_sin(x, a, n_terms) for x in x_range])
ax.plot(x_range, y_taylor_15)

ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
plt.savefig('taylor.png')

plt.show()
