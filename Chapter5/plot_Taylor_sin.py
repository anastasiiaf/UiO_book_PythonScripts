# plot_Taylor_sin
import math as math
import numpy as np
from matplotlib.pylab import *
def S(x, n):
    s_appr = []
    for i in range(0, len(x)): 
         s_appr.append(sum( [math.pow(-1,j)*(math.pow(x[i],(2*j+1)))/(math.factorial(2*j+1)) for j in range(0, n+1)] ))
    return(s_appr)

def plot_Taylor(x, y, n):

    y_app = S(x, n) 
  
    fig, ax1 = subplots()
    ax2 = ax1.twinx()
    ax1.plot(x, y, 'r-')
    #hold('on')
    ax2.plot(x, y_app, 'bo')
    ax1.set_xlabel('x')
    ax1.set_ylabel('sin(x)', color='r')
    ax2.set_ylabel('approx sin(x)', color='b') 
    title('Taylor approximation of sin(x)')
    show()


x = np.linspace(0, 4*math.pi, 100)
y = np.sin(x)

plot_Taylor(x, y, 1)
plot_Taylor(x, y, 2)
plot_Taylor(x, y, 3)
plot_Taylor(x, y, 6)
plot_Taylor(x, y, 12)
plot_Taylor(x, y, 14)
plot_Taylor(x, y, 16)

