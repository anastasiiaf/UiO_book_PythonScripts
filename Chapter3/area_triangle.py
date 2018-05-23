# Exercise 3.11???? area triangle

#http://mathworld.wolfram.com/TriangleArea.html
#https://stackoverflow.com/questions/20978757/how-to-append-a-vector-to-a-matrix-in-python
import numpy as np
def area(vertices):
    h = np.array(vertices)
    v = np.ones((3,1))
    matrix = np.c_[h, v]
    area = 1/2*(np.linalg.det(matrix))
    return(area)
# counterclockwise!!! or area will be negative
v1 = (2,3); v2 = (0,2); v3 = (1,1)
vertices = [v1, v2, v3]
print("Area of triangle area is %.2f" % area(vertices))

