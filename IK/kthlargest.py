def kth_largest_in_an_array(numbers, k):
    numbers.sort()
    lenn = len(numbers)
    nth = numbers[lenn-k]
    return nth
