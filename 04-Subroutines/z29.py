tab = [2, 3, 5, 2, 9, 8, 1, 3, 9, 1, 1, 4, 7, 7, 1, 4]
def mediana(tab):
    tab.sort()
    if len(tab) % 2 == 0:
        return (tab[len(tab) % 2 - 1] + tab[len(tab) % 2])/2
    else:
        return tab[len(tab) % 2]

def dominanta(tab):
    suma = 0
    sumaCal = 0
    for i in range(len(tab)):
        for j in tab:
            for x in range(len(tab)):
                if tab[x] == j:
                    suma += 1
            if suma > sumaCal:
                sumaCal = suma
                dom = j
            suma = 0
    return dom

print(dominanta(tab))
            
            
    