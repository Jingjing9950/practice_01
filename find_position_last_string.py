def find_last(source, target):
    position = -1
    temp = 0
    while True:
        temp = source.find(target, temp)
        if (temp == -1):
            break

        position = temp
        temp = temp + 1
    return position

print (find_last('aacaa', 'aa'))