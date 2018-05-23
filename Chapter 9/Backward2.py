import math as math

class Diff:
    def __init__(self, f, h):
        self.f = f
        self.h = float(h)
        
class Backward1(Diff):
    def __call__(self, x):
        f, h = self.f, self.h
        return((f(x)-f(x-h))/h)   

class Backward2(Diff):
    def __call__(self, x):
        f, h = self.f, self.h
        return((f(x-2*h) - 4*f(x-h) + 3*f(x))/(2*h))     
    
print("Program flow: \n")
s = '    backward1    backward2   backward1-backward2\n'
for i in range(0, 15):
    d1 = Backward1(math.exp, 2**(-i)) 
    d2 = Backward2(math.exp, 2**(-i)) 
    s += '%12.6f %12.6f %12.6f\n' % (d1(0), d2(0), d1(0)-d2(0))
print(s)


"""
Program output:
    backward1    backward2   backward1-backward2
    0.632121     0.831909    -0.199788
    0.786939     0.941757    -0.154818
    0.884797     0.982655    -0.097858
    0.940025     0.995253    -0.055228
    0.969391     0.998757    -0.029366
    0.984536     0.999682    -0.015146
    0.992228     0.999920    -0.007692
    0.996104     0.999980    -0.003876
    0.998049     0.999995    -0.001946
    0.999024     0.999999    -0.000975
    0.999512     1.000000    -0.000488
    0.999756     1.000000    -0.000244
    0.999878     1.000000    -0.000122
    0.999939     1.000000    -0.000061
    0.999969     1.000000    -0.000031   

"""   