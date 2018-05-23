#4.10 ball_cml

import sys
t = float(sys.argv[1])
v0 = float(sys.argv[2])
g = 9.81
y = v0*t-0.5*g*t**2
print(y)

# to call: type in console run ball_cml.py 2 2