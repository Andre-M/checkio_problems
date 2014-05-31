# Andre Meireles
# Problem submission for check.io
# Median
# http://www.checkio.org/mission/median/solve/

#data guaranteed to be non-empty list of integers
def checkio(data):

    # if we sort our input data then we may deduce the following:

    # if there is an even number of items in the input, the median is the average
    # of the two middle inputs

    # if there is an odd number of items in the input, the median is simply what
    # is in the middle index

    data.sort()

    # even length list
    if(len(data)%2 == 0):
        # list indices may only be integers
        middle_right_index = int(len(data)/2)
        middle_left_index = middle_right_index - 1
        median = (data[middle_right_index] + data[middle_left_index])/2
    # odd length list
    else:
        middle_index = int(len(data)/2)
        median = data[middle_index]

    return median

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
    print("Start the long test")
    assert checkio(list(range(1000000))) == 499999.5, "Long."
    print("The local tests are done.")