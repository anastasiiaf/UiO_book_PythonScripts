# Exercise 2.2 Approximate Fahrenheit-Celsius conversion table
Fdegrees = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Cdegrees = []
for F in Fdegrees:
    Cdegrees.append((F - 32)/(9.0/5))
    
#table = [[Fdegrees, Cdegrees] for F, C in zip(Fdegrees, Cdegrees)]  

for i in range(0, 11):
    C_apprx = (Fdegrees[i] - 30)/2
    print('%5.0f %5.1f %5.1f'% (Fdegrees[i], Cdegrees[i], C_apprx))
    