def f():
    k = 1
    for i in range(3):
        for j in range(3):
            print('{}'.format(k), end=' ')
            k += 1
        print()         
f()
            