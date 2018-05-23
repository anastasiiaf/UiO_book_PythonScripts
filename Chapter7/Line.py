class Line:
    def __init__(self, A, B):
        self.A = A
        self.B = B
        
        
    def value(self, x):
        a = (self.B[1]-self.A[1])/float(self.B[0]-self.A[0])
        b = self.A[1] - a*self.A[0]
        return(a*x+b)  
    
    
    def test(self):
        exact = 1.5
        result = self.value(1)
        success = (result - exact) < 1E-14
        assert success, 'Error!'

A = (0,-1); B = (2,4)        
l = Line(A, B) 
x = 1     
l.test()
print("Value of line at x = %2.3f is %2.3f" %(x, l.value(x)))  

"""
Program output:
  Value of line at x = 1.000 is 1.500
"""



