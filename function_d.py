def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
<<<<<<< HEAD
    maximum_value = numbers[0]
    for value in numbers:
        if value>maximum_value:
            maximum_value = value
    
    return maximum_value
=======
    return max_value([1, 12, 2, 42, 8, 3])
>>>>>>> 1428b67022dda8e62f1370336c77a68041e49f62


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
