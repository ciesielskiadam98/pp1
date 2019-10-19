
masa = float(input("Podaj mase ciala(kg): "))
wzrost = float(input("Podaj wzrost(m): "))

bmi = masa / wzrost**2

#porownanie bmi z przedzialami

if bmi < 18.5:
    print("Twoje bmi to {}. Masz niedowagę".format(bmi))
    
if bmi >= 18.5 and bmi <= 24.99:
    print("Twoje bmi to {}. Masz prawidłową wagę".format(bmi))
    
if bmi > 24.99:
    print("Twoje bmi to {}. Masz nadwagę".format(bmi))
    