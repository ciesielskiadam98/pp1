
numer = int(input("Wprowadz 26cyfrowy numer bankowy: "))

numer = str(numer)

print(numer[0:2] + " " + numer[2:6] + " " + numer[6:10] + " " + numer[10:14] + " " + numer[14:18] + " " + numer[18:22] + " " + numer[22:len(numer)])
