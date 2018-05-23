
# bjerrum_plot
from matplotlib.pylab import *
K1 = 5.01*math.pow(10, -7)
K2 = 4.79*math.pow(10, -11)
ph = np.linspace(1, 12, 100)   # pH = -log(H+)   http://academic.brooklyn.cuny.edu/biology/bio4fv/page/ph_def.htm

CO2 = np.exp(-ph**2)/(np.exp(-ph**2) + K1*np.exp(-ph) + K1*K2)
HCO3 = K1*np.exp(-ph)/(np.exp(-ph**2) + K1*np.exp(-ph) + K1*K2)
CO3 = K1*K2/(np.exp(-ph**2) + K1*np.exp(-ph) + K1*K2)


plot(ph, CO2, 'r-')
hold('on')
plot(ph, HCO3, 'b-')
plot(ph, CO3, 'g-')
xlabel('pH')
legend(['CO2', 'HCO3', 'CO3'])
title('Bjerrumplot')
show()


plot(ph, CO2, 'r-')
hold('on')
plot(ph, HCO3, 'b-')
idx = np.argwhere(np.diff(np.sign(CO2 - HCO3)) != 0).reshape(-1) + 0  #https://stackoverflow.com/questions/28766692/intersection-of-two-graphs-in-python-find-the-x-value
plot(ph[idx], CO2[idx], 'mo')
xlabel('pH')
legend(['CO2', 'HCO3'])
title('CO2 vs. HCO3')
show()
try:
    print('intersection: concentration = %5.5f, pH = %5.5f' % (CO2[idx],ph[idx]))
except:
    print('Series are not intercepted!')


plot(ph, HCO3, 'b-')
hold('on')
plot(ph, CO3, 'g-')
idx = np.argwhere(np.diff(np.sign(CO3 - HCO3)) != 0).reshape(-1) + 0
plot(ph[idx], CO3[idx], 'mo')
xlabel('pH')
legend(['HCO3', 'CO3'])
title('HCO3 vs. CO3')
show()
try:
    print('intersection: concentration = %5.5f, pH = %5.5f' % (CO3[idx],ph[idx]))
except:
    print('Series are not intercepted!')








