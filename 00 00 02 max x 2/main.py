import numpy as np


def twice_max(x:np.ndarray) -> np.ndarray:
  return np.arange(x[0], x[-1]*2+1e-3, x[1]-x[0])

x_input = np.arange(0, 10+1e-3, 2.5)

x_output = twice_max(x_input)
print(x_output)
