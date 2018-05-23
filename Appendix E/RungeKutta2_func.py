import numpy as np
from matplotlib.pylab import *
import math as math

class ForwardEuler:
    def __init__(self, f, U0, T, n):
        self.f, self.U0, self.T, self.n = f, U0, T, n
        self.dt = T/float(n)
        self.u = np.zeros(n+1)
        self.t = np.zeros(n+1)
        
    def solve_Runge_Kutta(self):
        self.u[0] = float(self.U0)
        self.t[0] = float(0)
        for k in range(self.n):
            self.k = k
            self.t[k+1] = self.t[k] + self.dt
            self.u[k+1] = self.advance()
        return(self.u, self.t)    
        
    def advance(self):
         u, dt, f, k, t = self.u, self.dt, self.f, self.k, self.t
         K1 = dt*f(u[k], t[k])
         K2 = dt*f(u[k]+0.5*K1, t[k]+0.5*dt)
         u_new = u[k] + K2
         return(u_new)
 
def f(u, t):
    return(u) 

def exact(U0, T, n):
    u = np.zeros(n+1)
    t = np.zeros(n+1)
    u[0] = U0
    t[0] = 0
    dt = T/n
    for i in range(1, n+1):
        t[i] = t[i-1] + dt
        u[i] = math.exp(t[i])
    return(u, t)    
        
    

def graph(u_ex, t_ex, u_RK, t_RK):
    plot(t_ex, u_ex, 'r-')
    hold('on')
    plot(t_RK, u_RK, 'bo')
    xlabel('t')
    ylabel('u')
    legend(['Exact solution', 'Runge-Kutta'])
    title("ODE u'=u, u(0)=1")
    show()

def test():
    solver =  ForwardEuler(f, U0=1, T=4, n=50) 
    u, t = solver.solve_Runge_Kutta()  
    u1, t1 = exact(U0=1, T=4, n=50) 
    error = np.abs(u1[0:2] - u[0:2]).max()
    success = error < 1E-5
    assert success, '|exact - u| = %g !=0' %error
    
    


solver =  ForwardEuler(f, U0=1, T=4, n=50) 
u_RK, t_RK = solver.solve_Runge_Kutta()  

u_ex, t_ex = exact(U0=1, T=4, n=50) 

graph(u_ex, t_ex, u_RK, t_RK)
test()

    
    
    

"""
ODE u'=u, u(0)=1
Program output:
    a)
    parametrs: U0=1, T=4, n=5
    Test function: AssertionError: |exact - u|  = 0.105541 !=0
    Run the program to see the graph
    
    b)
    parametrs: U0=1, T=4, n=10
    Test function: AssertionError: |exact - u| = 0.0118247 !=0
    Run the program to see the graph

    c) 
    parametrs: U0=1, T=4, n=50
    Test function:  AssertionError:|exact - u| = 8.70677e-05 !=0
    Run the program to see the graph   
    
"""    



