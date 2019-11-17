tab = [2, 5, 4, 1, 8, 7, 4, 0, 9]

def reversez(tab):
    k = 0
    for i in range(len(tab) - 1):
        tab.insert(k, tab[-1])
        tab.pop()
        k += 1
    return tab
    
print(tab)
print(reversez(tab))
    