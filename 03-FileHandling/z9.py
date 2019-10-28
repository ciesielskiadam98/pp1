with open('NoEducation.txt', 'r') as file:
    i = 1
    for line in file:
        print("{} ".format(i) + line, end='')
        i += 1