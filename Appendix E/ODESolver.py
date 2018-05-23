import numpy as np
from matplotlib.pylab import *
import math as math

class ODESolver:
    def __init__(self, f):
        self.f = lambda u, t: np.asarray(f(u, t), float)
        
    def advance(self):
        raise NotImplementedError
         
    def set_initial_condition(self, U0):
        if isinstance(U0, (float, int)):
            self.neq = 1
            U0 = float(U0)
        else:
            U0 = np.asarray(U0)
            self.neq = U0.size
        self.U0 = U0
        
    def solve(self, time_points, terminate=None):
        if terminate is None:
            terminate = lambda u, t, step_no: False
            
        self.t = np.asarray(time_points)
        n = self.t.size
        if self.neq == 1:
            self.u = np.zeros(n)
        else:
            self.u = np.zeros((n, self.neq))
            
        self.u[0] = self.U0 
        
        for k in range(n-1):
            self.k = k
            self.u[k+1] = self.advance()
            if terminate(self.u, self.t, self.k+1):
                break
        return(self.u[:k+2], self.t[:k+2])  
    
    
class RungeKutta(ODESolver):

        
    def advance(self):
         u,  f, k, t = self.u, self.f, self.k, self.t
         dt = t[k+1] - t[k]
         K1 = dt*f(u[k], t[k])
         K2 = dt*f(u[k]+0.5*K1, t[k]+0.5*dt)
         u_new = u[k] + K2
         return(u_new)    