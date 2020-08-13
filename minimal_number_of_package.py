def minimal_number_of_packages(items, available_large_packages, available_small_packages):
    # Function that discover the minimal number of packages to pack something
    large_package = 5
    small_package = 1
    contador_large = 0
    contador_small = 0
    total_package = (large_package * available_large_packages) + available_small_packages
    if items <= total_package:
        for i in range(0, available_large_packages):
            items -= large_package
            contador_large += 1
        for i in range(0, items):
            items -= small_package
            contador_small += 1

        total = contador_small + contador_large
        return f'{total}({contador_large} large packages + {contador_small} small package)'
    else:
        return -1


print(minimal_number_of_packages(16, 2, 10))

print(minimal_number_of_packages(24, 1, 10))

print(minimal_number_of_packages(30, 6, 18))

print(minimal_number_of_packages(16, 3, 10))

print(minimal_number_of_packages(18, 2, 10))