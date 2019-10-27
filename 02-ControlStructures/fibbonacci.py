lista = [0, 1]
print(lista[0], lista[1], end=" ")
for i in range(48):
    lista.append(lista[i] + lista[i+1])
    print(lista[i+2], end=" ")
    
    