def likes(names):
    # Function that which must take in input array, containing the names of people who like an item.
    list_names = [each_name for each_name in names]
    if len(list_names) == 0:
        return 'no one likes this'
    elif len(list_names) == 1:
        return f'{list_names[0]} likes this'
    elif len(list_names) == 2:
        return f'{list_names[0]} and {list_names[1]} like this'
    elif len(list_names) == 3:
        return f'{list_names[0]}, {list_names[1]} and {list_names[2]} like this'
    else:
        return f'{list_names[0]}, {list_names[1]} and {len(list_names) - 2} others like this'

print(likes(['Peter', 'Alex', 'Max', 'João', 'Vitor']))