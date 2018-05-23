#compute_prob.py
import random
for i in [1,2,3,6]:
    N = 10**i
    set = [random.uniform(0,1) for i in range(1, N+1)]
    M = [1  for i in range(0,len(set)-1) if 0.5 <= set[i] <= 0.6] 
    Prob = sum(M)/N
    print("Probability of a number to be in range [0.5,0.6] with %5.0f draws is %5.3f" %(N,Prob))
    
    
"""
Program output:
    Probability of a number to be in range [0.5,0.6] with    10 draws is 0.200
    Probability of a number to be in range [0.5,0.6] with   100 draws is 0.120
    Probability of a number to be in range [0.5,0.6] with  1000 draws is 0.104
    Probability of a number to be in range [0.5,0.6] with 1000000 draws is 0.100

"""    