#4.12 ball_cml_tcheck
import sys
t = float(sys.argv[1])
v0 = float(sys.argv[2])
g = 9.81
if not  0 < t < 2*v0/g:
    print("Error! Time value is not in range (%3.3f;%3.3f)" % (0, 2*v0/g))
    sys.exit(1)
else:
    y = v0*t-0.5*g*t**2
    print(y)

# to call: type in console run ball_cml_tcheck.py 2 2