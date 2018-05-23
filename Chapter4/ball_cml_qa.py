#4.11 ball_cml_qa
import sys
try:
    t = float(sys.argv[1])
except IndexError:
    print("Time value is missing!")   
    t = input('t=? ')
    t = float(t)
try:
    v0 = float(sys.argv[2])
except IndexError:
    print("Speed value is missing!")  
    v0 = input('v0=? ')
    v0 = float(v0)
g = 9.81
y = v0*t-0.5*g*t**2
print(y)

# to call: type in console run ball_cml_qa.py 2 2