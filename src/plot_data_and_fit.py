def plot_data_and_fit(time, data, func, params):
    plt.figure()
    plt.plot(time, data, 'bo-', label='Original Data')
    plt.plot(time, func(time, *params), 'r-', label='Best Fit')
    plt.xlabel('Time')
    plt.ylabel('Data')
    plt.legend()
    plt.show()
