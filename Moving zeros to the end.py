def move_zeros(array):
    array = sorted(array, key=lambda x: x is 0 or type(x) is float)
    return (array)