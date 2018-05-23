import numpy as np
from matplotlib.pylab import *
import math as math
import ODESolver


class ProblemSIZR:
    def __init__(self,  s, b, d_s, d_i, p, a,  U0, T):
        
        if isinstance(s, (float, int)):
            self.s = lambda t: s
        elif callable(s):
            self.s = s
        
        if isinstance(b, (float, int)):
            self.b = lambda t: b
        elif callable(b):
            self.b = b
            
        if isinstance(d_s, (float, int)):
            self.d_s = lambda t: d_s
        elif callable(d_s):
            self.d_s = d_s  
            
        if isinstance(d_i, (float, int)):
            self.d_i = lambda t: d_i
        elif callable(d_i):
            self.d_i = d_i    
            
        if isinstance(p, (float, int)):
            self.p = lambda t: p
        elif callable(p):
            self.p = p
            
        if isinstance(a, (float, int)):
            self.a = lambda t: a
        elif callable(a):
            self.a = a
            
        self.U0, self.T =  U0, T
        

        
    def __call__(self, u, t):
        S, I, Z, R = u
        return([self.s(t)-self.b(t)*S*Z-self.d_s(t)*S, self.b(t)*S*Z-self.p(t)*I-self.d_i(t)*I,
                self.p(t)*I-self.a(t)*S*Z, self.d_s(t)*S+self.d_i(t)*I+self.a(t)*S*Z])
        
class SolverSIZR:
    def __init__(self,  problem, dt):
        self.problem, self.dt = problem, dt
        
        
    def solve(self, method=ODESolver.RungeKutta):
        self.solver = method(self.problem)
        ic = self.problem.U0
        self.solver.set_initial_condition(ic)
        n = int(round(self.problem.T/float(self.dt)))
        t = np.linspace(0, self.problem.T, n+1)
        print(n)
        u, self.t = self.solver.solve(t)
        self.S, self.I, self.Z, self.R  = u[:,0], u[:,1], u[:,2], u[:,3]
        
                
    def graph(self):
        plot(self.t, self.S, 'g-')
        hold('on')
        plot(self.t, self.I, 'b-')
        hold('on')
        plot(self.t, self.Z, 'r-')
        hold('on')
        plot(self.t, self.R, 'm-')
        xlabel('t')
        ylabel('u')
        legend(['S', 'I', 'Z', 'R'])
        title("SIRV model")
        show()
 

def sigma(t):
    if t<=4:
        return(20)
    elif t>4 and t<=28:
        return(2)
    else:
        return(0)
def beta(t):
    if t<=4:
        return(0.03)
    elif t>4 and t<=28:
        return(0.0012)
    else:
        return(0) 
def alpha(t):
    if t<=4:
        return(0)
    elif t>4 and t<=28:
        return(0.0016)
    else:
        return(0)
def delta_i(t):
    if t<=4:
        return(0)
    elif t>4 and t<=28:
        return(0.014)
    else:
        return(0) 
def delta_s(t):
    if t<=4:
        return(0)
    elif t>4 and t<=28:
        return(0)
    else:
        return(0.0067)    
    


problem = ProblemSIZR(s=sigma, b=beta, d_s=delta_s, 
                      d_i=delta_i, p=lambda t: 1 , a=alpha, 
                      U0=[60, 0, 1, 0], T=33)



solver =  SolverSIZR(problem, dt=1)
solver.solve(method=ODESolver.RungeKutta)
solver.graph()




    
    

"""
    solved using 2nd order Runge Kutta method
Program output:
    see graph: zombies defeated humans
   
    
"""    



