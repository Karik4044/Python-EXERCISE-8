import numpy as np
import matplotlib.pyplot as plt

# Define the coefficients of the polynomial
# For example, let's define f(x) = 2x^3 - x^2 + 1
coefficients = [2, -1, 0, 1]  # This corresponds to 2x^3 - 1x^2 + 0x + 1

# Define the range of x values
X = np.array([-4, -3, -2, -1, 0, 1, 2, 3, 4])

# Evaluate the polynomial at each value of X
Y = np.polyval(coefficients, X)

# Plot the polynomial
plt.figure(figsize=(10, 6))
plt.plot(X, Y, label='f(x) = 2x^3 - x^2 + 1', marker='o')
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.title('Plot of the Polynomial')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.legend()
plt.show()

