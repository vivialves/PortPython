def persistence(n):
    # Code that multiply its digits
    n_string = str(n)
    count = 0
    while len(n_string) != 1:
        #n_string = str(n)
        numbers = [int(number) for number in n_string]
        mult = 1
        for i in range(0, len(numbers)):
            mult *= numbers[i]
        n_string = str(mult)
        print(n_string)
        count = count + 1
    return count


print(persistence(999))