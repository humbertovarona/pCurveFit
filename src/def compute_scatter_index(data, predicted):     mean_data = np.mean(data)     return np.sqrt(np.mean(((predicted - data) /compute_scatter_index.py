def compute_scatter_index(data, predicted):
    mean_data = np.mean(data)
    return np.sqrt(np.mean(((predicted - data) / mean_data) ** 2))
