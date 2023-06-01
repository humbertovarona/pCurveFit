def read_data(filename):
    data = np.loadtxt(filename, delimiter=',', skiprows=1)
    time = data[:, 0]
    variables = data[:, 1:]
    return time, variables
