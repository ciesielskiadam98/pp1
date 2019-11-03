import re

with open('students.txt', 'r') as file:
    for i in file:
        divided = re.split(",", i)
        if divided[2] != 'age':
            if int(divided[2]) < 30:
                print('{} {} {}'.format(divided[0], divided[1], divided[4]))
        
    

