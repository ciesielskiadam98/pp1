with open('numbers.txt', 'r') as file:
    suma = 0
    for line in file:
        suma += int(line)
    print(suma)