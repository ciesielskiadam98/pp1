n = 1
for i in range(4):
    if i+1 == 1 or i+1 == 4:
        for y in range(15):
            print("*", end="")
    else:
        print("*", end="")
        for x in range(13):
            print(" ", end="")
        print("*", end="")
    print("")