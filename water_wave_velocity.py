from matplotlib.pylab import *
import math as math
import numpy as np

def wave_speed(L):
    g = 9.81; s = 7.9*1/(10**2); r = 1000; h = 50
    y = [math.sqrt(g*l/(2*math.pi)*(1+s*(4*math.pi**2)/(r*g*l**2))*math.tanh(2*math.pi*h/l)) for l in L]
    return(y)

def plot_speed(l, y):
    plot(l1, y, 'r-')
    xlabel('x')
    ylabel('f(x)')
    legend(['wave speed'])
    title('Wave speed')
    show()

l1 = np.linspace(0.001, 0.1, 10000)    
y = wave_speed(l1)
plot_speed(l1, y)


l2 = np.linspace(0.001, 2000, 10000) 
y = wave_speed(l2)
plot_speed(l2, y)