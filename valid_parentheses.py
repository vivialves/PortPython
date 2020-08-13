from collections import Counter


def valid_parentheses(string):
   # Write a function called that takes a string of parethesis, and determine if the order
   # of the parenthese is valid
    string_list = [carac for carac in string]
    count = Counter(string_list)
    contador = 0
    if count.get('(') == count.get(')'):
        for carac in string_list:
            if carac == '(':
                contador += 1
            elif carac == ')':
                contador -= 1
                if contador < 0:
                    return False
        if contador == 0:
            return True
    else:
        return False
