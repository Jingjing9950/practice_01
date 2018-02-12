def print_abacus(value):
    new_value = str(value)
    for zero_star in range(10 - len(new_value)):
        print('|00000*****   |')

    for i in new_value:
        if i == '0':
            print('|00000*****   |')
        if i == '1':
            print('|00000****   *|')
        if i == '2':
            print('|00000***   **|')
        if i == '3':
            print('|00000**   ***|')
        if i == '4':
            print('|00000*   ****|')
        if i == '5':
            print('|00000   *****|')
        if i == '6':
            print('|0000   0*****|')
        if i == '7':
            print('|000   00*****|')
        if i == '8':
            print('|00   000*****|')
        if i == '9':
            print('|0   0000*****|')

print_abacus(135)