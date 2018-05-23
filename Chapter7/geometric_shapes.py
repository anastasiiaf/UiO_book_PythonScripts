

import numpy as np
import math as math

class Triangle:
    def __init__(self, vertices):
        self.vertices = vertices
        
        
    def area(self):
        h = np.array(self.vertices)
        v = np.ones((3,1))
        matrix = np.c_[h, v]
        area = 1/2*(np.linalg.det(matrix))
        return(area)
    
    def perimeter(self):
        v1 = self.vertices[0]
        v2 = self.vertices[1]
        v3 = self.vertices[2]
        side1 = math.sqrt((v2[0]-v1[0])**2 + (v2[1]-v1[1])**2)
        side2 = math.sqrt((v2[0]-v3[0])**2 + (v2[1]-v3[1])**2)
        side3 = math.sqrt((v1[0]-v3[0])**2 + (v1[1]-v3[1])**2)
        return(side1 + side2 +side3)
    
    def test_area(self):
        v1 = self.vertices[0]
        v2 = self.vertices[1]
        v3 = self.vertices[2]
        area_exact = 0.5*(v2[0]*v3[1] - v3[0]*v2[1]- v1[0]*v3[1]+ v3[0]*v1[1]+v1[0]*v2[1]-v2[0]*v1[1])
        error = np.abs(area_exact - self.area())
        success = error < 1E-3
        assert success, '|area_exact - self.area()| = %g !=0' %error
        
        
    def test_perimeter(self):
        side1 = 2.236
        side2 = 1.414
        side3 = 2.236
        perimeter_exact = side1+side2+side3
        error = np.abs(perimeter_exact - self.perimeter())
        success = error < 1E-3
        assert success, '|area_exact - self.area()| = %g !=0' %error   
        
        
class Rectangle:
    def __init__(self, W, H, LC):
        self.W = W
        self.H = H
        self.LC = LC
        
        
    def area(self):
        return(self.W*self.H)
    
    def perimeter(self):
        return(2*(self.W + self.H))
    
    def test_area(self):
        H = 2
        W = 3
        area_exact = H*W
        error = np.abs(area_exact - self.area())
        success = error < 1E-3
        assert success, '|area_exact - self.area()| = %g !=0' %error
        
        
    def test_perimeter(self):
        H = 2
        W = 3
        perimeter_exact = 2*(H+W)
        error = np.abs(perimeter_exact - self.perimeter())
        success = error < 1E-3
        assert success, '|area_exact - self.area()| = %g !=0' %error          
        
# counterclockwise!!! or area will be negative
v1 = (2,3); v2 = (0,2); v3 = (1,1)
vertices = [v1, v2, v3]

t = Triangle(vertices)
t.test_area()
t.test_perimeter()
print("Triangle area is %5.5f and perimeter is %5.5f" % (t.area(), t.perimeter()))


LC = (1,2)
r = Rectangle(3,2,LC)
r.test_area()
r.test_perimeter()
print("Rectangle area is %5.5f and perimeter is %5.5f" % (r.area(), r.perimeter()))


"""
Program output:
    Triangle area is 1.50000 and perimeter is 5.88635
    Rectangle area is 6.00000 and perimeter is 10.00000
"""