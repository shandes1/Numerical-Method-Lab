# to find lagrange interpolation polynomial for the given data

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# Input section
n = int(input("Enter the number of data points: "))
x = np.array(list(map(float, input('Enter all x_data :').split())))
y = np.array(list(map(float, input('Enter all y_data :').split())))

xp = float(input("Enter the point to interpolate: "))

# Symbolic variable for polynomial
X = sp.symbols('X')
s = 0

# Construct Lagrange polynomial
for i in range(n):
    lf = 1
    for j in range(n):
        if j != i:
            lf *= (X - x[j]) / (x[i] - x[j])
    s += y[i] * lf

# Simplify the expression
poly = sp.simplify(s)
print("\nLagrange interpolation polynomial is:\n", poly)

# Interpolated value at a given point
int_val = poly.subs(X, xp)
print(f"\nThe interpolated value at x = {xp} is {int_val}")

# Plotting
f = sp.lambdify(X, poly, 'numpy') 
x_val = np.linspace(min(x) - 1, max(x) + 1, 1000)
y_val = f(x_val)

plt.plot(x_val, y_val, label='Lagrange Polynomial', color='blue')
plt.scatter(x, y, color='red', label='Data Points')
plt.axvline(x=xp, color='green', linestyle='--', label=f'Interpolated x = {xp}')
plt.scatter(xp,float(int_val), color='black', label=f'Interpolated y = {float(int_val):.4f}')

plt.title('Lagrange Interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
