import numpy as np
from matplotlib.pylab import *
import math as math

class ForwardEuler:
    def __init__(self, f, b, v, p, U0, T, n):
        self.f, self.b,self.v,self.p, self.U0, self.T, self.n = f, b, v, p, U0, T, n
        self.dt = T/float(n)
        self.u = np.zeros((n+1, 4))
        self.t = np.zeros(n+1)
        
    def solve_Runge_Kutta(self):
        self.u[0,:] = list(map(float, self.U0))
        self.t[0] = float(0)
        for k in range(self.n):
            self.k = k
            self.t[k+1] = self.t[k] + self.dt
            self.u[k+1,:] = self.advance()    
        return(self.u, self.t)    
        
    def advance(self):
         u, b, v, p, dt, f, k, t = self.u,self.b,self.v, self.p, self.dt, self.f, self.k, self.t
         K1 = np.multiply(dt,f(u[k,:], t[k], b, v, p))
         K2 = np.multiply(dt,f(u[k,:]+np.multiply(0.5,K1), t[k]+0.5*dt, b, v, p))
         u_new = u[k,:] + K2
         return(u_new)
 
def f(u, t, b, v, p):
    S, I, R, V = u
    return([-b*S*I-p*S, b*S*I-v*I, v*I, p*S]) 

  

def graph(S,I,R,V,t):
    plot(t, S, 'r-')
    hold('on')
    plot(t, I, 'b-')
    hold('on')
    plot(t, R, 'g-')
    hold('on')
    plot(t, V, 'm-')
    xlabel('t')
    ylabel('u')
    legend(['S', 'I', 'R', 'V'])
    title("SIRV model")
    print("Maximum number of contaminated people is %3.0f" % max(I))
    show()
  

b = 0.0005
v = 0.1
p = 0.1
solver =  ForwardEuler(f, b, v, p, U0=[1500,1,0, 0], T=60 ,n=120) 
u, t = solver.solve_Runge_Kutta()  
S = u[:,0]
I = u[:,1]
R = u[:,2]
V = u[:,3]
graph(S,I,R,V,t)


    
    
    

"""
    solved using 2nd order Runge Kutta method
Program output:
    b=0.0005 and without vaccination:
    Maximum number of infected people is 897
    
    b=0.0005 and with vaccination:
    Maximum number of infected people is 64
    
"""    



