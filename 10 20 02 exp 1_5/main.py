import numpy as np
import math

from root_finding import bisection

def h(x:float) -> float:
  return math.exp(1)**x - 1.5
  
  
if isinstance(h(0.0), float):
  x = bisection(h, 0.0, 1, 1e-3)
  print(f"exp({x:g}) =", np.exp(x))