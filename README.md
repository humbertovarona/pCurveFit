# pCurveFit

Find the best function that fits a time series

# Version

![](https://img.shields.io/badge/Version%3A-1.0-success)

# Release date

![](https://img.shields.io/badge/Release%20date-May%2C%2030%2C%202023-9cf)

# License

![](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)

# Programming language

<img src="https://img.icons8.com/?size=512&id=13441&format=png" width="50"/>

# OS

<img src="https://img.icons8.com/?size=512&id=17842&format=png" width="50"/> <img src="https://img.icons8.com/?size=512&id=122959&format=png" width="50"/> <img src="https://img.icons8.com/?size=512&id=108792&format=png" width="50"/>

# Installation

```shell
pip install numpy
pip install matplotlib
pip install scipy
```

## Requirements

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
```

# Functions list

1. **fit_time_series** Fit a time series to the best-fitting mathematical equation

> Arguments:
>
>> `time`: Array of time values.
>>
>> `data`: Array of corresponding data values.
>>
> Returns: The best-fitting function `best_func`, optimal parameters `best_params`, and covariance matrix `cov_matrix`.

2. **jacobian** Compute the Jacobian matrix of a given function

> Arguments:
>
>> `func`: Function for which to calculate the Jacobian.
>>
>> `x`: Array of input values.
>>
>> `params`: Additional parameters required by the function.
>>
> Returns: array: Jacobian matrix `jac`.

3. **compute_bias** Compute the bias between the predicted values and the actual data.

> Arguments:
>
>> `data`: Function for which to calculate the Jacobian.
>>
>> `predicted`: Array of predicted values.
>>
> Returns: float value (Bias value).

4. **compute_rmse** Compute the Root Mean Squared Error (RMSE) between the predicted values and the actual data.

> Arguments:
>
>> `data`: Function for which to calculate the Jacobian.
>>
>> `predicted`: Array of predicted values.
>>
> Returns: float value (RMSE value).

5. **compute_scatter_index** Compute the scatter index between the predicted values and the actual data.

> Arguments:
>
>> `data`: Function for which to calculate the Jacobian.
>>
>> `predicted`: Array of predicted values.
>>
> Returns: float value (Scatter index value).

6. **compute_r_squared** Compute the coefficient of determination (R-squared) between the predicted values and the actual data.

> Arguments:
>
>> `data`: Function for which to calculate the Jacobian.
>>
>> `predicted`: Array of predicted values.
>>
> Returns: float value (R-squared value).

7. **plot_data_and_fit** Plot the original data along with the best-fitting function.

> Arguments:
>
>> `time`: Array of time values.
>>
>> `data`: Array of corresponding data values.
>>
>> `func`: The best-fitting function.
>>
>> `params`: The optimal parameters.
>>
> Returns: none.

8. **read_data** Read the data from a file with columns separated by commas.

> Arguments:
>
>> `filename`: Path to the data file (including filename).
>>
> Returns: Time values `time` and data values as numpy arrays `variables`.

9. **format_equation_with_coefficients** Formats the best-fit equation with substituted coefficients as a string.

> Arguments:
>
>> `best_func`: The best-fitting function.
>>
>> `best_params`: The optimal parameters.
>>
> Returns: `equation_with_coefficients`: The formatted equation with substituted coefficients (string).

# Usage examples

## Sample 1

```python
time = np.array([1, 1.5, 2, 3, 4, 5])
data = np.array([1.5, 3, 8, 20, 48, 120])
best_func, best_params, cov_matrix = fit_time_series(time, data)

predicted_data = best_func(time, *best_params)

bias = calculate_bias(data, predicted_data)
rmse = calculate_rmse(data, predicted_data)
scatter_index = calculate_scatter_index(data, predicted_data)
r_squared = calculate_r_squared(data, predicted_data)

print("Bias:", bias)
print("RMSE:", rmse)
print("Scatter Index:", scatter_index)
print("R-squared:", r_squared)

plot_data_and_fit(time, data, best_func, best_params)
```

<p align="center">
<img src="/images/sample1.png" width="500">
</p>


## Sample 2

```python

```

<p align="center">
<img src="/images/sample2.png" width="500">
</p>
