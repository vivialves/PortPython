def solution(s):
    # Function so that it splits the string into pairs
    s = s.ljust(len(s) + 1)
    s = s.replace(' ', '_')
    caracter_list = []
    for caracter in s:
        caracter_list.append(s[0:2])
        s = s.replace(s, s[2:len(s)])
    s_list = [caracter for caracter in caracter_list if len(caracter) == 2]

    return s_list

print(solution('abcdefghi'))