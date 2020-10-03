import numpy as np

from root_finding import sequential


def f(x_i):
  return x_i ** 2 - 10



if "__main__" == __name__:

  sqrt_10_seq = sequential(f, 0.0, 1e-5, 1e-3, 6)

  print(f"{sqrt_10_seq:g} ** 2 =", sqrt_10_seq ** 2)
  

