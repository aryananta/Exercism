def square_of_sum(number):
    #pass
    the_square_of_sum = 0
    for i in range(number+1):
        the_square_of_sum += i
    return the_square_of_sum ** 2


def sum_of_squares(number):
    #pass
    the_sum_of_squares = 0
    for i in range(number+1):
        the_sum_of_squares += i**2
    return the_sum_of_squares


def difference_of_squares(number):
    # pass
    diff = square_of_sum(number) - sum_of_squares(number)
    return diff
