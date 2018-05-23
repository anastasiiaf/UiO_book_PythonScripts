#4.16 stopping_length
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--v0', '--initial speed, km/h', type=float, default=1, help='km/h', metavar='v0')
parser.add_argument('--m', '--initial m', type=float, default=1, help='no units', metavar='m')
args = parser.parse_args()
g = 9.81
d = 0.5*(((args.v0/1000*3600)**2)/(args.m*g))
print(d)

# call: run stopping_length.py --v0 1 --m 1
# run stopping_length.py --v0 1