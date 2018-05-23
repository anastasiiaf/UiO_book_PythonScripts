import numpy as np
import math as math
from matplotlib.pylab import *

def S(t, n):
    T = 2*math.pi
    y = [(1/(2*i - 1)*math.sin(2*(2*i-1)*math.pi*t/T)) for i in range(1, n+1)]
    return(4/math.pi*sum(y))

def f(t):
    T = 2*math.pi
    if 0<t<T/2:
        y = 1
    elif t == T/2:
        y = 0
    else:
        y = -1
    return(y) 

T = 2*math.pi
alpha = 0.49
t = alpha*T   

n = [1, 3, 10, 20, 50, 100, 150, 200, 300, 400, 500]  # [1,3,20,200]
s_approx = [S(t, n[i]) for i in range(0, len(n))]    
s_exact = [f(t)]*len(n)

plot(n, s_exact, 'r-')
hold('on')
plot(n, s_approx, 'bo')
xlabel('n')
ylabel('f(x)')
legend(['exact', 'approximation'])
title('Sum of sines approximation')
show()