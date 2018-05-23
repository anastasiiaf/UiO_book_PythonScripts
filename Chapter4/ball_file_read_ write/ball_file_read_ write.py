#4.14 ball_file_read_ write


#(a)
def read_from_file(file_name):
    with  open(file_name, 'r') as data:
        first = data.readline().split()
        v0 = float(first[1])
        data.readline()
        t = [float(i) for i in data.read().split()]
    print("v0: %5.3f" %v0)    
    print("t:", t) 
    return(v0, t)

#(b)
def write_to_file(y, t):
    data2 = open('data2.txt', 'w')
    data2.write('t        y\n')
    for i in range(0, len(t)-1):
        data2.write('%5.5f  %5.5f \n' %(t[i], y[i]))
            
def function(v0, t):
    y = [v0*t[i] - 0.5*9.81*t[i]**2 for i in range(0, len(t)-1)]
    write_to_file(y, t)
    return(y)

#(c)
def test():
    v0 = 10.0
    t = [0.25592, 0.38075, 0.46807889, 0.45, 0.67681501876,
         0.31342619, 0.1519085, 0.142, 0.37, 0.60620017, 0.628,
         0.31385894, 0.4464815, 0.67982969, 0.20262264,
         0.39584013, 0.27383923]
    v0_test, t_test = read_from_file('test.txt')
    success1 = v0 - v0_test  == 0
    s = [t[i] - t_test[i] for i in range(0, len(t)-1)]
    success2 = sum(s) == 0
    msg = "Error! Data is not the same"
    assert (success1 and success2), msg

v0, t = read_from_file('data.txt')
t.sort()
function(v0, t)
test()
