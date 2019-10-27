nrDniaTygodnia = ['PN', 'WT', 'SR', 'CZ', 'PT', 'SB', 'ND']
x = 1
for i in range(6):
    if i == 0:
        print("| {} | {} | {} | {} | {} | {} | {} |".format(nrDniaTygodnia[0], nrDniaTygodnia[1], nrDniaTygodnia[2], nrDniaTygodnia[3], nrDniaTygodnia[4], nrDniaTygodnia[5], nrDniaTygodnia[6]))
    elif i == 1:
        print("|    |    |", end="")
        for k in range(5):
            print("  {} |".format(x), end="")
            x += 1
        print("")    
    elif i==2:
        x=10
        print("|  {} |  {} |  {} |  {} |".format(6,7,8,9), end="")
        for g in range(3):
            print(" {} |".format(x), end="")
            x += 1
        print("")
    else:
        if i == 3:
            x = 13
        elif i == 4:
            x = 20
        print("|", end="")
        if(i != 5):
            for z in range(7):
                print(" {} |".format(x), end="")
                x += 1
            print("")
        else:
            x=27
            
            for c in range(4):
                print(" {} |".format(x), end="")
                x += 1
        

        