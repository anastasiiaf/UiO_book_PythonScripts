from matplotlib.pylab import *
import math as math

x = [i for i in range (-4, 5)]
t = 0
y = [math.exp(-(i-3*t)**2)*math.sin(3*math.pi*(i-t)) for i in x]


plot(x, y, 'r-')
xlabel('x')
ylabel('f(x)')
legend(['wave packey, t=0'])
title('Wave packet')
show()
