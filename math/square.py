def square(number):
    """ :return: the square of the input number """
    if not isinstance(number, (int, float)):
        raise TypeError("Input must be a number")
    return number * number
