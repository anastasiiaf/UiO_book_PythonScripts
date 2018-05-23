import numpy as np
from matplotlib.pylab import *
import math as math
import ODESolver

class ProblemSIR:
    def __init__(self,  b, v, p, U0, T):
     
        if isinstance(b, (float, int)):
            self.b = lambda t: b
        elif callable(b):
            self.b = b
            
        if isinstance(v, (float, int)):
            self.v = lambda t: v
        elif callable(v):
            self.v = v    
            
        if isinstance(p, (float, int)):
            self.p = lambda t: p
        elif callable(p):
            self.p = p
            
        self.U0, self.T =  U0, T
        
    def __call__(self, u, t):
        S, I, R, V = u
        return([-self.b(t)*S*I-self.p(t)*S, self.b(t)*S*I-self.v(t)*I, self.v(t)*I, self.p(t)*S])
        
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
        self.S, self.I, self.R, self.V  = u[:,0], u[:,1], u[:,2], u[:,3]
        return(self.I)
        
                
    def graph(self):
        plot(self.t, self.S, 'r-')
        hold('on')
        plot(self.t, self.I, 'b-')
        hold('on')
        plot(self.t, self.R, 'g-')
        hold('on')
        plot(self.t, self.V, 'm-')
        xlabel('t')
        ylabel('u')
        legend(['S', 'I', 'R'])
        title("SIRV model")
        print("Maximum number of contaminated people is %3.0f" % max(self.I))
        show()
 

inf = []; t = []  
for i in range(0,32):
    problem = ProblemSIR(b=0.0005, v=0.1, p=lambda t: 0.1 if 6<=t<=6+i else 0, U0=[1500,1,0,0], T=60)
    solver =  SolverSIR(problem, dt=0.5)
    I = solver.solve(method=ODESolver.RungeKutta)
    inf.append(max(I))
    t.append(i)
    
plot(t, inf, 'r-')
xlabel('t')
ylabel('infected people')
legend(['Vt'])
title("Optimal vaccination period")
show()    
    
    
    
    

"""
   solved using 2nd order Runge Kutta method
Program output:
   The optimal vaccination period starting from the 6th day should end around 6+7=13th day
   ("elbow plot": after around 6-7 days of vaccination this campaign has a negligible effect)
   
    
"""    



