n = 10
def fun(x,y):
    if n >= x and n <= y:
        return "Liczba w zakresie"
    else:
        return "Liczba poza zakresem"

print(fun(10,11))