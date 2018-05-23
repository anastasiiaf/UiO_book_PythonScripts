# Exercise 3.3
from numpy.lib.scimath import sqrt

def roots(a,b,c):
    r1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
    r2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)    
    return(r1, r2)   

def test_roots_float():
    a = 1; b = 4; c = 1
    r1, r2 = roots(a,b,c)
    success1 = (a*r1**2 + b*r1 + c and a*r2**2 + b*r2 + c)  < 1E-10 
    success2 = (isinstance(r1, (float)) and isinstance(r2, (float))) == True
    print("R1 type " + str(type(r1)) + " and R2 type " + str(type(r2)))
    msg = "Error! Root(s) are not float type"
    assert (success1 and success2), msg

    
def test_roots_complex():
    a = 1; b = 4; c = 1
    r1, r2 = roots(a,b,c)
    success1 = (a*r1**2 + b*r1 + c and a*r2**2 + b*r2 + c) < 1E-10 
    success2 = (isinstance(r1, (complex)) and isinstance(r2, (complex))) == True
    print("R1 type " + str(type(r1)) + " and R2 type " + str(type(r2)))
    msg = "Error! Root(s) are not complex type"
    assert (success1 and success2), msg

    
a = 1; b = 2; c = 100
r1, r2 = roots(a,b,c)
print(r1, r2)
test_roots_float()
test_roots_complex()


