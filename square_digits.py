def square_digits(num):
    # Squaring every digit of a number
    num_str = str(num)
    num_list = [int(number) for number in num_str]
    list_squa = [number * number for number in num_list]
    squa_str = [str(number) for number in list_squa]
    new_str = ''.join(squa_str)
    new_num = int(new_str)
    return new_num


print(square_digits(9119))