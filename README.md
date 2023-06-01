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

4. **compute_rmse** Calculate the Root Mean Squared Error (RMSE) between the predicted values and the actual data.

> Arguments:
>
>> `data`: Function for which to calculate the Jacobian.
>>
>> `predicted`: Array of predicted values.
>>
> Returns: float value (RMSE value).


