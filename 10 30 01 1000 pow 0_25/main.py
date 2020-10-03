import numpy as np

from root_finding import newton_raphson


def q(x:float) -> float:
  return x ** 4 - 1000


def dq_dx(x:float) -> float:
  return 4 * (x**3)


if isinstance(q(1.0), float) and isinstance(dq_dx(1.0), float):
  x = newton_raphson(q, dq_dx, 1.0, 1e-3)
  print(f"({x:g}) ** 4 =", (x ** 4))