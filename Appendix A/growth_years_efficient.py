# growth_years_efficient
import numpy as np
x0 = 100
p = 5
n = 4
# was before
index_set = range(n+1)
x = np.zeros(len(index_set))

x[0] = x0
for n in index_set[1:]:
      x[n] = x[n-1]+(p/100.0)*x[n-1]
print(x)

# reshaped with while loop and two variables
n = 1
for_plot = []
for_plot.append(x0) 
prev = for_plot[0]     
while n<=4:
      curr = prev + (p/100.0)*prev
      for_plot.append(curr)
      prev = curr
      n = n + 1
print(for_plot)

"""
Output
[100, 105.0, 110.25, 115.7625, 121.550625]



"""
