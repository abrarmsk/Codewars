def high_and_low(numbers):
    ##########
    # this program returns highest and lowest
    #number stored in a string
    ##########
    numbers_str = numbers.split(' ')
    new_numbers = []
    for num in numbers_str:
        int_num = int(num)
        new_numbers.append(int_num)
    #new_numbers.sort()

    return f'{max(new_numbers)} {min(new_numbers)}'
