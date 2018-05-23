import numpy as np
from matplotlib.pylab import *
import math as math

class Decay:
    def __init__(self, a):
        self.a = a
        self.dt = float(500)
        self.n = int(20000/500)
        self.u = np.zeros(self.n+1)
        self.t = np.zeros(self.n+1)
        
    def __call__(self):
        self.u[0] = float(1)
        self.t[0] = float(0)
        for k in range(self.n):
            self.k = k
            self.t[k+1] = self.t[k] + self.dt
            self.u[k+1] = self.advance()
        return(self.u, self.t)    
        
    def advance(self):
         u, dt,  k, t, a = self.u, self.dt,  self.k, self.t, self.a
         u_new = u[k] + dt*f(-a*u[k], t[k])
         return(u_new)
 
def f(u, t):
    return(u) 

def exact(a):
    dt = float(500)
    n = int(20000/500)
    u = np.zeros(n+1)
    t = np.zeros(n+1)
    u[0] = 1
    t[0] = 0
    
    for i in range(1, n+1):
        t[i] = t[i-1] + dt
        u[i] = math.exp(-a*t[i])
    return(u, t)

def graph(u_ex, t_ex, u, t):
    plot(t_ex, u_ex, 'r-')
    hold('on')
    plot(t, u, 'bo')
    xlabel('t')
    ylabel('decay')
    legend(['Exact solution', 'Approximation'])
    title("Radioactive decay: ODE u'=-au, u(0)=1")
    show()


a = math.log(2)/5600
d = Decay(a)
u, t = d.__call__()
u_ex, t_ex = exact(a)
graph(u_ex, t_ex, u, t)

print("Final results: u(T)= %5.5f and exact value exp(-aT)= %5.5f" %(u[-1], u_ex[-1]))

"""
Program output:
    Final results: u(T)= 0.07766 and exact value exp(-aT)= 0.08412
    Run program to see the graph
"""

