import re
with open('numbers.txt', 'r') as file:
    even = re.findall('[1-9][0-9][0|2|4|6|8]', file.read())
    file.close()
    
with open('evennumbers.txt', 'w') as file:
    for i in even:
        file.write(i+'\n')
        