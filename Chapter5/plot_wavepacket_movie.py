
# plot_wavepacket_movie
import math as math
import numpy as np
from matplotlib.pylab import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import glob, os

def f(x, t):
    y = np.exp(-(x-3*t**2))*np.sin(3*np.pi*(x-t))
    return(y)

def init():
      lines[0].set_data([],[])
      return(lines)

def frame(args):
      frame_no, x, t, lines = args
      y = f(x, t)
      lines[0].set_data(x,y)
      return(lines)
      
for filename in glob.glob('tmp*.png'):
      os.remove(filename)



x = np.linspace(-6, 6, 1000)
t = np.linspace(-1, 1, 1000)
fig = plt.figure()
plt.axis([x[0], x[-1], min(y), max(y)])
lines = plt.plot([],[])
plt.xlabel('x')
plt.ylabel('f(x)')

all_args = [(frame_no, x, t,  lines)
            for frame_no, t in enumerate(t)]
anim = animation.FuncAnimation(fig, frame, all_args, interval = 150, init_func = init, blit = True)
#anim.save('movie1.mp4', fps=5)
plt.show()


