#one6_ndice.py
import sys
import numpy as np
n = int(sys.argv[1])
N = int(sys.argv[2])


def dice(n):
    i = 1
    d = []
    while i<=n:
        d.append(np.random.randint(1,7))
    return(d)
    
d = np.random.randint(1,7, size=(n,N))
#d = np.transpose(d)
M = [1  for i in range(0,N) if sum(d[:,i] == 6) >= 1] 
#M = [sum(d[:,i] == 6)  for i in range(0,n) if sum(d[:,i] == 6) >= 1] 

Prob = sum(M)/N
print("""Probability of at least one dice with 6 eyes throwing %3.0f dices
%3.0f times is %5.6f, exact solution is 11/36=0.3055555555555556""" %(n,N,Prob))
   
# to call: type in console run one6_ndice.py 2 1000    

"""
Program output:
   run one6_ndice.py 2 10
       Probability of at least one dice with 6 eyes throwing   2 dices
 10 times is 0.100000, exact solution is 11/36=0.3055555555555556
       
   run one6_ndice.py 2 100
        Probability of at least one dice with 6 eyes throwing   2 dices
        100 times is 0.290000, exact solution is 11/36=0.3055555555555556    

   run one6_ndice.py 2 1000
        Probability of at least one dice with 6 eyes throwing   2 dices
        1000 times is 0.304000, exact solution is 11/36=0.3055555555555556

   run one6_ndice.py 2 10000
        Probability of at least one dice with 6 eyes throwing   2 dices
        10000 times is 0.296900, exact solution is 11/36=0.3055555555555556

   run one6_ndice.py 2 100000
        Probability of at least one dice with 6 eyes throwing   2 dices
        100000 times is 0.307070, exact solution is 11/36=0.3055555555555556

   run one6_ndice.py 2 1000000
        Probability of at least one dice with 6 eyes throwing   2 dices
        1000000 times is 0.305511, exact solution is 11/36=0.3055555555555556
        
   run one6_ndice.py 2 10000000
        Probability of at least one dice with 6 eyes throwing   2 dices
        10000000 times is 0.305809, exact solution is 11/36=0.3055555555555556      

"""