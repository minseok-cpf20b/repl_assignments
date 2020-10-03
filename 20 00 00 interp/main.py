import pylab as py


def linear_interpolation(x_i, x_data, y_data):
  print("x_i =", x_i)
  print("x_data =", x_data)
  print("y_data =", y_data)
  return py.interp(x_i, x_data, y_data)


if "__main__" == __name__:
  x_sin_data = py.arange(5+1e-3)
  y_sin_data = py.sin(x_sin_data)
  
  x_desired = py.arange(0, 5+1e-3, 1e-2)
  y_desired = linear_interpolation(x_desired, x_sin_data, y_sin_data)
  
  print(y_desired)