for j in range(7):
    x = j+1
    if j == 0 or j == 1:
        for i in range(7):
            if i == 0:
                print("{}  ".format(x), end="")
                x += 7
            else:
                print("{} ".format(x), end="")
                x += 7
        print("")
    else:
        for i in range(7): 
            print("{} ".format(x),end="")
            x += 7
        print("")