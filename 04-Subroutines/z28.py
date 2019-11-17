lang = ['Java', 'Python', 'JavaScript', 'C++', "C#", 'Ruby', 'Perl', 'PHP', 'C', 'Android']
x = [61, 47, 37, 32, 26, 18, 14, 14, 9, 7]
def rysujWykres(lang, x):
    z = 0
    result = ''
    for j in lang:
        hash = ''
        for i in range(int(x[z]/2)):
            hash += "#"
        result += "{:>10s}: {}\n".format(j, hash)
        z += 1
    return result
print(rysujWykres(lang, x))
        