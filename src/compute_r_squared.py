def compute_r_squared(data, predicted):
    ss_total = np.sum((data - np.mean(data)) ** 2)
    ss_residual = np.sum((data - predicted) ** 2)
    return 1 - (ss_residual / ss_total)
