from matplotlib.pylab import *

F = [10*i for i in range (-2, 13)]

C_exact = [ (f-32)*5/9.0 for f in F]
C_approx = [(f-30)/2 for f in F]

plot(F, C_exact, 'r-')
hold('on')
plot(F, C_approx, 'bo')
xlabel('Fahrenheit')
ylabel('Celsius')
legend(['Exact', 'Approximated'])
title('Fahrenheit-Celsius convertion')
show()