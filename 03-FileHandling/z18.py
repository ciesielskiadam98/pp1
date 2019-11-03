import re
tab = []
with open('numbers.txt', 'r') as file:
    liczby = re.findall('[0-9][0-9][0-9]', file.read())
    for i in liczby:
        tab.append(int(i))
    tab.sort()
    for j in tab:
        print(j, end=' ')
    