import math as math
class F:
    def __init__(self, a, w):
        self.a = a
        self.w = w
        
    def __str__(self):
        return('exp(-%g*x)*sin(%g*x)' %(self.a,self.w))
        
    def value(self, x):
        return(math.exp(-self.a*x)*math.sin(self.w*x))  
    

a = 1; w = 0.1       
f = F(a, w)
print(f.value(math.pi))
print(f)


"""
Program output:
  exp(-1*x)*sin(0.1*x)  with current values of a and w
"""



