# Finding out which one of the given numbers differs from the others.

def iq_test(numbers):
    numbers_list = numbers.split(" ")
    numbers_list_i = [int(numbers) for numbers in numbers_list]
    counter_p = 0
    counter_i = 0
    for n in range(0, len(numbers_list_i)):
        if numbers_list_i[n] % 2 == 0:
            counter_p += 1
            position_p = n + 1
        else:
            counter_i += 1
            position_i = n + 1
    if counter_i > counter_p:
        print(f'The {ordinal[position_p]} number is odd, while the rest of the numbers are even')
    else:
        print(f'The {ordinal[position_i]} number is even, while the rest of the numbers are odd')


iq_test("2 4 7 8 10")
