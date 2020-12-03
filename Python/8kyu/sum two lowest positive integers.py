def sum_two_smallest_numbers(numbers):
    sorted_num = sorted(numbers)
    min_num = sorted_num[:2]
    return sum(min_num)
    #another way to do
    #sum_min = sorted_num[0] + sorted_num[1]
    #return sum_min
