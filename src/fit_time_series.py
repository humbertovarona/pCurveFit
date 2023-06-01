def linear_func(x, a, b):
    return a * x + b

def exponential_func(x, a, b, c):
    return a * np.exp(b * x) + c

def quadratic_func(x, a, b, c):
    return a * x**2 + b * x + c

def cubic_func(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d
    
def logistic_func(x, a, b, c):
    return c / (1 + a * np.exp(-b * x))
    
def logistic_func(x, a, b, c):
    return c / (1 + a * np.exp(-b * x))

def sqrt_func(x, a, b):
    return a * np.sqrt(x) + b

def polynomial_func(x, *coefficients):
    return np.polyval(coefficients, x)

def fit_time_series(time, data):
    time = np.array(time)
    data = np.array(data)
    functions = [
        linear_func,
        exponential_func,
        quadratic_func,
        cubic_func,
        logarithmic_func,
        sqrt_func,
        polynomial_func
    ]
    best_residuals = float('inf')
    best_func = None
    best_params = None
    for func in functions:
        try:
            popt, _ = curve_fit(func, time, data)
            residuals = np.sum((data - func(time, *popt))**2)
            if residuals < best_residuals:
                best_residuals = residuals
                best_func = func
                best_params = popt
        except RuntimeError:
            continue
    jac = jacobian(best_func, time, *best_params)
    cov_matrix = np.linalg.inv(np.dot(jac.T, jac))
    return best_func, best_params, cov_matrix
    
   
