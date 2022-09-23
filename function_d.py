def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    maximum_value = numbers[0]
    for value in numbers:
        if value>maximum_value:
            maximum_value = value
    
    return maximum_value


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
