def format_equation_with_coefficients(best_func, best_params):
    equation = best_func.__name__
    equation_with_coefficients = equation + ": "
    for i, param in enumerate(best_params):
        equation_with_coefficients += f"{param} * x^{i} + "
    equation_with_coefficients = equation_with_coefficients.rstrip(" + ")
    return equation_with_coefficients
