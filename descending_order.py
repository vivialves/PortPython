def descending_order(num):
    # return its digits in descending order
    num_str = str(num)
    num_list = [int(number) for number in num_str]
    num_ord = sorted(num_list)
    num_reverse = num_ord[::-1]
    num_list_str = [str(number) for number in num_reverse]
    new_str = ''.join(num_list_str)
    new_num = int(new_str)
    return new_num

print(descending_order(213))