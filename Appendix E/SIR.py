import numpy as np
from matplotlib.pylab import *
import math as math

class ForwardEuler:
    def __init__(self, f, b, v, U0, T, n):
        self.f, self.b,self.v, self.U0, self.T, self.n = f, b, v, U0, T, n
        self.dt = T/float(n)
        self.u = np.zeros((n+1, 3))
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
         u, b, v, dt, f, k, t = self.u,self.b,self.v, self.dt, self.f, self.k, self.t
         K1 = np.multiply(dt,f(u[k,:], t[k], b, v))
         K2 = np.multiply(dt,f(u[k,:]+np.multiply(0.5,K1), t[k]+0.5*dt, b, v))
         u_new = u[k,:] + K2
         return(u_new)
   
def f(u, t, b, v):
    S, I, R = u
    return([-b*S*I,b*S*I-v*I,v*I]) 

def graph(S,I,R,t):
    plot(t, S, 'r-')
    hold('on')
    plot(t, I, 'b-')
    hold('on')
    plot(t, R, 'g-')
    xlabel('t')
    ylabel('u')
    legend(['S', 'I', 'R'])
    title("SIR model")
    show()
    
        
 
        
 

b = 0.0005
v = 0.1
solver =  ForwardEuler(f, b, v, U0=[1500,1,0], T=60 ,n=120) 
u, t = solver.solve_Runge_Kutta()  
S = u[:,0]
I = u[:,1]
R = u[:,2]
graph(S,I,R,t)


    
    
    

"""
   solved using 2nd order Runge Kutta method
Program output:
   beta = 0.0005, peak of contamination reached after around 18 days
   beta = 0.0003, peak of contamination reached after around 25 days
   beta = 0.0001, (increased precautions) almost noone got infected 
       and only around 60 days we can see a slightly increased number 
       of infected people in a sample
    
"""    



