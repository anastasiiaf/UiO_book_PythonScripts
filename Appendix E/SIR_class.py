import numpy as np
from matplotlib.pylab import *
import math as math
import ODESolver

class ProblemSIR:
    def __init__(self,  b, v, U0, T):
     
        if isinstance(b, (float, int)):
            self.b = lambda t: b
        elif callable(b):
            self.b = b
            
        if isinstance(v, (float, int)):
            self.v = lambda t: v
        elif callable(v):
            self.v = v    
        self.U0, self.T =  U0, T
        
    def __call__(self, u, t):
        S, I, R = u
        return([-self.b(t)*S*I,self.b(t)*S*I-self.v(t)*I,self.v(t)*I])
        
class SolverSIR:
    def __init__(self,  problem, dt):
        self.problem, self.dt = problem, dt
        
        
    def solve(self, method=ODESolver.RungeKutta):
        self.solver = method(self.problem)
        ic = self.problem.U0
        self.solver.set_initial_condition(ic)
        n = int(round(self.problem.T/float(self.dt)))
        t = np.linspace(0, self.problem.T, n+1)
        u, self.t = self.solver.solve(t)
        self.S, self.I, self.R = u[:,0], u[:,1], u[:,2]
        
                
    def graph(self):
        plot(self.t, self.S, 'r-')
        hold('on')
        plot(self.t, self.I, 'b-')
        hold('on')
        plot(self.t, self.R, 'g-')
        xlabel('t')
        ylabel('u')
        legend(['S', 'I', 'R'])
        title("SIR model")
        print("Maximum number of contaminated people is %3.0f" % max(self.I))
        show()
 

   

problem = ProblemSIR(b=lambda t: 0.0005 if t<=12 else 0.0001, v=0.1,U0=[1500,1,0], T=60)
solver =  SolverSIR(problem, dt=0.5)
solver.solve(method=ODESolver.RungeKutta)
solver.graph()


    
    
    

"""
   solved using 2nd order Runge Kutta method
Program output:
   b=0.0005 when t<=12 and b=0.0001 otherwise:
   Maximum number of infected people is 732
   
   b=0.0005:
   Maximum number of infected people is 897
    
"""    



