import numpy as np
import typing


Scalar = typing.Union[float, int]
Array = typing.Union[typing.List[Scalar], typing.Tuple[Scalar], np.ndarray]


def get_array_start_end_delta(x:Array):
  start_x = min(x)
  end_x = max(x)
  delta_x = x[1] - x[0]

  return {'start':start_x, 'end':end_x, 'delta':delta_x}


def main():
  print(get_array_start_end_delta([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

  print(get_array_start_end_delta([ 0. ,  2.5,  5. ,  7.5, 10. ]))

  print(get_array_start_end_delta([0. , 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1. , 1.1, 1.2]))


if "__main__" == __name__:
  main()
