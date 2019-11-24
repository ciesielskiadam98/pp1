def back(x):
    return x[::-1]
def space(x):
    y = ''
    for i in x:
        y += i + ' '
    return y
def big(x):
    y = x.lower()
    y = x.title()
    return y