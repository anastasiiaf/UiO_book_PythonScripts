# fortune_and_inflation1
from matplotlib.pylab import *


def function(prev_x, p, q, I, N):
    prev_c = p*q/1000.0*prev_x
    for_plot = []
    for_plot.append(prev_x)
    n = 1
    while n<=N:
          curr_x = prev_x + (p/100.0)*prev_x - prev_c
          for_plot.append(curr_x)
          curr_c = prev_c + I/100.0*prev_c
          prev_x = curr_x
          prev_c = curr_c
          n = n + 1
    return(for_plot)


prev_x = 100
p = 5
q = 3
I = 2
N = 4
for_plot = function(prev_x, p, q, I, N)      
print(for_plot)
x = range(N+1)
plot(x, for_plot, 'r-')
xlabel('years')
ylabel('x')
title('Making a living from a fortune')
show()




