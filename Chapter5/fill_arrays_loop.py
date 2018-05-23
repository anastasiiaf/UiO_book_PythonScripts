# 5.2 fill_arrays_loop
import numpy as np
import math as math
step = (4-(-4))/41
x = [-4 + step*i for i in range(0,41)]
y = [1/(math.sqrt(2*math.pi)*math.exp(-0.5*i**2)) for i in x]
print(y)  



