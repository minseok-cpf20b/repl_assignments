import numpy as np


def min_minus_90(x:np.ndarray) -> np.ndarray:
  return np.arange(x[0]-90, x[-1]+1e-3, x[1]-x[0])


x_input = np.arange(0, 360+1e-3, 2.5)
x_output = min_minus_90(x_input)
print(x_output)
