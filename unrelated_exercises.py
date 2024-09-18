if __name__ == '__main__':
    n1 = int(input('nombre 1: '))
    n2 = int(input('nombre 2: '))
    n3 = int(input('nombre 3: '))

    lowest = n1 if n1 < n2 else n2
    lowest = lowest if lowest < n3 else n3

    print(f'le plus bas: {lowest}')

