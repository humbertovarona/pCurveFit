def jacobian(func, x, *params):
    h = np.sqrt(np.finfo(float).eps)
    n = len(params)
    m = len(x)
    jac = np.zeros((m, n))
    for i in range(n):
        params_plus_h = list(params)
        params_minus_h = list(params)
        params_plus_h[i] += h
        params_minus_h[i] -= h
        jac[:, i] = (func(x, *params_plus_h) - func(x, *params_minus_h)) / (2 * h)
    return jac
