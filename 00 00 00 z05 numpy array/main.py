import numpy as np
def make_an_array_using_arange(x_i, x_e, delta_x):
    array = []

    if delta_x > 0:
        value = x_i
        while value < x_e:
            array.append(value)
            value += delta_x
    elif delta_x < 0:
        value = x_e
        while value > x_i:
            array.append(value)
            value -= delta_x
    result_array = np.array(array)
    return np.arange(x_i, x_e, delta_x)

def main():
    print(make_an_array_using_arange(1, 10, 1))

    print(make_an_array_using_arange(0, 11, 2.5))

    print(make_an_array_using_arange(0, 1.21, 0.1))


if "__main__" == __name__:
    main()