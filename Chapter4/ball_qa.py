#4.9 ball.qa

#t = input('t=? ')
#try:
#    t = float(t)
#except:
#
#    while type(t) not in (float, int):
#        t = input('t=? ')
#        try:
#            t = float(t)
#        except:
#            continue
#
#
#v0 = input('v0=? ')
#try:
#    v0 = float(v0)
#except:
#
#    while type(v0) not in (float, int):
#        v0 = input('v0=? ')
#        try:
#            v0 = float(v0)
#        except:
#            continue
t = input('t=? ')
t = float(t)
v0 = input('v0=? ')
v0 = float(v0)
g = 9.81
y = v0*t-0.5*g*t**2
print(y)

