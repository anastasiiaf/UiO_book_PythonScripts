# Exercise 3.16 Implement a Gaussian function

def gauss(x, m=0, s=1):
    function = 1/(math.sqrt(2*math.pi)*s)*math.exp(-0.5*((x-m)/s)**2)
    return(function)

m = 0
s = 3
n = 10
step = 10*s/n   #(m + 5*s - m + 5*s)/n
for i in range(0, n):
    x_value = m - 5*s + step*i
    function = gauss(x_value, m, s)
    print('%5.1f  %5.4f'% (x_value, function))