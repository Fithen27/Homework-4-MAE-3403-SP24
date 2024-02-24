from scipy.optimize import fsolve
import numpy as np
import matplotlib.pyplot as plt

# Define the equations
def equation1(x):
    return x - 3 * np.cos(x)

def equation2(x):
    return np.cos(2 * x) * x**3

# Use fsolve to find the roots
root1 = fsolve(equation1, 0)  # Initial guess for root 1
root2 = fsolve(equation2, [-2, 0, 2])  # Initial guesses for root 2

print("Roots of x - 3*cos(x) = 0:", root1)
print("Roots of cos(2*x)*x^3 = 0:", root2)

# Plot the functions to visualize intersection
x_values = np.linspace(-2*np.pi, 2*np.pi, 1000)
y1 = x_values - 3*np.cos(x_values)
y2 = np.cos(2*x_values) * x_values**3

plt.plot(x_values, y1, label='x - 3*cos(x)')
plt.plot(x_values, y2, label='cos(2*x)*x^3')
plt.scatter(root1, [0]*len(root1), color='red', label='Roots of x - 3*cos(x) = 0')
plt.scatter(root2, [0]*len(root2), color='blue', label='Roots of cos(2*x)*x^3 = 0')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Intersection of Functions')
plt.legend()
plt.grid(True)
plt.show()
