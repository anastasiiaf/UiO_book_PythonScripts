# oscilating_spring
import numpy as np
import math as math
from matplotlib.pylab import *

def y(t):
    y = A*np.exp(-gamma*t)*np.cos(np.sqrt(k/m)*t)
    return(y)

m = 9
A = 0.3
k = 4
gamma = 1/0.15

#(a)
step = (25-(0))/101
t_array = [0 + step*i for i in range(0,101)]
y_array = [A*math.exp(-gamma*t)*math.cos(math.sqrt(k/m)*t) for t in t_array]

#(b)
t_array2 = np.linspace(0, 25, 101)
y_array2 = y(t_array2)

#(c)
plot(t_array, y_array, 'r-')
hold('on')
plot(t_array, y_array2, 'bo')
xlabel('t')
ylabel('y')
legend(['scalar code', 'vectorized code'])
title('Oscilating spring')
show()