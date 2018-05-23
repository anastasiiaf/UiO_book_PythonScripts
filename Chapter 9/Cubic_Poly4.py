

class Parabola:
    def __init__(self, c0, c1, c2):
        self.c0 = c0
        self.c1 = c1
        self.c2 = c2
  
    def __call__(self, x):
        return(self.c2*x**2 + self.c1*x + self.c0)
    
    def table(self, L, R, n):
        """ Return a table with n points for L <= x <= R. """
        s = '           x            y\n'
        import numpy as np
        for x in np.linspace(L, R, n):
            y = self(x)
            s += '%12g %12g\n' % (x, y)
        return(s)

class Cubic(Parabola):
    def __init__(self, c0, c1, c2, c3):
        Parabola.__init__(self, c0, c1, c2) 
        self.c3 = c3
        
    def __call__(self, x):
        return(Parabola.__call__(self, x) + self.c3*x**3)

class Poly4(Cubic):
    def __init__(self, c0, c1, c2, c3, c4):
        Cubic.__init__(self, c0, c1, c2, c3) 
        self.c4 = c4
        
    def __call__(self, x):
        return(Cubic.__call__(self, x) + self.c4*x**4)    

    
p = Poly4(1, 2, 2, 3, 4)
print("Program output: \n")   
print("Given x =%3g, function value is %3g:" % (5, p(5)))
print("Program flow: \n")
print(p.table(0, 10, 5))


"""
Program output:

Given x =  5, function value is 2936:
Program flow: 

           x            y
           0            1
         2.5      221.625
           5         2936
         7.5      14050.4
          10        43221
"""

