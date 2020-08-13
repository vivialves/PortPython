def sort_by_price_ascending(json_string):
    # Função que ordena de forma crescente os preços de uma string importada do json
    # letters_upper = [chr(i) for i in range(65, 91)]
    letters_lower = [chr(i) for i in range(97, 123)]
    letters_numbers = [chr(i) for i in range(46, 58)]
    list_js = json_string.split(',')
    list_string = []
    for i in range(0, len(list_js)):
        list_string.append([])
        for caracter in list_js[i]:
            if caracter in letters_lower or caracter in letters_numbers:
                list_string[i].append(caracter)
    list_food = [''.join(lista[4:len(lista)]) for lista in list_string]
    list_price = [''.join(lista[5:len(lista)]) for lista in list_string]
    list_dict = []
    for i in range(0, len(list_food), 2):
        dict_son = {}
        if i % 2 == 0:
            dict_son['name'] = list_food[i]
        if (i + 1) % 2 != 0:
            dict_son['price'] = float(list_price[i + 1])
        list_dict.append(dict_son)
    print(list_dict)
    return sorted(list_dict, key=lambda food_price: food_price['price'])


print(sort_by_price_ascending('[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice,"price":4.04}]'))
