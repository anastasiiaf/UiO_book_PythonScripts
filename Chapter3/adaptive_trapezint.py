

# Exercise 3.8 Make adaptive trapezoidal rule
import math as math 
def trapezint(f, a, b, n):
    h = (b - a)/float(n)
    s = sum([1/2*h*(f(a + i*h)+f(a + (i+1)*h)) for i in range(0, n)])  
#    s = 0
#    for i in range(0, n):
#       x_i = a + i*h
#       x_i2 = a + (i+1)*h 
#       s+= 1/2*h*(f(x_i)+f(x_i2)) 
    return(s) 

def adaptive_trapezint(f, a, b, eps=1E-10):
    step = (b-a)/10
    d = 0.000001
    max_der2 = max([abs((f(a + i*step + d) - 2*f(a + i*step) +  f(a + i*step - d))/(d**2)) for i in range(1, 11)])
#    der2_approx = []   
#    for i in range(1, 11):
#       interim = (f(a + i*d) - 2*f(a) +  f(a - i*d))/((i*d)**2)
#       print(interim)
#       der2_approx.append(abs(interim))
#    max_der2 = max(der2_approx)
#    print(max_der2)
    h = math.sqrt(12*eps)*((b-a)*max_der2)**(-1/2)
    n = (b - a)/float(h)
    return(n)

def test_trapezint(a, b, n):
#    def g(x): # test function
#        return(math.cos(x)) 
#    
#    def G(x): # integral from g(x)
#        return(math.sin(x)) 
 
    g = lambda x: math.cos(x)
    G = lambda x: (math.sin(x))
    exact = G(b) - G(a)
    approx = trapezint(g, a, b, n)
    print("Exact, Approx", exact, approx)
    print("Exact error", abs(exact - approx))
    success = abs(exact - approx) < 1E-2
    msg = "Error!"
    assert success, msg
          
        
n = 160751
a = 0
b = math.pi
f = lambda x: math.cos(x)
result = trapezint(f, a, b, n)
test_trapezint(a, b, n)
adaptive_trapezint(f, a, b, eps=1E-10)

"""
Results:
    cos(x): a = 0, b = pi
    Exact, Approx 1.2246467991473532e-16 3.885780586188048e-16
    Exact error 2.6611337870406944e-16
    n = 160750.92834452755
    
    after correct n
    Exact, Approx 1.2246467991473532e-16 3.463145026826042e-16
    Exact error 2.2384982276786887e-16
    
    sin(x): a = 0, b = pi
    Exact, Approx 2.0 1.9835235375094546
    Exact error 0.01647646249054535
    n = 160750.92834452755
    
    after correct n:
    Exact, Approx 2.0 1.999999999936343
    Exact error 6.365707960753753e-11   
    
    sin(x): a = 0, b = pi/2
    Exact, Approx 0.9999999999999999 0.9979429863543573
    Exact error 0.0020570136456425914
    n = 56834.03575722411
    
    after correct n
    Exact, Approx 0.9999999999999999 0.9999999999363569
    Exact error 6.364297977512479e-11
    
"""    