import math as math
class Quadratic:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def value(self, x):
        return(self.a*x**2 + self.b*x + self.c)  
    
    def table(self, L, R, n):
        s = '           x            y\n'
        import numpy as np
        for x in np.linspace(L, R, n):
            y = self.value(x)
            s += '%12g %12g\n' % (x, y)
        return(s)
    
    def roots(self):
        D = self.b**2 -4*self.a*self.c
        x1 = (-self.b + math.sqrt(D))/(2*self.a)
        x2 = (-self.b - math.sqrt(D))/(2*self.a)
        return(x1, x2)
    
    def test(self):
        x1, x2 = self.roots()
        result1 = self.a*x1**2 + self.b*x1 + self.c
        result2 = self.a*x2**2 + self.b*x2 + self.c
        success = (result1 + result2) < 1E-3
        assert success, 'Error!'

a = 7; b = 8; c = -11        
eq =  Quadratic(a, b, c) 
print(eq.table(0,5,10))      
x1, x2 = eq.roots()  
eq.test()
print("Roots of the equation with a=%2.2f, b=%2.2f and c=%2.2f are %2.2f and %2.2f" %(a, b, c, x1, x2))  

"""
Program output:
    
   x            y
           0          -11
    0.555556     -4.39506
     1.11111      6.53086
     1.66667      21.7778
     2.22222      41.3457
     2.77778      65.2346
     3.33333      93.4444
     3.88889      125.975
     4.44444      162.827
           5          204  
    
  Roots of the equation with a=7.00, b=8.00 and c=-11.00 are 0.81 and -1.95  
    
"""



