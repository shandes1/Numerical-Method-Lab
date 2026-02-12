#to fit second degree curve y = a + bx + cx^2 to the given data
import numpy as np
import scipy.linalg as slg

print('To find the curve y = a + bx + cx^2')
n = int(input("Enter the number of data points: "))
x = np.array(list(map(float, input('Enter all x_data :').split())))
y = np.array(list(map(float, input('Enter all y_data :').split())))
A = []
B = []
A = [[n, np.sum(x), np.sum(x**2)] , [np.sum(x), np.sum(x**2),np.sum(x**3)], [np.sum(x**2), np.sum(x**3),np.sum(x**4)]]
B = [np.sum(y),np.sum(x*y),np.sum(x**2*y)]
print('The coefficient matrix of normal eqn A: \n', np.matrix(A))
print('The output matrix of normal eqn B: \n', np.matrix(B))
coeff = slg.solve(A,B)
print(f'Curve of best fit : {coeff[0]} + {coeff[1]}*x + {coeff[2]}*x^2')
X = np.linspace(-10, 10 , 1000)
import matplotlib.pyplot as plt

plt.plot(X, coeff[0] + coeff[1]*X + coeff[2]*X**2)
plt.scatter(x, y, color='red', label='Data Points')

# Decorations
plt.title('Second Degree Curve Fitting')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()
