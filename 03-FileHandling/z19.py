import re
uni = []
with open('universities.txt', 'r') as file:
    name = re.findall('.*\n', file.read())
    for i in name:
        uni.append(i)
    uni.sort()
    file.close()
        
with open('universities.txt', 'w') as file:
    zapis = uni[0]
    for i in range(1,len(uni)):
        zapis += uni[i]
    file.write(zapis)
    