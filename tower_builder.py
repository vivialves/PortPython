def tower_builders(n_floors):
    # Build a tower by the following given argument
    list = []
    line = (n_floors * 2) - 1
    for i in range(1, 2 * n_floors, 2):
        simbol = i * '*'
        quant_simbol = simbol.center(line)
        list.append(quant_simbol)
    return list

print(tower_builders(3))
