import timeit
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt



# Define the function
def calcfn(n):
    x = 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            x = x + 1
    return x

# Benchmarking 
time_exec = [timeit.timeit(lambda: calcfn(n), number=1) for n in [1, 2, 3, 10, 100, 500, 1000, 5000, 10000, 20000]]

# Input sizes
n_values = [1, 2, 3, 10, 100, 500, 1000, 5000, 10000, 20000]

# Fit a polynomial curve to the data
def poly_curve_fit(x, a, b, c):
    return a * x ** 2 + b * x + c

popt, _ = curve_fit(poly_curve_fit, n_values, time_exec)

# Generate points for the curve
x_axis_c = np.linspace(min(n_values), max(n_values), 100)
y_axis_c = poly_curve_fit(x_axis_c, *popt)

# Define upper and lower bounds for the polynomial curve
def upper_bound(x, a, b, c):
    return poly_curve_fit(x, a, b, c) * 1.1  # 10% increase

def lower_bound(x, a, b, c):
    return poly_curve_fit(x, a, b, c) * 0.9  # 10% decrease

# Fit upper and lower bound curves
popt_upper, _ = curve_fit(upper_bound, n_values, time_exec)
popt_lower, _ = curve_fit(lower_bound, n_values, time_exec)

# Generate points for the upper and lower bound curves
y_upper = upper_bound(x_axis_c, *popt_upper)
y_lower = lower_bound(x_axis_c, *popt_lower)

# Plotting
plt.scatter(n_values, time_exec, label='Execution Times')
plt.plot(x_axis_c, y_axis_c, 'r-', label='Fitted Polynomial(curve)')
plt.plot(x_axis_c, y_upper, 'g--', label='Upper Bound')
plt.plot(x_axis_c, y_lower, 'b--', label='Lower Bound')
plt.xlabel('n')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time vs Input Size with Bounds')
plt.legend()
plt.grid(True)
plt.show()
